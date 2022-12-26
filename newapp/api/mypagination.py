from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):

    """cursor pagination for student api.

    Args:
        CursorPagination (_type_): _description_
    """
    
    page_size = 5
    ordering = 'name'