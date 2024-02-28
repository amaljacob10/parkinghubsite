from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.contrib import messages
from .forms import BookingForm,rasperryForm
from .models import service_station,Booking,rasperry,UserProfile,EventBooking
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .models import Slot
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from .models import UserProfile 
from django.shortcuts import render
from .utils import calculate_parking_cost  # Import your cost calculation function

from django.shortcuts import render, redirect
from .forms import BookingForm  # Import your BookingForm here
import datetime

from datetime import datetime

from datetime import datetime
from django.http import HttpResponse
# from xhtml2pdf import pisa


from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .models import RazorpayPayment
from django.shortcuts import render
from django.http import JsonResponse
# import cv2
from google.cloud import vision
from .models import ProcessedImage
from .forms import ProcessedImageForm
from django.conf import settings
import base64  
from django.http import JsonResponse
import base64
from google.cloud import vision_v1
from django.conf import settings
from django.http import JsonResponse
from .models import ProcessedImage  # Assuming you have a model for storing processed images
from collections import defaultdict


razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# def index(request):
#     # Retrieve all parks
#     parks = service_station.objects.all()

#     # Retrieve all subscription data
#     subscriptions = Subscription.objects.all()
#     data = service_station.objects.all()
#     # Extract features from each subscription and create a list of tuples
#     subscription_features = [
#         (sub.sub_type, [feature.strip() for feature in sub.features.split(',')]) if sub.features else (sub.sub_type, [])
#         for sub in subscriptions
#     ]

#     # Flatten the features list to make it a single list
#     flattened_features = [feature for _, features in subscription_features for feature in features]

#     # Prepare the context data
#     context = {'parks': parks, 'subscriptions': subscriptions,'data': data, 'subscription_features': subscription_features, 'flattened_features': flattened_features}

#     return render(request, 'index.html', context)

from decimal import Decimal  # Import Decimal for accurate currency handling

from decimal import Decimal
from django.shortcuts import render
from django.conf import settings
from .models import service_station, Subscription
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages


def index(request):
    # Retrieve all parks
    parks = service_station.objects.all()

    # Retrieve all subscription data
    subscriptions = Subscription.objects.all()
    data = service_station.objects.all()
    # Extract features from each subscription and create a list of tuples
    subscription_features = [
        (sub.sub_type, [feature.strip() for feature in sub.features.split(',')]) if sub.features else (sub.sub_type, [])
        for sub in subscriptions
    ]

    # Flatten the features list to make it a single list
    flattened_features = [feature for _, features in subscription_features for feature in features]

    # Razorpay payment details
    currency = 'INR'
    amount = 100000  # Rs. 200
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler_subscription/'

    # Add Razorpay payment details to the context
    context = {
        'parks': parks,
        'subscriptions': subscriptions,
        'data': data,
        'subscription_features': subscription_features,
        'flattened_features': flattened_features,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url,
    }
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        print("fftufutfut")
        if feedback_form.is_valid():
            # Save the feedback associated with the currently logged-in user
            feedback = feedback_form.save(commit=False)
            feedback.user = request.user  # Assumes users are authenticated
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('index')  # Redirect to the same page after submission

    else:
        feedback_form = FeedbackForm()

        
    context['feedback_form'] = feedback_form
    return render(request, 'index.html', context)

from django.shortcuts import render
from .models import UserFeedback

def admin_feedback(request):
    # Retrieve all feedbacks
    feedbacks = UserFeedback.objects.all()

    # Pass the feedbacks to the template
    return render(request, 'admin_feedback.html', {'feedbacks': feedbacks})




def showData(request):
    data=Booking.objects.all()
    return render(request,"data.html",{'datas':data})
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpass')
        if confirmpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, 'reg.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, 'reg.html')
            else:
                user_reg = User.objects.create_user(username=username, email=email,password=password)
                user = request.user
                user_profile = UserProfile(user=user)   
                user_profile.save()
                user_reg.save()
                
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'reg.html')
    return render(request, 'reg.html')

