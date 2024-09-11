from django.shortcuts import render
from django.conf import  settings
# from testeDjango.services.handlerDataset import testeFunction
import pandas as pd

# Create your views here.
def index(request):
    print(settings.ARCHIVE_CSV)
    # data=pd.read_csv('archive/datatran2007.csv')
    # print(data)




    return  render(request,'index.html')


