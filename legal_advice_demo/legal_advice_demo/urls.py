from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import AnswerDetail
from .views import AnswerUpdate
from .views import LawCaseDetail
from .views import LawCaseForm
from .views import LawCaseList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LawCaseList.as_view(), name='law-case-list'),
    path('<int:pk>/', LawCaseDetail.as_view(), name='law-case-detail'),
    path('<int:pk>/form/', LawCaseForm.as_view(), name='law-case-form'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail-download'),
    path('answers/<int:pk>/edit/', AnswerUpdate.as_view(), name='answer-detail-update'),
    path('tinymce/', include('tinymce.urls')),
    path('advicebuilder/admin/', include('legal_advice_builder.urls'))
]
