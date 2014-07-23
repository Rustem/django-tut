from company.models import Company
from django.views.generic.base import TemplateView


class CompanyIndexView(TemplateView):

    def get_context_data(self, **kw):
        kw['companies'] = Company.objects.all()
        return kw

    def get(self, request, *a, **kw):
        return super(CompanyIndexView, self).get(request, *a, **kw)
