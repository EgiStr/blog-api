from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class PostLimitoffset(LimitOffsetPagination):
    default_limit = 5
    
class PostPagepaginator(PageNumberPagination):
    page_size =5