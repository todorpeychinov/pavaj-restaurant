from django.urls import path

from inquiries import views

urlpatterns = [
    path('answer-inquiry/', views.answer_inquiry, name='answer-inquiry'),
    path('inquiries/', views.inquiries_list, name='inquiries-list'),
    path('inquiry-details/', views.inquiry_details, name='inquiry-details'),
    path('sent-inquiry/', views.sent_inquiry, name='sent-inquiry'),
]