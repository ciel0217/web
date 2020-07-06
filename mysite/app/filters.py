from django_filters import filters
from django_filters import FilterSet
from .models import Book


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class BookFilter(FilterSet):

    title = filters.CharFilter(label='タイトル', lookup_expr='contains')
    author = filters.CharFilter(label='著者', lookup_expr='contains')
    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'title'),
            ('author', 'author'),
        ),
        field_labels={
            'title': 'タイトル',
            'author': '著者',
        },
        label='並び順'
    )

    class Meta:

        model = Book
        fields = ('title', 'author',)
