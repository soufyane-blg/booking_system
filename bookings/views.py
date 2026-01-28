from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from  .models import Booking, Service
from .forms import BookingForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user : 
            login(request, user)
            return redirect ('booking_list')
        else:
            return render (request, 'auth/login.httml', {'error' : 'invalid username or password'} )

    return render (request, 'auth/login.html')    


def logout_view (request):
    logout(request)

    return redirect('login')

def register(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)

        if form.is_valid (): 
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render (request, 'auth/register.html', {'form' : form } )

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render (request, 'bookings/booking_list.html',
         {'bookings' : bookings})


@login_required
def booking_create(request):
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
            
    else:
          form = BookingForm()  
        
    return render(request, 'bookings/booking_create.html', 
                  {'form' : form})
    
@login_required
def booking_details(request, id):
    booking = get_object_or_404(Booking, id=id, user= request.user)
    return render(request, 'bookings/booking_details.html', {'booking': booking})

@login_required
def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id, user= request.user)
    
    if request.user != booking.user:
        return redirect('booking_list')

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted succesfully")
        return redirect('booking_list')

    return render(request, 'bookings/booking_confirm_delete.html', {
        'booking': booking
    })
@login_required
def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id, user= request.user)
    if request.user != booking.user:
        return redirect('booking_list')

    services = Service.objects.all()

    if request.method == 'POST':
        service_id = request.POST['service']
        date = request.POST['date']
        time = request.POST['time']

        service = Service.objects.get(id=service_id)

        booking.service= service
        booking.date= date
        booking.time= time
        booking.save() 

        messages.success(request, "Booking updated succesfully")
        return redirect('booking_list')

    return render(request, 'bookings/booking_update.html', {
    'booking': booking,
    'services': services
    })
    
    


def test(request):
    return render(request, 'test.html')
