from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name='index'),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^knowledge_management/', include('knowledge_management.urls')),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
