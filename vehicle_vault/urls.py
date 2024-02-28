"""
URL configuration for vehicle_vault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from vv import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('vv.urls')),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('book/<int:book_id>',views.book,name='book'),
    path('data/',views.showData,name='data'),
    path('addslot/', views.addslot, name='addslot'),
    path('add_rasperry/', views.add_rasperry, name='add_rasperry'),
    path('view_rasperry/', views.view_rasperry, name='view_rasperry'),
    path('delete/<int:delete_id>',views.delete,name='delete'),
    path('update/<int:update_id>',views.update,name='update'),
    path('slot/<int:park_id>',views.slot,name='slot'),
    path('profile/', views.profile,name='profile'),
    path('mybooking/', views.mybooking,name='mybooking'),
    path('delete_booking/<int:stid2>/', views.delete_booking, name="delete_booking"),
    path('calculate_cost/', views.calculate_cost, name='calculate_cost'),
    path('parkingcost/<int:costdata>/', views.payment, name='calculate_cost'),
    # path('parkingcost', views.parkingcost, name='parkingcost'),
    path('payment/<int:costdata>/', views.payment, name='payment'),
     path('show_activity/', views.show_activity, name='show_activity'),
      path('bill_generate/<str:entry>/<str:exit>', views.bill_generate, name='bill_generate'),
        path('generate_qr_code/<int:cost>/', views.generate_qr_code, name='generate_qr_code'),

    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    
    path('capture_image/', views.capture_image, name='capture_image'),
    
    # path('print_as_pdf/<int:booking_id>/', views.print_as_pdf, name='print_as_pdf'),

    path('process/',views.process_image,name='process'),
    path('process2/',views.process_image2,name='process2'),    
    path('process_image2/', views.process_image2, name='process_image2'),
    path('admin_feedback/', views.admin_feedback, name='admin_feedback'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)