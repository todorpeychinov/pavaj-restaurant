from django.urls import path, include

from bookings import views

urlpatterns = [
    path('book-table/', views.BookATableView.as_view(), name='book-table'),
    path('clients-bookings/', views.BookingsListView.as_view(), name='bookings'),
    path('bookings/', views.FutureBookingsClientView.as_view(), name='client-bookings'),
    path('<int:pk>/', include([
        path('booking-details/', views.BookingDetailsView.as_view(), name='booking-details'),
        path('confirm-booking/', views.confirm_booking, name='confirm-booking'),
        path('reject-booking/', views.reject_booking, name='reject-booking'),
        path('edit-booking/', views.BookingEditView.as_view(), name='edit-booking'),
        path('cancel-booking/', views.cancel_booking, name='cancel-booking'),
    ]))

]