from django.contrib.auth.models import User
from .models import UserProfile  # Make sure to import UserProfile

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        confirmpassword = request.POST.get('confirmpass')
        
        if confirmpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, 'reg.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, 'reg.html')
            else:
                # Create a new User instance
                user_reg = User.objects.create_user(username=username, email=email, password=password)

                # Create a UserProfile instance associated with the new User
                user_profile = UserProfile(user=user_reg)  # Add any other UserProfile fields here
                user_profile.save()

                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'reg.html')
    return render(request, 'reg.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            user=request.user
            user_email=user.email
            print(user_email)
            subject = 'BOOKING SUCCESSFUL'
            message = 'Your booking is succesful.'
            from_email = settings.EMAIL_HOST_USER  # Your sender email address
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request) 
    return redirect('login')

# def book(request,book_id):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'confirm.html')
#     else:
#         form = BookingForm()

#     return render(request, 'booking.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.http import HttpResponse
from datetime import datetime

# ...

from datetime import datetime

from django.shortcuts import redirect  # Import redirect function
from django.shortcuts import redirect
from django.urls import reverse  # Import reverse function

# ...

from django.urls import reverse

# ...

def book(request, book_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking data into the database
            booking = form.save(commit=False)
            booking.slot_id = book_id
            booking.name = request.user.username
            booking.status = 'Pending'
            booking.save()

            # Convert date and time components to datetime object
            entry_datetime = datetime.combine(booking.indate, booking.intime)
            exit_datetime = datetime.combine(booking.outdate, booking.outtime)

            # Calculate parking cost using datetime objects
            cost = calculate_cost(entry_datetime, exit_datetime)

            if cost is None:
                # Generate the URL for the payment view with the cost as a parameter
                cost = 123
            cost=int(cost)
# Generate the URL with the 'costdata' parameter
                # payment_url = reverse('payment', kwargs={'costdata': cost})

# Redirect to the generated URL
            url = f'http://127.0.0.1:8000/parkingcost/{cost}'
            return redirect(url)

                # Redirect the user to the payment URL
                
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form,'slot':book_id})


from django.shortcuts import render, redirect
from .models import EventBooking
from datetime import datetime

