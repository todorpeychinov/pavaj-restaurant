from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'common/index.html')


def about(request):
    return render(request, 'common/about.html')


def contact(request):
    return render(request, 'common/contact.html')


def confirmation_page(request):
    return render(request, 'common/delete-confirmation-page.html')


def main_menu(request):
    return render(request, 'common/main-menu.html')


def seasonal_menu(request):
    return render(request, 'common/seasonal-menu.html')


def wine_list(request):
    return render(request, 'common/wine-list.html')