

def confirm_site_admin(request):
    is_site_admin = request.user.is_superuser  # Check if the user is a site admin
    return {'is_site_admin': is_site_admin}
