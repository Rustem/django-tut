from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from company.models import Company
from company.forms import CompanyForm

class CompanyIndexView(TemplateView):

    def get_context_data(self, **kw):
        kw['companies'] = Company.objects.all()
        return kw

    def get(self, request, *a, **kw):
        return super(CompanyIndexView, self).get(request, *a, **kw)

class CompanyCreateView(CreateView):
	form_class = CompanyForm
	success_url = reverse_lazy('list_company')

class CompanyDetailView(DetailView):
	model = Company

class CompanyUpdateView(UpdateView):
	form_class = CompanyForm
	model = Company
	success_url = reverse_lazy('list_company')
