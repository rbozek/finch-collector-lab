from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#Part 7 - Auth:
from django.contrib.auth.views import LoginView
from .models import Monkey, Accessory
from .forms import BrushingForm



# Added - might not need anymore!
from django.http import HttpResponse

class Home(LoginView):
  template_name = 'home.html'
# Orig home view before AUTH
# def home(request):
#   return render(request, 'home.html')
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
  accessories_monkey_doesnt_have = Accessory.objects.exclude(id__in = monkey.accessories.all().values_list('id'))
  brushing_form = BrushingForm()
  return render(request, 'monkeys/detail.html', {
    'monkey': monkey,
    'brushing_form': brushing_form,
    'accessories_not' : accessories_monkey_doesnt_have,
  })




class MonkeyCreate(CreateView):
  model = Monkey
  # fields = '__all__'
  # OR
  fields = ['name', 'breed', 'description', 'age']
  # going to use method written in models.py instead:
  # success_url = '/monkeys/' 
  # PART 7 AUTH - This inherited method is called when a valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the monkey
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class MonkeyUpdate(UpdateView):
  model = Monkey
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class MonkeyDelete(DeleteView):
  model = Monkey
  success_url = '/monkeys/'



def add_brushing(request, monkey_id):
  # create a ModelForm instance using the data in request.POST
  form = BrushingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it has the monkey_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.monkey_id = monkey_id
    new_feeding.save()
  return redirect('monkey-detail', monkey_id=monkey_id)


class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'


def assoc_accessory(request, monkey_id, accessory_id):
  # Note that you can pass a accessory's id instead of the whole object
  Monkey.objects.get(id=monkey_id).accessories.add(accessory_id)
  return redirect('monkey-detail', monkey_id=monkey_id)