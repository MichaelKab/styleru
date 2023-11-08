from django.shortcuts import render, HttpResponse
import random
from . import models


def index(request, start=1, end=1):
    item = models.Item.objects.get(id=1)
    item.delete()
    return HttpResponse(f'Item deleted: {item.name} - {item.description} - {item.price}')
    # return render(request, 'myapp/index.html', {'data': ['1', 2, 3, 4], 'rand': random_number, 'arr': array})
