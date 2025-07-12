from django.shortcuts import render

# Create your views here.


def answer_inquiry(request):
    return render(request, 'inquiries/answer-inquiry-page.html')


def inquiries_list(request):
    return render(request, 'inquiries/inquiries-page.html')


def inquiry_details(request):
    return render(request, 'inquiries/inquiry-details.html')


def sent_inquiry(request):
    return render(request, 'inquiries/sent-inquiry.html')