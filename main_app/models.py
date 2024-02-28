from django.db import models
from django.urls import reverse

BRUSHINGS = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Monkey(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('monkey-detail', kwargs={'monkey_id': self.id})
  
# Add new Brushing model
class Brushing(models.Model):
  date = models.DateField('Brushing date')
  brushing = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=BRUSHINGS,
    # set the default value for brushing to be 'M''
    default=BRUSHINGS[0][0]
  )
  # Create a monkey_id column in the database
  monkey = models.ForeignKey(Monkey, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    # questioning my naming choice - "brushing?" "Brush?"
    return f"{self.get_brushing_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']