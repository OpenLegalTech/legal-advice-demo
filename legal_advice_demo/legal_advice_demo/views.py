from django.views.generic import DetailView
from django.views.generic import ListView
from legal_advice_builder.mixins import GenerateEditableDocumentMixin
from legal_advice_builder.models import Answer
from legal_advice_builder.models import LawCase
from legal_advice_builder.views import FormWizardView
from legal_advice_builder.views import PdfDownloadView


class LawCaseList(ListView):

    model = LawCase


class LawCaseDetail(DetailView):

    model = LawCase


class AnswerDetail(DetailView):

    model = Answer


class LawCaseForm(GenerateEditableDocumentMixin,
                  FormWizardView):

    def get_lawcase(self):
        pk = self.kwargs.get('pk')
        return LawCase.objects.get(pk=pk)


class AnswerDetailDownload(PdfDownloadView):

    def get_answer(self):
        pk = self.kwargs.get('pk')
        return Answer.objects.get(pk=pk)
