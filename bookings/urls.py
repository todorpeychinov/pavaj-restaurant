from django.urls import path

from bookings import views

urlpatterns = [
    path('book-table/', views.book_a_table, name='book-table'),
    path('booking-details/', views.booking_details, name='booking-details'),
    path('bookings/', views.bookings, name='bookings'),
    path('client-bookings/', views.client_bookings, name='client-bookings'),
    path('edit-booking/', views.edit_booking, name='edit_booking'),

]
