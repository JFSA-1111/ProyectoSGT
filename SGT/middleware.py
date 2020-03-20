"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompleteMiddleware:
    """
    Middleware que se encarga de restringir el acceso
    si el usuario no tiene el los datos completos
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Código que se ejecutará para cada solicitud antes de que se llame a la vista."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                perfil = request.user.perfil
                if not perfil.telefono_fijo \
                        and not perfil.celular \
                        and not perfil.celular_telemercadeo:
                    request.log = True
                    if request.path not in [reverse('usuario:perfil'), reverse('usuario:logout')]:
                        return redirect('usuario:perfil')
        if request.user.is_anonymous:
            return redirect('usuario:login')
        request.log = False
        response = self.get_response(request)
        return response