def book_event(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        intime = request.POST.get('intime')
        outtime = request.POST.get('outtime')

        # Convert date and time strings to datetime objects

        # Save the event booking data into the database
        event_booking = EventBooking.objects.create(
            user=request.user,
            event_name=event_name,
            date=date,
            intime=intime,
            outtime=outtime,
            # event_id=event_id
        )

        # Redirect or perform additional logic
        return bill_generate(request,intime,outtime,double=True)
    return render(request, 'book_event.html')

    



# def mybooking(request):
#     user_id = request.user.id
#     stdata = Booking.objects.filter(head__id=user_id)
#     return render(request, "mybookings.html", {'stdata': stdata})

def mybooking(request):
    expired()
    user_id = request.user.username
    stdata = Booking.objects.filter(name=user_id,hidden=False)
    from django.shortcuts import render
    from .models import EventBooking
        # Check if the user is logged in
    if request.user.is_authenticated:
        # Retrieve all event bookings associated with the logged-in user
        event_bookings = EventBooking.objects.filter(user=request.user)
    return render(request, "mybookings.html", {'stdata': stdata,'eventbooking':event_bookings})

from django.shortcuts import get_object_or_404

def delete_booking(request, stid2):
    print("Entered")
    item_to_delete =Booking.objects.get(id=stid2)

    
    item_to_delete.hidden=True

        
    item_to_delete.save()
    
    

    
    return redirect("mybooking")


# def add_slot(request):
#     if request.method == 'POST':
#         form = AddSlot(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')  # Redirect to your success view
#         else:
#             print(form.errors)  # Print errors for debugging purposes
#     else:
#         form = AddSlot()

#     return render(request, 'add_slot.html', {'form': form})


def addslot(request):
    print("function")
    if request.method == 'POST':
        stname = request.POST.get('stname')        
        place = request.POST.get('loc')        
        photo = request.FILES.get('photo')
        print(photo)
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        maxslot = request.POST.get('max_slot')
        price = request.POST.get('price')

        post = service_station(
            stname=stname,
            place=place,
            photo=photo,
            latitude=latitude,
            longitude=longitude,
            maxslot=maxslot,
            price=price
            
        )
        post.save()
        return redirect('index')
    return render(request, "addslot.html")



def delete(request, delete_id):
    dele=service_station.objects.get(id=delete_id)
    dele.delete()
    return redirect('/')

def update(request, update_id):
    upd = service_station.objects.get(id=update_id)

    if request.method == 'POST':
        # Your logic to update the model instance based on the posted data
        upd.stname = request.POST.get('stname')  # Replace 'stname' with actual field names
        upd.place = request.POST.get('loc')  # Replace 'loc' with actual field names
        upd.maxslot = request.POST.get('max_slot')  # Replace 'max_slot' with actual field names
        upd.latitude = request.POST.get('latitude')  # Replace 'latitude' with actual field names
        upd.longitude = request.POST.get('longitude')  # Replace 'longitude' with actual field names
        upd.price = request.POST.get('price')  # Replace 'price' with actual field names
        upd.photo = request.FILES.get('photo')
        # Save the updated instance
        upd.save()

        return redirect('/')

    return render(request, 'update.html', {'upd': upd})

def add_rasperry(request):
    if request.method == 'POST':
        form = rasperryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_rasperry')
    else:
        form = rasperryForm()
    return render(request, 'add_rasperry.html', {'form': form})

def view_rasperry(request):
    rasperry_data = rasperry.objects.all()
    return render(request, 'view_rasperry.html', {'rasperry_data': rasperry_data})

def rasperry_list(request):
    rasperry_data = rasperry.objects.all()
    return render(request, 'view_rasperry.html', {'rasperry_data': rasperry_data})


@login_required
def slot(request, park_id):

    slot_1_bookings = Booking.objects.filter(slot_id=1,hidden=False)
    slot_2_bookings = Booking.objects.filter(slot_id=2,hidden=False)
    slot_3_bookings = Booking.objects.filter(slot_id=3,hidden=False)
    slot_4_bookings = Booking.objects.filter(slot_id=4,hidden=False)
    slot_5_bookings = Booking.objects.filter(slot_id=5,hidden=False)
    slot_6_bookings = Booking.objects.filter(slot_id=6,hidden=False)
    slot_7_bookings = Booking.objects.filter(slot_id=7,hidden=False)
    slot_8_bookings = Booking.objects.filter(slot_id=8,hidden=False)
    slot_9_bookings = Booking.objects.filter(slot_id=9,hidden=False)
    
    if request.method == 'POST':
        # Get the selected park
        user = request.user
        park = service_station.objects.get(pk=park_id)
        name = user.username  # Change this according to your User model
        # Retrieve booking details from the form
        indate = request.POST['indate']
        intime = request.POST['intime']
        outdate = request.POST['outdate']
        outtime = request.POST['outtime']

        # Create a new booking
        booking = Booking(
            name=name,
            park=park,
            indate=indate,
            intime=intime,
            outdate=outdate,
            outtime=outtime,
            slot_id=1  # Adjust the slot ID accordingly
        )
        booking.save()

        return redirect('list_parks')  # Replace 'list_parks' with the appropriate URL name

    # Render the booking form
    park = service_station.objects.get(pk=park_id)
    return render(request, 'slot.html', {'park': park, 'book1': slot_1_bookings, 'book2': slot_2_bookings, 'book3': slot_3_bookings, 'book4': slot_4_bookings, 'book5': slot_5_bookings, 'book6': slot_6_bookings, 'book7': slot_7_bookings, 'book8': slot_8_bookings, 'book9': slot_9_bookings})

def expired():
    # Check for expired bookings and make slots available
    now = datetime.now()
    expired_bookings = Booking.objects.filter(outtime__lt=now)

    for booking in expired_bookings:
        # Update the slot status here
        booking.status = 'Pending'
        booking.save()

        # Delete the expired booking
        booking.delete()
# def slot(request, park_id):
#     park = get_object_or_404(Park, pk=park_id)

#     if request.method == 'POST':
#         # Retrieve booking details from the form
#         name = request.POST['name']
#         phno = request.POST['phno']
#         indate = request.POST['indate']
#         intime = request.POST['intime']
#         outdate = request.POST['outdate']
#         outtime = request.POST['outtime']

#         # Create a new booking
#         booking = Booking(
#             name=name,
#             park=park,
#             phno=phno,
#             indate=indate,
#             intime=intime,
#             outdate=outdate,
#             outtime=outtime
#         )
#         booking.save()

#         return redirect('list_parks')  # Replace 'list_parks' with the appropriate URL name

#     # Retrieve bookings for the slot
#     slot_1_bookings = Booking.objects.filter(park=park, slot_id=1)
    

#     # Extract the outtime from the first booking (assuming there is only one booking for slot 1)
#     outtime = slot_1_bookings.first().outtime if slot_1_bookings.exists() else None

#     return render(request, 'slot.html', {'park': park, 'book': slot_1_bookings, 'outtime': outtime})

def editprofile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Update user profile fields
        if 'profilepic' in request.FILES:
            user_profile.profilepic = request.FILES['profilepic']


        user_profile.save()

        return redirect('viewprofile')

    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'editprofile.html', context)



