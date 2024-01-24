"""RTP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.homepageshow,name="homepage"),
    path('sell',views.sellfn,name='sellpage'),
    path('buy',views.buyfn,name='buypage'),
    path('cart', views.cartfn, name='cartpage'),
    path('user_register', views.registerfn, name='registerpage'),
    path('remove_item/<str:k1>', views.remove_itemfn, name='removepage'),
    path('checkout', views.checkoutfn, name='checkoutpage'),
    path('place_order', views.placeorderfn, name='placeorderpage'),
    path('my-orders',views.ordersfn,name='myorderspage'),
    # path('my-orderitems/<str:k2>', views.orderitemsfn, name='orderitemspage'),
    path('logout', views.logout, name='page004'),

    path('reviews', views.reviewsfn),

    # path('proceed-to-pay', views.razorpaycheckfn),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)