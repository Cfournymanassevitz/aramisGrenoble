import os
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from ventes.utils import get_agency_names


def index(request):
    template = loader.get_template('ventes/template/index.html')
    context = {
        'agency_names': get_agency_names(),
    }
    return HttpResponse(template.render(context, request))


def ventes_json(request):
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)

