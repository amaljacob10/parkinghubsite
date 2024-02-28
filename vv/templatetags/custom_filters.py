# vv/templatetags/custom_filters.py

from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def calculate_cost(intime, outtime):
    if intime and outtime:
        duration = outtime - intime
        cost = duration.total_seconds() * 0.01  # Adjust the cost calculation formula as needed
        return round(cost, 2)  # Round to 2 decimal places
    else:
        return 0.0
