from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import AnswerDetail
from .views import AnswerUpdate
from .views import DocumentAdminView
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
    path('documents/<int:pk>/edit/', DocumentAdminView.as_view(), name='document-update-view'),
    path('documents/', DocumentAdminView.as_view(), name='document-create-view'),
    path('tinymce/', include('tinymce.urls'))
]
