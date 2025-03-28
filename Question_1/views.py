from django.shortcuts import render

from django.http import HttpResponse
from myapp.signals import my_signal
import time

def test_signal(request):
    print("Sending signal...")
    start_time = time.time()
    my_signal.send(sender=None)  
    end_time = time.time()
    print(f"Signal sent, took {end_time - start_time:.2f} seconds")
    return HttpResponse("Signal test complete!")
