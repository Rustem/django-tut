from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from company.models import Company
from company.forms import CompanyForm

class CompanyIndexView(TemplateView):

    def get_context_data(self, **kw):
        kw['companies'] = Company.objects.all()
        return kw

    def get(self, request, *a, **kw):
        return super(CompanyIndexView, self).get(request, *a, **kw)

def create(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/companies/list/')
	else:
		form = CompanyForm()
	return render(request, 'company/new.html', {'form': form})