def profile(request):
    # user_profile1 = request.user
    # userid = user_profile1.id
    user_profile1 = None
    user_profile1 = request.user
    userid = user_profile1.id
    error_message=''
    show=''
    check = UserProfile.objects.filter(user_id=userid).exists()
    if check:
        user_profile = UserProfile.objects.get(user_id=userid)
    else:
        user_profile=None
        
    
    print(user_profile.addressline2)

    if request.method == 'POST':
        # Update user fields
        if check:
            user_profile.first_name = request.POST.get('first_name')
            user_profile.last_name = request.POST.get('last_name')
            user_profile.save()

            # Update user profile fields
            pic=request.FILES.get('profilepic')
            if pic==None:
                user_profile.profilepic = user_profile.profilepic
            else:
                user_profile.profilepic=pic
            print("image is : ",user_profile.profilepic)

            user_profile.country = request.POST.get('country')
            user_profile.state = request.POST.get('state')
            user_profile.city = request.POST.get('city')
            user_profile.district = request.POST.get('district')
            user_profile.aphone_no = request.POST.get('aphone_no')
            user_profile.phone = request.POST.get('phone_no')
            user_profile.addressline1 = request.POST.get('addressline1')
            user_profile.addressline2 = request.POST.get('addressline2')
            user_profile.pin_code = request.POST.get('pin_code')
            user_profile.save()
            error_message = "Profile Updated"
        else:
            user = UserProfile(
                phone_no=request.POST.get('phone_no'),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                city=request.POST.get('city'),
                district=request.POST.get('district'),
                aphone_no=request.POST.get('aphone_no'),
                addressline1=request.POST.get('addressline1'),
                addressline2=request.POST.get('addressline2'),
                pin_code=request.POST.get('pin_code'),
                user_id=userid
            )
            error_message = "Profile Updated"
            user.save()
        context = {
        'user': user_profile1,
        'user_profile': user_profile,
        'error_message': error_message,
        'show': show
    }
        return render(request, 'profile.html', context)  

    context = {
        'user': user_profile1,
        'user_profile': user_profile,
        'error_message': error_message,
        'show': show
    }
    return render(request, 'profile.html', context)  
# def bookstation(request, station_id):
#     user = request.user
#     user_id = user.id
#     error_message = ''
#     data = station.objects.get(id=station_id)

#     print(data.available)
#     if data.available is None:
#         data.available = data.maxslot
#     data.available = data.available

#     # Retrieve existing booked slot numbers for the station
#     booked_slot_numbers = booknow.objects.filter(
#         station_id=data).values_list('slotnumber', flat=True)
#     # Generate a list of available slot numbers
#     available_slot_numbers = [num for num in range(
#         1, data.maxslot + 1) if num not in booked_slot_numbers]

#     if request.method == 'POST':
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         slotnumber = request.POST.get('your_slot')

#         existing_booking = booknow.objects.filter(
#             date=date, time=time, slotnumber=slotnumber, station_id_id=station_id).first()

#         if existing_booking:
#             error_message = "Slot already booked"
#             return render(request, "booknow.html", {'error': error_message})

