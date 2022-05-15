from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, logout_then_login

app_name = 'micuenta'
urlpatterns = [
    #path('login/', views.login, name='login')
    path('login/', LoginView.as_view(template_name = 'micuenta/login.html'), name='login'),
    path('logout/',logout_then_login, name='logout'),
    path('micuenta/inicio/', views.inicio, name='inicio'),
    path('registrocuenta/', views.registrocuenta, name='registrocuenta'),
    path('guardarcuenta/', views.guardarcuenta, name='guardarcuenta'),
    path('agendarcita/', views.agendarcita, name='agendarcita'),
    path('edicioncita/<int:id_cita>', views.edicioncita, name='edicioncita'),
    path('edtarcita/<int:id_cita>', views.editarcita, name='editarcita'),
    path('eliminarcita/<int:id_cita>', views.eliminarcita, name='eliminarcita'),
    path('agregarmascota/', views.agregarmascota, name='agregarmascota'),
]