from django.urls import path
from .views import ClienteRegistrationView

urlpatterns = [
    path('registrar/', ClienteRegistrationView.as_view(), name='registrar_cliente'),
]