#         post = booknow(
#             name=user,  # Assuming 'name' and 'email' are ForeignKey fields in 'booknow'
#             email=user,
#             date=date,
#             time=time,
#             slotnumber=slotnumber,
#             stname=data.stname,
#             place=data.place,
#             price=data.price,
#             ownername=data.ownername,
#             station_id_id=data.id
#         )

#         # No need to decrement data.available here
#         data.available -= 1
#         print(data.available)
#         data.save()
#         post.save()

#         return redirect('payment')

#     return render(request, "booknow.html", {'available_slot_numbers': available_slot_numbers})

# def calculate_parking_cost(entry_time_str, exit_time_str):
#     # Define a format that includes hours and minutes only (without seconds)
#     format_without_seconds = '%H:%M'

#     try:
#         # Try to parse the time strings with the format including seconds
#         entry_time = datetime.strptime(entry_time_str, format_without_seconds)
#         exit_time = datetime.strptime(exit_time_str, format_without_seconds)
#     except ValueError:
#         # If parsing with seconds fails, try without seconds
#         entry_time = datetime.strptime(entry_time_str, format_without_seconds)
#         exit_time = datetime.strptime(exit_time_str, format_without_seconds)

#     if entry_time is None or exit_time is None:
#         # Handle the case where either entry_time or exit_time is None
#         return 0  # You can choose a default cost or raise an error

#     duration = (exit_time - entry_time).total_seconds() / 3600.0
#     cost = duration * 5  # $5 per hour (replace with your actual calculation)
#     cost= int(cost)
#     return cost

def paymentSubscription(request,costdata):
    # Retrieve the costdata parameter from the request's GET parameters
    print("sub")
    print(costdata)
    # Check if costdata is not None and is a valid number (you may need to adjust this validation)
    if costdata:
        cost = float(costdata) 
        cost=int(cost)# Convert it to an integer
        currency = 'INR'
        amount = cost * 100

        # Initialize Razorpay client
        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

        # Get the order ID
        razorpay_order_id = razorpay_order['id']
        callback_url = '/paymenthandler/'

        # Prepare context data to pass to the frontend
        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency,
            'callback_url': callback_url,
            'amount': amount / 100,
        }
        print(amount)
        RazorpayPayment.objects.create(
            razorpay_id=razorpay_order_id,
            amount=amount
        )   
        sub=UserSubscription(
            payment_amount=amount,
            payment_date=timezone.now(),
            subscription_id=1,
            user_id=request.user.id
        )
        print(123,sub)
        print(sub)
        sub.save()
        print("Subscribed")
        return redirect('http://127.0.0.1:8000/')
    else:
        # Handle the case where costdata is invalid or missing
        return HttpResponseBadRequest("Invalid or missing costdata parameter")
# Rest of your code for calculate_cost function and other views

def payment(request,costdata):
    # Retrieve the costdata parameter from the request's GET parameters
    

    # Check if costdata is not None and is a valid number (you may need to adjust this validation)
    if costdata:
        cost = float(costdata) 
        cost=int(cost)# Convert it to an integer
        currency = 'INR'
        amount = cost * 100

        # Initialize Razorpay client
        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

        # Get the order ID
        razorpay_order_id = razorpay_order['id']
        callback_url = '/paymenthandler/'

        # Prepare context data to pass to the frontend
        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency,
            'callback_url': callback_url,
            'amount': amount / 100,
        }
        print(context)
        RazorpayPayment.objects.create(
            razorpay_id=razorpay_order_id,
            amount=amount
        )
        return render(request, 'parkingcost.html', context=context)
    else:
        # Handle the case where costdata is invalid or missing
        return HttpResponseBadRequest("Invalid or missing costdata parameter")

