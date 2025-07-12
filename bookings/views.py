from django.shortcuts import render

# Create your views here.


def book_a_table(request):
    return render(request, 'bookings/book-a-table.html')


def booking_details(request):
    return render(request, 'bookings/booking-details.html')


def bookings(request):
    return render(request, 'bookings/bookings.html')


def client_bookings(request):
    return render(request, 'bookings/bookings-client.html')


def edit_booking(request):
    return render(request, 'bookings/edit-booking.html')