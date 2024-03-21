from django.urls import path
from .views import UserRegistrationView, CreateEmployeeView

urlpatterns = [
    path('register/admin/', UserRegistrationView.as_view(), name='register-admin'),
    path('criar-funcionario/', CreateEmployeeView.as_view(), name='employee-create'),
]