@csrf_exempt
def paymenthandler(request):

    user=request.user
    user_email=user.email
    # only accept POST request.
    if request.method == "POST":
           
            # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        subject = 'BOOKING SUCCESSFUL'
        message = 'Your booking is succesful.'
        from_email = settings.EMAIL_HOST_USER  # Your sender email address
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)
        
        
        # verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(
            params_dict)
        if result is not None:
            amount = 20000  # Rs. 200
            a=RazorpayPayment.objects.filter( razorpay_id=razorpay_order_id)
                # capture the payemt
            razorpay_client.payment.capture(payment_id, int(a[0].amount))

            feedback_form = FeedbackForm()  # Create an instance of the FeedbackForm
            return render(request, 'confirm.html', {'feedback_form': feedback_form})
            # render success page on successful caputre of payment
            


            # if there is an error while capturing payment.

    
    
    
    
    
    
    
    
    
    
    
    

from datetime import datetime

def calculate_cost(entry_datetime, exit_datetime):
    # Calculate the duration in hours
    duration = (exit_datetime - entry_datetime).total_seconds() / 3600.0

    # Calculate the cost at a rate of 30 Rs/hr
    rate_per_hour = 30
    cost = duration * rate_per_hour

    return cost

def bill_generate(request,entry,exit,double=False):
    if not double:
        entry_datetime = datetime.strptime(entry, '%Y-%m-%d %H:%M:%S.%f+00:00')
        exit_datetime = datetime.strptime(exit, '%Y-%m-%d %H:%M:%S.%f+00:00')
    else:
        entry_datetime_str = f'1970-01-01 {entry}'  # Using a dummy date, you can adjust this as needed
        entry_datetime = datetime.strptime(entry_datetime_str, '%Y-%m-%d %H:%M')
        exit_datetime_str = f'1970-01-01 {exit}'  # Using a dummy date, you can adjust this as needed
        exit_datetime = datetime.strptime(exit_datetime_str, '%Y-%m-%d %H:%M')
    # Now you have two separate datetime objects: entry_datetime and exit_datetime
    print(entry_datetime,exit_datetime)
    val = calculate_cost(entry_datetime, exit_datetime)  # Assuming calculate_cost takes two datetime objects
    val=int(val)
    if double:
        val=val*8
        return payment(request,val) 
    return render(request,'bill.html',{'amount':val})
   
def capture_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        
        # Process the captured image and send it to Google Cloud Vision API
        process_and_send_to_vision_api(image_data)
        return JsonResponse({'status': 'Image processing started'})
    # render success page on successful caputre of payment
    
    return JsonResponse({'error': 'Invalid request method'})
# def cap (req):


   

