from django.conf.urls import patterns, url
from company.views import CompanyIndexView, CompanyCreateView, CompanyDetailView


urlpatterns = patterns(
    '',
    url(r'^$', CompanyIndexView.as_view(
        template_name='company/list.html'), name='list_company'),
    url(r'^new/$', CompanyCreateView.as_view(
    	template_name='company/new.html'), name='new_company'),
    url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(
    	template_name='company/detail.html'), name='detail_company')
)
