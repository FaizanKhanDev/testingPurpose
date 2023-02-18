from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from Users.views import index, profile

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('users/', include('Users.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('profile/<username>', profile, name='profile'),


]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns