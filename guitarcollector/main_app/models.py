from django.db import models
from django.urls import reverse
from datetime import date

CONDITION = (
  ('B', 'Bad'),
  ('O', 'Okay'),
  ('G', 'Good'),
)

# Create your models here.
class Amp(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)

  def __str__(self):
    return self.name 
  
  def get_absolute_url(self):
    return reverse('amps_detail', kwargs={'pk': self.id})

class Guitar(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  finish = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.model

  def get_absolute_url(self):
    return reverse('detail', kwargs={'guitar_id': self.id})

class Maintenance(models.Model):
  date = models.DateField('Maintenance Date')
  condition = models.CharField(
    max_length=1,
    choices=CONDITION,
    default=CONDITION[0][0]
  )

  guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

  def __str__(self):
    return f"Maintenance on {self.date} condition is {self.get_condition_display()}"

  class Meta:
    ordering = ['-date']