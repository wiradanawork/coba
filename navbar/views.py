from django.shortcuts import render

def get_user_role(request):
    # Check if user is logged in
    if not request.session.get('user_email'):
        return 'guest'
    
    # Get user role from session if available
    return request.session.get('user_role', 'guest')

def render_navbar(request):
    user_role = get_user_role(request)
    return render(request, 'navbar.html', {'user_role': user_role})