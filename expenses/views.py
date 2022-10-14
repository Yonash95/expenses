from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        order_by = '-date'
        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name').strip()
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            amount = form.cleaned_data.get('amount')
            order = form.cleaned_data.get('order')

            if name:
                queryset = queryset.filter(name__icontains=name)
            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)
            if amount:
                queryset = queryset.filter(amount=amount)

            if order == 'category descending':
                order_by = '-category'
            if order == 'category ascending':
                order_by = 'category'
            if order == 'date descending':
                order_by = '-date'
            if order == 'date ascending':
                order_by = 'date'

        return super().get_context_data(
            form=form,
            object_list=queryset.order_by(order_by),
            summary_per_category=summary_per_category(queryset),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5
