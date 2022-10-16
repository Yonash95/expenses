from collections import OrderedDict

from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce, TruncMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def total_amount_spent(queryset):
    return queryset.aggregate(s=Sum('amount'))


def summary_per_month(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(month=TruncMonth('date'))
        .order_by()
        .values('month')
        .annotate(s=Sum('amount'))
        .values_list('month', 's')
    ))


def category_count(queryset):
    return OrderedDict(sorted(queryset
                              .annotate(category_name=Coalesce('category__name', Value('-')))
                              .order_by().values("category_name")
                              .annotate(c=Count("pk"))
                              .values_list('category_name', 'c')
                              ))
