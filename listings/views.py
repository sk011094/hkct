from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Listing
def index(request):
    listings = Listing.objects.all()
    #get all data from listing database
    context = {'listings' : listings}
    # pass database records into listings context
    return render(request,'listings/listings.html', context)

def listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')