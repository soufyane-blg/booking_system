from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from  .models import Booking, Service
# Create your views here.

def booking_list(request):
    bookings = Booking.objects.all()
    return render (request, 'bookings/booking_list.html',
         {'bookings' : bookings})

def booking_create(request):
    services = Service.objects.all()

    if request.method == 'POST':
        user = request.user
        service_id = request.POST['service']
        date = request.POST['date']
        time = request.POST['time']

        service = Service.objects.get(id=service_id)

        Booking.objects.create(
            user=user,
            service=service,
            date=date,
            time=time
        )
        return redirect('booking_list')

    return render(request, 'bookings/booking_create.html', 
                  {'services' : services})
    

def booking_details(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'bookings/booking_details.html', {'booking': booking})

def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)
    
    if request.user != booking.user:
        return redirect('booking_list')

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted succesfully")
        return redirect('booking_list')

    return render(request, 'bookings/booking_confirm_delete.html', {
        'booking': booking
    })

def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id)
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
