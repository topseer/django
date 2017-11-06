# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import login
import pyodbc 
import pandas.io.sql as sql
from django import forms
import datetime   
from .forms import NameForm
from .forms import PeriodFilter
from datetime import date 
from django.shortcuts import redirect

from . import numOfLeads
from . import datatrend
from django.http import JsonResponse

from random import randint
from django.views.generic import TemplateView
from jchart import Chart
from random import randint
from datetime import datetime, timedelta

from jchart import Chart
from jchart.config import Axes, DataSet, rgba

class BarChart(Chart):
    chart_type = 'bar'

    def get_labels(self, **kwargs):
        return ["January", "February", "March", "April",
                "May", "June", "July"]

    def get_datasets(self, **kwargs):
        data = [10, 15, 29, 30, 5, 10, 22]
        colors = [
            rgba(255, 99, 132, 0.2),
            rgba(54, 162, 235, 0.2),
            rgba(255, 206, 86, 0.2),
            rgba(75, 192, 192, 0.2),
            rgba(153, 102, 255, 0.2),
            rgba(255, 159, 64, 0.2)
        ]

        return [DataSet(label='Bar Chart',
                        data=data,
                        borderWidth=1,
                        backgroundColor=colors,
                        borderColor=colors)]


def dashboard(request):
 
    user = User.objects.get(id=2)
    user_email = user.email
    from_date = date.today()
    to_date = date.today()
    
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = PeriodFilter(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            (from_date, to_date) = form.cleaned_data['Range']

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PeriodFilter(initial={'range': (date.today(), date.today())})

    
    num_Router_lstWk= numOfLeads.numOfRouterCalls(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    num_Web_lstWk= numOfLeads.numOfWebLeads(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    numOfAOs= numOfLeads.numOfAOs(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    numOfIPs= numOfLeads.numOfIPs(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    numOfFunds= numOfLeads.numOfFunds(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    numOfPitch= numOfLeads.numOfPitch(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'),user_email)
    timeseries_data = datatrend.datatrend(user_email)
        
    timeseries_webLeads=timeseries_data[["StartOfWeek","WebLead"]]
    timeseries_Router=timeseries_data[["StartOfWeek","RouterCall"]]
    

    timeseries_webLeads=	  [
		  ['2012, 1, 1', 82],
		  ['2012, 1, 2', 23],
		  ['2012, 1, 3', 66],
		  ['2012, 1, 4', 9],
		  ['2012, 1, 5', 119],
		  ['2012, 1, 6', 6],
		  ['2012, 1, 7', 9]
		];
        
    timeseries_Router=	  [
		  ['2012, 1, 1', 2],
		  ['2012, 1, 2', 2],
		  ['2012, 1, 3', 6],
		  ['2012, 1, 4', 9],
		  ['2012, 1, 5', 19],
		  ['2012, 1, 6', 1],
		  ['2012, 1, 7', 1]
		];
    
    timeseries_webLeads = [100, 80, 60, 40, 20, 10, 0]

    if request.user.is_authenticated():
         return render(
         request, 
         'GDashboard/production/index.html',
         context={'num_router_leads':num_Router_lstWk,'user_email':user_email,'form':form,
                  'num_web_leads':num_Web_lstWk,
                  'numOfAOs':numOfAOs,
                  'numOfIPs':numOfIPs,
                  'numOfFunds':numOfFunds,
                  'numOfPitch':numOfPitch ,                 
                  'timeseries_webLeads':timeseries_webLeads, 
                  'timeseries_Router':timeseries_Router ,
                  'line_chart': BarChart()
                 },
         ) 
    else:       
       return  redirect('accounts/login/')
    # return render(
    #     request, 
    #      'GDashboard/production/index.html',
    #      context={'num_leads_yst':num_Router_lstWk,'user_email':user_email,'form':form},
    #      ) 
 