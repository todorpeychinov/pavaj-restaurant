from django.urls import path, include

from inquiries import views

urlpatterns = [
    path('inquiries/', views.InquiriesListView.as_view(), name='inquiries-list'),
    path('sent-inquiry/', views.InquiryCreateView.as_view(), name='sent-inquiry'),
    path('thank-you/', views.InquiryThankYouView.as_view(), name='thank-you'),
    path('<int:pk>/', include([
        path('answer-inquiry/', views.InquiryAnswerView.as_view(), name='answer-inquiry'),
        path('inquiry-details/', views.InquiryDetailView.as_view(), name='inquiry-details'),
    ]))
]