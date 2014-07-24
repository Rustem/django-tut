from django.conf.urls import patterns, url
from company.views import CompanyIndexView, CompanyCreateView


urlpatterns = patterns(
    '',
    url(r'^list/$', CompanyIndexView.as_view(
        template_name='company/list.html'), name='list_company'),
    url(r'^new/$', CompanyCreateView.as_view(
    	template_name='company/new.html'), name='new_company')
)
