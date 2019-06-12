from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Amp
from .forms import MaintenanceForm
from django.http import HttpResponse

# Create your views here.
class GuitarCreate(CreateView):
  model = Guitar
  fields = '__all__'
  success_url = '/guitars/'

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = ['make', 'model', 'finish']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
  guitars = Guitar.objects.all()
  return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
  guitar = Guitar.objects.get(id=guitar_id)
  maintenance_form = MaintenanceForm()
  return render(request, 'guitars/detail.html', { 
    'guitar': guitar, 'maintenance_form': maintenance_form
    })

def add_maintenance(request, guitar_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.guitar_id = guitar_id
    new_maintenance.save()
  return redirect('detail', guitar_id=guitar_id)

