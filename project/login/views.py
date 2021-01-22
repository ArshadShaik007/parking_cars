from django.shortcuts import render
from datetime import datetime

# Create your views here.
def login_page(request):
    page_name="login page is here"
    return render(request, 'login_page.html', {'date':datetime.now()})