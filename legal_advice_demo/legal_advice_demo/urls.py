from django.contrib import admin
from django.urls import path

from .views import AnswerDetailDownload
from .views import LawCaseDetail
from .views import LawCaseForm
from .views import LawCaseList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LawCaseList.as_view(), name='law-case-list'),
    path('<int:pk>/', LawCaseDetail.as_view(), name='law-case-detail'),
    path('<int:pk>/form/', LawCaseForm.as_view(), name='law-case-form'),
    path('answers/<int:pk>/download/', AnswerDetailDownload.as_view(), name='answer-detail-download')
]
