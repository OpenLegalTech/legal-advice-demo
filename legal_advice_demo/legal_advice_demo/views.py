from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from legal_advice_builder.forms import RenderedDocumentForm
from legal_advice_builder.models import Answer
from legal_advice_builder.models import LawCase
from legal_advice_builder.views import FormWizardView


class LawCaseList(ListView):

    model = LawCase


class LawCaseDetail(DetailView):

    model = LawCase


class AnswerDetail(DetailView):

    model = Answer


class AnswerUpdate(UpdateView):

    model = Answer
    form_class = RenderedDocumentForm

    def get_success_url(self):
        return reverse('answer-detail-update', kwargs={'pk': self.object.id})


class LawCaseForm(FormWizardView):

    def get_lawcase(self):
        pk = self.kwargs.get('pk')
        return LawCase.objects.get(pk=pk)
