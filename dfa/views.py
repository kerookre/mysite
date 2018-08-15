import json

from django.http.response import HttpResponse
from django.shortcuts import render

from .config import graph_styles, \
    default_data_length, \
    default_segments_length

from . import models


def graphs(request):
    possible_data_length = models.get_possible_data_length()

    possible_segments_length = \
        models.get_possible_segments_length(possible_data_length)

    context = {
        'view': 'graphs',
        'graph_type': 'classic_dfa',
        'graph_styles': graph_styles,
        'default_data_length': default_data_length,
        'default_segments_length': default_segments_length,
        'possible_data_length': possible_data_length,
        'possible_segments_length': json.dumps(possible_segments_length),
    }
    return render(request, 'dfa/graphs.html', context)


def get_data(request, graph_type):
    data = {}

    data_length = default_data_length
    segments_length = default_segments_length

    url_query = {}
    for key in request.GET.keys():
        url_query[key] = request.GET.getlist(key)
        if key == 'data_length':
            data_length = int(url_query.pop('data_length', [None])[0])
        if key == 'segments_length':
            segments_length = int(url_query.pop('segments_length', [None])[0])

    print("graph_type = {}, data_length = {}, segments_length = {}"
          .format(graph_type, data_length, segments_length))
    if graph_type == 'classic_dfa':
        data = models.get_classic_dfa_data(data_length, segments_length)
    return HttpResponse(json.dumps(data))
