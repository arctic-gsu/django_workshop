from django.shortcuts import render
from django.views.generic import TemplateView

from charts.models import Chart

class ChartView(TemplateView):
    template_name = "charts/chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chart_data"] = Chart.objects.first()
        return context