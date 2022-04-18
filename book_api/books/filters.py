from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions.text import Concat
from django_filters import rest_framework as filters
from django_filters.filters import OrderingFilter

from books.models import Book


class BookFilter(filters.FilterSet):
    q = filters.CharFilter(
        method="book_custom_filter",
        label="Search"
    )

    ordering = OrderingFilter(
        fields = (
            ('name', 'name'),
            ("created_at", "created_at"),
        )
    )
    class Meta:
        model = Book
        fields = (
            "author", "category", "q"
        )

    def book_custom_filter(self, queryset, name, value):
        return queryset.filter(name__istartswith=value).annotate(full_name=Concat(
            "author__first_name", V(" "), "author__last_name"
        )).filter(full_name__icontains=value)

   