from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import include, path

from backend.core import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('about/', v.about, name='about'),
    path('accounts/profile/', v.profile, name='profile'),
    path(
        'accounts/login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('person/', include('backend.crm.urls')),
    path('admin/', admin.site.urls),
]
