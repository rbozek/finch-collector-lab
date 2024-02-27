from django.shortcuts import render
from .models import Monkey

# Added
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')
  # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def monkey_index(request):
  monkeys = Monkey.objects.all()
  return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })
# From Step 1, refactored to use ORM Monkey mondel! (above)
# def monkey_index(request):
#   return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })
