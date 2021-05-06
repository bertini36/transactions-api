from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django Admin, use {% url 'admin:index' %}
    path(f'{settings.ADMIN_URL}', admin.site.urls),

    # Internal apps
    path('', include('src.transactions.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
