from django.urls import path

from network.views import GraphView, JSNetworkXGraphView

urlpatterns = [
    path('', GraphView.as_view(), name='get_graph'),
    path('jsnetworkx/', JSNetworkXGraphView.as_view(), name='js_networkx_graph'),
]
