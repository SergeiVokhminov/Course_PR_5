from rest_framework.pagination import PageNumberPagination


class PageSizePagination(PageNumberPagination):
    """Разбивка данных на страницы."""

    page_size = 5
    page_size_query = "page_size"
    max_page_size = 20
