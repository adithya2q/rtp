import random

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app1.models import productsinput, cartitems, Orderdetails, Orderitems, Reviews


def homepageshow(request):
    if request.method == "POST":
        username = request.POST.get('uname',)
        password = request.POST.get('pword')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request,'User logged in successfully')
            return redirect('homepage')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('registerpage')

    reviewdata=Reviews.objects.all()
    context1={
        'con1':reviewdata
    }
    return render(request,'homepage.html',context1)


def buyfn(request):
    if request.method == "POST":
        product_id=request.POST.get('product_id',)
        quantity=int(request.POST.get('req_quantity'))
        selected_product=productsinput.objects.filter(id=product_id)
        selected_product2=productsinput.objects.get(id=product_id)
        for p in selected_product:
            unit_price=p.Price_per_kg
            img=p.Image
            seller_name=p.Name
            quantity_available=p.Quantity_For_Sale
        if quantity<=quantity_available:
            Sum_price=quantity*unit_price
            product,created=cartitems.objects.get_or_create(productname=selected_product2,quantity=quantity,Sum_price=Sum_price,
                                                            user=request.user,image=img,seller_name=seller_name)
            product.save()
            # new_quantity=quantity_available-quantity
            # selected_product2.Quantity_For_Sale=new_quantity
            # selected_product2.save()
            return redirect('cartpage')
        else:
            messages.info(request,"Quantity is unavailable")

    data=productsinput.objects.all()
    dict1={
        'key1':data
    }
    return render(request,'page2buy.html',dict1)



def sellfn(request):
    if request.method == "POST":
        productname=request.POST.get('np1',)
        name=request.POST.get('n1',)
        email=request.POST.get('e1',)
        phone_no=request.POST.get('p1',)
        address=request.POST.get('a1',)
        pincode=request.POST.get('pc1',)
        image=request.FILES['i1']
        quantity_for_sale=request.POST.get('q1',)
        price_per_kg=request.POST.get('pr1',)
        comments=request.POST.get('c1')
        info=productsinput(Productname=productname,Name=name,Email=email,PhoneNumber=phone_no,Address=address,PINCODE=pincode,Image=image,Quantity_For_Sale=quantity_for_sale,Price_per_kg=price_per_kg,Comments=comments)
        info.save()
    return render(request,'page3sell.html')



@login_required(login_url='homepage')
def cartfn(request):

    data2=cartitems.objects.all()
    dict2={
        'key2':data2
    }
    return render(request,'cart.html',dict2)

def registerfn(request):
    if request.method =="POST":
        u=request.POST.get('uname',)
        f=request.POST.get('fname',)
        l=request.POST.get('lname',)
        e=request.POST.get('email')
        p=request.POST.get('pass',)
        cp=request.POST.get('cpass')
        if p==cp:
            if User.objects.filter(username=u).exists():
                messages.info(request,'username taken')
                return redirect('registerpage')
            else:
                user1=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
                user1.save()
                messages.info(request,'user is registered')

    return render(request,'userregister.html')


def remove_itemfn(request,k1):
    item=cartitems.objects.get(id=k1)
    if request.method=="POST":
        item.delete()
        return redirect('cart.html')
    dict3={
        'key3':item
    }
    return render(request,'remove.html',dict3)


@login_required(login_url='homepage')
def checkoutfn(request):
    simplecart1=cartitems.objects.filter(user=request.user)
    for i in simplecart1:
        if i.quantity>i.productname.Quantity_For_Sale:
            cartitems.objects.delete(id=i.id)

    maincart1=cartitems.objects.filter(user=request.user)
    total_price=0
    for i in maincart1:
        total_price=total_price+i.Sum_price
    dict4={
        'key4':maincart1,
        'key5':total_price
    }
    return render(request,'checkout.html',dict4)

@login_required(login_url='homepage')
def placeorderfn(request):
    if request.method == "POST":
        neworder=Orderdetails()
        neworder.user=request.user
        neworder.First_name=request.POST.get('fname')
        neworder.Last_name=request.POST.get('lname')
        neworder.Email=request.POST.get('email')
        neworder.Phone=request.POST.get('phone')
        neworder.Address=request.POST.get('address')
        neworder.City=request.POST.get('city')
        neworder.State=request.POST.get('state')
        neworder.Country=request.POST.get('country')
        neworder.Pincode=request.POST.get('pincode')

        neworder.Payment_mode=request.POST.get('payment_mode')
        neworder.Payment_id=request.POST.get('payment_id')


        maincart1 = cartitems.objects.filter(user=request.user)
        total_price = 0
        for i in maincart1:
            total_price = total_price + i.Sum_price

        neworder.Total_price=total_price

        random_trackno='rtp'+str(random.randint(1000000,9999999))
        while Orderdetails.objects.filter(Tracking_id=random_trackno) is None:
            random_trackno = 'rtp' + str(random.randint(1000000, 9999999))

        neworder.Tracking_id=random_trackno
        neworder.save()

        neworderitems=cartitems.objects.filter(user=request.user)
        for i in neworderitems:
            Orderitems.objects.create(
            order=neworder,
            product=i.productname,
            unit_price_at_purchase=i.productname.Price_per_kg,
            quantity=i.quantity
            )

            # to decrease the product quantity from available stock
            orderproduct=productsinput.objects.filter(id=i.productname_id).first()
            orderproduct.Quantity_For_Sale=orderproduct.Quantity_For_Sale-i.quantity
            orderproduct.save()

        # to clear user's cart
        cartitems.objects.filter(user=request.user).delete()

        messages.success(request,"Your order has been placed successfully")

        paymode=request.POST.get('payment_mode')
        if (paymode == "Paid by Paypal"):
            return JsonResponse({"status":"Your order has been placed successfully"})
    return redirect('cartpage')




def ordersfn(request):
    orders=Orderdetails.objects.filter(user=request.user)
    context2={
        'orders':orders
    }
    return render(request,'myorders.html',context2)



#
# def orderitemsfn(reqeust,k2):
#     order = Orderdetails.objects.filter(Tracking_id=k2).first()
#     orderitems=Orderitems.objects.filter(order=order)
#     context3={
#         'order': order,
#         'orderitems':orderitems
#     }
#     return render(reqeust,'myorderitems.html',context3)




def reviewsfn(request):
    if request.method == "POST":
        name=request.POST.get('n1',)
        address=request.POST.get('a1',)
        phone=request.POST.get('p1',)
        email=request.POST.get('e1',)
        rev=request.POST.get('r1',)
        img=request.POST['e1']
        review1=Reviews(Name=name,Address=address,Phone=phone,Email=email,Review=rev,Image=img)
        review1.save()
    return HttpResponse("Review has been submitted")



def logout(request):
    auth.logout(request)
    return redirect('homepage')

# def razorpaycheckfn(request):
#     maincart1 = cartitems.objects.filter(user=request.user)
#     total_price = 0
#     for i in maincart1:
#         total_price = total_price + i.Sum_price
#
#     return JsonResponse({
#         'total_price':total_price
#     })