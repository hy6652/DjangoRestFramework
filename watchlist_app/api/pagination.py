from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'