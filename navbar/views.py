from django.shortcuts import render

def show_navbar(request):
    # Get user role from session
    user_role = request.session.get('role', 'guest')
    
    context = {
        'role': user_role,
    }
    return render(request, 'navbar.html', context)