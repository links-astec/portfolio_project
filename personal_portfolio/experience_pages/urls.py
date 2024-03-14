from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("portfolio/experience/",views.ExperienceList.as_view(), name='experience'),
    path('portfolio/experience/update<int:experience_index>',views.experience_update,name='update_e'),
    path('portfolio/experience/delete<int:experience_index>',views.experience_delete,name='delete_e'),
    path('portfolio/experience/add',views.experience_create, name='create_e')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)