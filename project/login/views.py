from django.shortcuts import render
from models import sqlserverconn
from datetime import datetime
import pyodbc

# Create your views here.
def connsql(request):
    conn=pyodbc.connect('Driver={sqlserver};Server=ARCHANGEL\SQLEXPRESS;Database=parking;Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from vehicle_table")
def login_page(request):
    page_name="login page is here"
    return render(request, 'login_page.html', {'date':datetime.now()})