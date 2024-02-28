from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
path('accounts/', include('allauth.urls')), 
path('add_subscription/',views.add_subscription,name='add_subscription'),
path('paymenthandler_subscription/', views.paymenthandler, name='paymenthandler'),
path('paymentSubscription/<str:costdata>', views.paymentSubscription, name='paymentSubscription'),
path('book_event/', views.book_event, name='book_event'),


]