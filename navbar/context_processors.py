def user_role_processor(request):
    """
    Context processor to add user role to all templates
    """
    user_role = None
    if request.user.is_authenticated:
        # Here you should get the user role based on your user model structure
        # This is just a placeholder, you'll need to adapt it to your models
        try:
            if hasattr(request.user, 'pegawai'):
                if hasattr(request.user.pegawai, 'front_desk'):
                    user_role = 'front_desk'
                elif hasattr(request.user.pegawai, 'tenaga_medis'):
                    if hasattr(request.user.pegawai.tenaga_medis, 'dokter_hewan'):
                        user_role = 'dokter_hewan'
                    elif hasattr(request.user.pegawai.tenaga_medis, 'perawat_hewan'):
                        user_role = 'perawat_hewan'
            elif hasattr(request.user, 'klien'):
                user_role = 'klien'
        except:
            user_role = None
    
    return {'user_role': user_role}