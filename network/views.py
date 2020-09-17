from math import floor
from random import randint, randrange

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import networkx as nx
from networkx.readwrite import json_graph


def complete_graph(total):
    return nx.complete_graph(total)


def normal_graph():
    return nx.Graph()


class GraphView(View):
    def get(self, request):
        # Creating Complete Graph
        g = complete_graph(5)
        # Adding Node
        g.add_node(5)
        # Adding Node
        g.add_node(6)
        # Adding Edge
        g.add_edge(6, 7)
        g_json = json_graph.node_link_data(g)
        nodes, links = g_json['nodes'], g_json['links']
        return render(request, 'network.html', context={'nodes': nodes, 'links': links})
        # return JsonResponse({'nodes':nodes, 'edges':edges})

    def post(self, request):
        x = randint(0, 100)
        y = randrange(0, 10, 2)
        g = nx.random_regular_graph(y, x)
        g_json = json_graph.node_link_data(g)
        nodes, links = g_json['nodes'], g_json['links']
        return JsonResponse({'nodes': nodes, 'links': links})


class JSNetworkXGraphView(View):
    def get(self, request):
        return render(request, 'jsnetworkx.html')


