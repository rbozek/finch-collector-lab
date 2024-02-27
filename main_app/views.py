from django.shortcuts import render

# Added
from django.http import HttpResponse


# Adding the Monkey class & list and view function below the imports
class Monkey:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

monkeys = [
  Monkey('Alfred', 'fake monkey', 'Loyal servant.', 10),
  Monkey('Lumiere', 'brass monkey', 'Handy in pre-electricity-grid times.', 100),
  Monkey('The Wrangler', 'Southwest monkey', 'Don\'t cross this dude.', 4),
  Monkey('PartyBoy', 'Xmas monkey', 'Will barf on your shoes if he drinks too much eggnog.', 6)
]


# Define the home view
def home(request):
  return render(request, 'home.html')
  # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def monkey_index(request):
  return render(request, 'monkeys/monkey-index.html', { 'monkeys': monkeys })
