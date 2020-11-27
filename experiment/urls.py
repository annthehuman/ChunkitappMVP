from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.introduction, name='introduction'),
    path('consent', views.consent, name='consent'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('training1', views.training1, name='training1'),
    path('training2', views.training2, name='training2'),
    path('training3', views.training3, name='training3'),
    path('trainingcompleted', views.trainingcompleted, name='trainingcompleted'),
    path('challange', views.challange, name='challange'),
    path('thanks', views.thanks, name='thanks'),
    path('data/', views.data),
    path('get_challange', views.confirm, name='get_challange'),
    path('taskcompleted', views.taskcompleted, name='taskcompleted'),
    path('feedback', views.feedback, name='feedback'),
    path('end', views.end, name='end')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)