def process_and_send_to_vision_api(image_data):
   
    # google_api_key = settings.GOOGLE_CLOUD_API_KEY

    # Convert the base64 image data to an image file
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image_filename = 'captured_image.png'
    with open(image_filename, 'wb') as image_file:
        image_file.write(image_bytes)

    # Send the image to Google Cloud Vision API for text detection
    client = vision_v1.ImageAnnotatorClient()
    with open(image_filename, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.Image(content=content)
    response = client.text_detection(image=image)
    
    # Extract the detected text
    texts = response.text_annotations
    detected_text = texts[0].description if texts else ''

    return detected_text

# Remove one of the process_image functions if not needed
from datetime import datetime
from django.shortcuts import render
from .models import ProcessedImage

def process_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        print("Received image data:", image_data)
        
        # Get the current timestamp as the 'intime'
        intime = datetime.now()
        
        # Process the captured image and send it to Google Cloud Vision API
        detected_text = process_and_send_to_vision_api(image_data)

        # Create an instance of your model and save it with 'intime'
        processed_image = ProcessedImage(
            image_data=image_data,
            processed_text=detected_text,
            intime=intime  # Store the 'intime'
        )
        processed_image.save()

        # Return the detected text in the response
        return render(request, 'result.html', {'result': detected_text})
    
    return render(request, 'capture_image.html')

def process_image2(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        
        # Get the current timestamp as the 'intime'
        outtime = datetime.now()
        
        # Process the captured image and send it to Google Cloud Vision API
        detected_text = process_and_send_to_vision_api(image_data)

        # Create an instance of your model and save it with 'intime'
        processed_image = ProcessedImage.objects.filter(processed_text__iexact=detected_text).order_by('-created_at').first()
        print(processed_image)
        if processed_image is None:
            detected_text="UNKNOWN VEHICLE"
        else:
            processed_image.cam2=detected_text
            processed_image.outtime=outtime
            processed_image.save()

        # Return the detected text in the response
        return render(request, 'result.html', {'result': detected_text})
    
    return render(request, 'capture_image2.html')


# def expired():
#     # Check for expired bookings and make slots available
#     now = datetime.now()
#     expired_bookings = booking.objects.filter(outtime__lt=now)

#     for booking in expired_bookings:
#         station1 = Booking.station_id
#         station1.status = 'Pending'  # Mark the station as unavailable
#         station1.save()

#         # Delete the expired booking
#         booking.delete()

# def print_as_pdf(request, booking_id):
    # Use the booking_id parameter to filter the Booking object
    data = Booking.objects.filter(id=booking_id)

    # Ensure that a booking with the specified ID exists
    if not data.exists():
        # Handle the case where the booking does not exist, e.g., return an error response or redirect
        return HttpResponse("Booking not found")

    # Retrieve the cost based on the booking
    cost = RazorpayPayment.objects.get(booking_id_id=booking_id)
    cost = cost.amount
    cost = cost / 100

    total_cost = int(cost)
    template_path = 'template\receipt.html'  # Update with the actual path to your HTML template.

    # Context data to pass to the template
    context = {'data': data, 'total_cost': total_cost}

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{booking_id}.pdf"'

    # Render the HTML template to PDF
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
        rendered_html = render(request, 'printpdf.html', context)

        # Create a PDF using pisa
        pisa_status = pisa.CreatePDF(
            rendered_html.content,
            dest=response,
            link_callback=None  # Optional: Handle external links
        )
    return response
def show_activity(request):
    # Query the ProcessedImage model to get the data
    processed_images = ProcessedImage.objects.all()

    # Pass the data to the template
    return render(request, 'show_activity.html', {'processed_images': processed_images})
# views.py

import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

def generate_qr_code(request, cost):
    print("Entered")
    # Generate the QR code image with the cost
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Cost: {cost}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to BytesIO for HttpResponse
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')

    response = HttpResponse(content_type='image/png')
    response.write(img_bytes.getvalue())
    print(response)
    return response
# views.py

from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscription

def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            sub_type = form.cleaned_data['sub_type']
            price = form.cleaned_data['price']
            validity = form.cleaned_data['validity']
            features_list = form.cleaned_data['features'].split(',')
            features_csv = ','.join(features_list)
            

            if Subscription.objects.filter(
                sub_type=sub_type,
                price=price,
                validity=validity,
                features=features_csv
            ).exists():
                
                form.add_error(None, "A subscription with the same data already exists.")
            else:
               
                subscription = form.save(commit=False)
                subscription.features = features_csv
                subscription.save()
                return redirect('/')
    else:
        form = SubscriptionForm()
    
    return render(request, 'subscription.html', {'form': form})




from .models import UserSubscription, Subscription

#payment
@csrf_exempt
def paymenthandler_subscription(request):
    if request.method == "POST":
        try:
            # Get the required parameters from the POST request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            subscription_type = request.POST.get('subscription_type', '')  # Added line to retrieve subscription type

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # Verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result is not None:
                amount = int(total_subscription_amount_float * 100)  # Convert to paisa

                try:
                    # Capture the payment
                    razorpay_client.payment.capture(payment_id, amount)

                    # Get the Subscription instance based on the subscription type
                    subscription = get_object_or_404(Subscription, sub_type=subscription_type)

                    # Create a UserSubscription instance
                    user_subscription = UserSubscription.objects.create(
                        user=request.user,
                        subscription=subscription,
                        payment_id=payment_id,
                        # Add other fields as needed
                    )

                    # Render success page on successful capture of payment
                    return render(request, 'paymentsuccess.html')
                except Exception as e:
                    # Handle payment capture errors
                    return render(request, 'paymentfail.html', {'error_message': str(e)})
            else:
                # If signature verification fails.
                return render(request, 'paymentfail.html', {'error_message': 'Signature verification failed'})
        except Exception as e:
            # If we don't find the required parameters in POST data.
            return HttpResponseBadRequest()
    else:
        # If other than POST request is made.
        return HttpResponseBadRequest()