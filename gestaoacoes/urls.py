from django.contrib import admin
from django.urls import path, include

from gestaoacoes.base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestaoacoes.base.urls')),
    path('configuracoes/', include('gestaoacoes.base.apps.configuracoes.urls')),
    path('notas/', include('gestaoacoes.base.apps.notas.urls'))
]
