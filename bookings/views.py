from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views.generic import FormView, DetailView, ListView, UpdateView

from bookings.choices import ReservationStatusChoices
from bookings.forms import BookingCreateForm, BookingEditForm
from bookings.models import Booking


# Create your views here.
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


class BookingDetailsView(PermissionRequiredMixin, DetailView):
    template_name = 'bookings/booking-details.html'
    model = Booking
    permission_required = "bookings.can_manage_bookings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        return context


@permission_required('bookings.can_manage_bookings')
def confirm_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, status=ReservationStatusChoices.PENDING)
    booking.status = ReservationStatusChoices.CONFIRMED
    booking.confirmed_by = request.user
    booking.save()

    status = request.GET.get('status', 'pending')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('bookings')}?status={status}&page={page}")


@permission_required('bookings.can_manage_bookings')
def reject_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, status=ReservationStatusChoices.PENDING)
    booking.status = ReservationStatusChoices.REJECTED
    booking.confirmed_by = request.user
    booking.save()

    status = request.GET.get('status', 'pending')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('bookings')}?status={status}&page={page}")


class BookingsListView(PermissionRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings.html'
    context_object_name = 'bookings'
    paginate_by = 3
    permission_required = "bookings.can_manage_bookings"

    def get_queryset(self):
        status = self.request.GET.get('status', ReservationStatusChoices.PENDING)
        return Booking.objects.filter(status=status, date__gte=now().date()).order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        context['statuses'] = ReservationStatusChoices.choices
        context['selected_status'] = self.request.GET.get('status', ReservationStatusChoices.PENDING)
        return context


class FutureBookingsClientView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings-client.html'
    context_object_name = 'bookings'
    paginate_by = 3

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            date__gte=now().date()
        ).order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATUS'] = ReservationStatusChoices
        return context


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = ReservationStatusChoices.CANCELLED
    booking.save()
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('client-bookings')}?page={page}#booking-{pk}")


class BookingEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingEditForm
    template_name = 'bookings/edit-booking.html'

    def get_success_url(self):
        return reverse_lazy('client-bookings')

    def test_func(self):
        return self.request.user == self.get_object().user and self.get_object().status == ReservationStatusChoices.PENDING
