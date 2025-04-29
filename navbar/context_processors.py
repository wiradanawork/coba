from .views import get_user_role

def navbar_context(request):
    return {
        'user_role': get_user_role(request),
    }