from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class service_station(models.Model):
    stname = models.CharField(max_length=30, default='')    
    photo = models.ImageField(upload_to='pics', default='')
    latitude = models.CharField(max_length=12,null=True)
    longitude = models.CharField(max_length=12,null=True)
    maxslot = models.IntegerField(default='4')
    hidden = models.BooleanField(default=False)
    status= models.BooleanField(default=False)
    price = models.FloatField(default='10')
    place = models.CharField(default='', max_length=30)

    def str(self):
        return str(self.stname)
    
    
class Booking(models.Model):
    name=models.CharField(max_length=20, default='')
    head=models.ForeignKey(service_station,on_delete=models.CASCADE,null=True)
    phno=models.CharField(max_length=13)
    indate=models.DateField()
    intime=models.TimeField(default='00:00')
    outdate=models.DateField()
    outtime=models.TimeField(default='00:00')
    slot_id=models.IntegerField(null=True)
    hidden =models.BooleanField(default=False)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')

    def __str__(self):
        return f" {self.name}"
    

class rasperry(models.Model):
    entryvnumber=models.CharField(max_length=20, default='')
    entryvnumber=models.CharField(max_length=20, default='')
    head=models.ForeignKey(service_station,on_delete=models.CASCADE)
    entrydate=models.DateField()
    entrytime=models.TimeField(default='00:00')
    exitdate=models.DateField()
    exittime=models.TimeField(default='00:00')
    def __str__(self):
        return f"Rasperry entry {self.entryvnumber}"

class wallet(models.Model):
    entryvnumber=models.CharField(max_length=20, default='')
    entryvnumber=models.CharField(max_length=20, default='')
    head=models.ForeignKey(service_station,on_delete=models.CASCADE, null=True)
    entrydate=models.DateField()
    entrytime=models.TimeField(default='00:00')
    exitdate=models.DateField()
    exittime=models.TimeField(default='00:00')
    
VALIDITY_CHOICES = [
        ('1 MONTH', '1 MONTH'),
        ('2 MONTH', '2 MONTH'),
        ('3 MONTH', '3 MONTH'),
        ('4 MONTH', '4 MONTH'),
        ('5 MONTH', '5 MONTH'),
        ('6 MONTH', '6 MONTH'),
        ('7 MONTH', '7 MONTH'),
        ('8 MONTH', '8 MONTH'),
        ('9 MONTH', '9 MONTH'),
        ('10 MONTH', '10 MONTH'),
        ('11 MONTH', '11 MONTH'),
        ('12 MONTH', '12 MONTH'),
    ]

class Subscription(models.Model):  
    sub_type = models.CharField(max_length=40, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    validity = models.CharField(max_length=40, choices=VALIDITY_CHOICES, blank=True, null=True) 
    features = models.CharField(max_length=255 , default='',) 

    def str(self):
        return f"{self.sub_type} Subscription"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    district = models.CharField(max_length=15, blank=True, null=True)
    addressline1 = models.CharField(max_length=15, blank=True, null=True)
    addressline2 = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    profilepic = models.ImageField(blank=True, null=True, upload_to='pics')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.user:
            return self.user.first_name
        else:
            return "UserProfile with no associated user"

class RazorpayPayment(models.Model):
    razorpay_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Razorpay ID: {self.razorpay_id}, Amount: {self.amount}'

class ProcessedImage(models.Model):
    image_data = models.TextField()
    processed_text = models.TextField()
    cam2 = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.TextField(default='')
    intime = models.DateTimeField(null=True, blank=True)
    outtime = models.DateTimeField(null=True, blank=True)
    
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subscription.sub_type} Subscription"
    
from django.db import models
from django.contrib.auth.models import User

class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} at {self.created_at}"

class EventBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_bookings')
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    intime = models.TimeField(null=True, blank=True)
    outtime = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')