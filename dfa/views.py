from django.http.response import HttpResponse
from django.shortcuts import render
import json

from .config import graph_styles
from . import models


def graphs(request):
    context = {
        'view': 'graphs',
        'graphs': [
            'classic_dfa',
            'modified_dfa',
        ],
        'graph_styles': graph_styles
    }
    return render(request, 'dfa/base.html', context)


def get_data(request, graph_type):
    data = {}
    if graph_type == 'classic_dfa':
        data = models.get_classic_dfa_data()
    if graph_type == 'modified_dfa':
        data = models.get_modified_dfa_data()
    return HttpResponse(json.dumps(data))
