from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.humster_register.as_view(), name='humster_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>', views.verification_view.as_view(), name='activate'),

]
