from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.introduction, name='introduction'),
    path('consent', views.consent, name='consent'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('practice13', views.practice13, name='practice13'),
    path('thanks', views.thanks, name='thanks'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)