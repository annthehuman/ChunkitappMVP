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
    path('challenge', views.challenge, name='challenge'),
    path('thanks', views.thanks, name='thanks'),
    path('data/', views.data),
    path('get_challenge', views.confirm, name='get_challenge'),
    path('taskcompleted', views.taskcompleted, name='taskcompleted'),
    path('feedback', views.feedbackQ, name='feedback'),
    path('end', views.end, name='end'),
    path('passed', views.you_passed, name='passed'),
    path('results', views.results, name='results'),
    path('questions', views.questions, name='questions'),
    path('background_results', views.backgroundRES, name='background_results'),
    path('feedback_results', views.feedbackRES, name='feedback_results'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)