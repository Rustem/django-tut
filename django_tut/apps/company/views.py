from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from company.models import Company
from company.forms import CompanyForm

# from company import tasks

def get_letters(companies):
	letters = []
	for c in companies:
		letters.append(c.name[0])
	return list(set(letters))

class CompanyIndexView(TemplateView):

    def get_context_data(self, **kw):
        companies = Company.objects.order_by('name')
        letters = get_letters(companies)
        kw['letters'] = letters

        # tasks.add.delay(1,2)
        
        alphabeted_companies = {}
        for company in companies:
        	letter = company.name[0]
        	if letter not in alphabeted_companies:
        		alphabeted_companies[letter] = []
        	alphabeted_companies[letter].append(company)
        kw['alphabeted_companies'] = alphabeted_companies
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

class CompanyDeleteView(DeleteView):
	model = Company
	success_url = reverse_lazy('list_company')

class CompanyLetterFilteredView(TemplateView):

    def get_context_data(self, **kw):
        companies = Company.objects.order_by('name')
        letters = get_letters(companies)
        kw['letters'] = letters
        
        companies = Company.objects.filter(name__startswith=kw['let']).order_by('name')
        alphabeted_companies = {kw['let']: []}
        for company in companies:
        	alphabeted_companies[kw['let']].append(company)
        kw['alphabeted_companies'] = alphabeted_companies
        return kw

    def get(self, request, *a, **kw):
        return super(CompanyLetterFilteredView, self).get(request, *a, **kw)