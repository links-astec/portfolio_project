from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name='home'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("portfolio/skills/",views.skills, name='skills'),
    path("portfolio/project/", views.ProjectList.as_view(), name='project'),
    path("contacts/", views.contact, name='contact'),
    path('portfolio/projects/add/',views.project_create, name='create'),
    path('portfolio/projects/update<int:project_index>/', views.project_update, name='update'),
    path('portfolio/project/delete/<int:project_index>/', views.project_delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)