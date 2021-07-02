from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Item, Side
from django.http import JsonResponse
import json



def collections_home(request):
    sides = Side.objects.all()
    context = {'sides': sides}
    return render(request, 'collection/collection_home.html',context)


def items(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'collection/items.html',context)



def item(request, slug):
    item = Item.objects.get(slug=slug)
    context = {

        'item':item
    }
    return render(request, 'collection/item.html',context)

def sides(request):
    sides = Side.objects.all()
    context = {

        'sides':sides
        }
    return render(request, 'collection/sides.html',context)



def side(request, slug):
    side = Side.objects.get(slug=slug)

    context = {'side':side}

    return render(request, 'collection/side.html', context)




def json_sides(request):
    data = list(Side.objects.values())
    return JsonResponse(data, safe=False)

def json_items(request):
    data = list(Item.objects.values())
    return JsonResponse(data, safe=False)

def load_json(request):
    data = list(Item.objects.values()) + list(Side.objects.values())

    return JsonResponse(data, safe=False)

