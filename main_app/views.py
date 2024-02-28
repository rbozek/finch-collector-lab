from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def monkey_detail(request, monkey_id):
  monkey = Monkey.objects.get(id=monkey_id)
  return render(request, 'monkeys/detail.html', { 'monkey': monkey })

class MonkeyCreate(CreateView):
  model = Monkey
  fields = '__all__'
  # OR
  # fields = ['name', 'breed', 'description', 'age']
  # going to use method written in models.py instead:
  # success_url = '/monkeys/' 

class MonkeyUpdate(UpdateView):
  model = Monkey
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class MonkeyDelete(DeleteView):
  model = Monkey
  success_url = '/monkeys/'


