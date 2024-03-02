from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#Part 7 - Auth:
from django.contrib.auth.views import LoginView
#Part 7 - new user signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Part 7 - for implementing Auth on Views
from django.contrib.auth.decorators import login_required

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

@login_required
def monkey_index(request):
  monkeys = Monkey.objects.filter(user=request.user)
  # Can also retrieve the logged in user's cats like this
  # cats = request.user.cat_set.all()
  return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })

  # replaced this for Part 7 Auth
  # monkeys = Monkey.objects.all()
  # return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })
# From Step 1, refactored to use ORM Monkey mondel! (above)
# def monkey_index(request):
#   return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })


@login_required
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


@login_required
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


@login_required
def assoc_accessory(request, monkey_id, accessory_id):
  # Note that you can pass a accessory's id instead of the whole object
  Monkey.objects.get(id=monkey_id).accessories.add(accessory_id)
  return redirect('monkey-detail', monkey_id=monkey_id)


#PART 7 AUTH
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This creates a 'user' form object that includes the data from browser:
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in - and does not redirect or anything else
      login(request, user)
      return redirect('monkey-index')
    else:
      error_message = 'Invalid sign up - try again'
  # In case of a bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  # could put these within the 'render' method below, this just looks cleaner:
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})