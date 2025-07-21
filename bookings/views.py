from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from bookings.forms import BookingCreateForm


# Create your views here.


def book_a_table(request):
    return render(request, 'bookings/book-a-table.html')


class BookATableView(LoginRequiredMixin, FormView):
    template_name = "bookings/book-a-table.html"
    form_class = BookingCreateForm
    success_url = reverse_lazy('client-bookings')

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        if user.is_authenticated:
            full_name = f"{user.first_name} {user.last_name}".strip()
            initial['full_name'] = full_name if full_name else ''
            initial['email'] = user.email
            if hasattr(user, 'profile'):
                initial['phone_number'] = user.profile.phone_number or ''
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def booking_details(request):
    return render(request, 'bookings/booking-details.html')


def bookings(request):
    return render(request, 'bookings/bookings.html')


def client_bookings(request):
    return render(request, 'bookings/bookings-client.html')


def edit_booking(request):
    return render(request, 'bookings/edit-booking.html')
