from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    query = request.GET.get('q')
    if query:
        cars = cars.filter(model__icontains=query)
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})

def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})

def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car)
    template_name = 'main/sales.html'
    return render(request, template_name, {'car': car, 'sales': sales})
