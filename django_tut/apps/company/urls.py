from django.conf.urls import patterns, url
from company.views import 	CompanyIndexView, \
							CompanyCreateView, \
							CompanyDetailView, \
							CompanyUpdateView, \
							CompanyDeleteView, \
							CompanyLetterFilteredView


urlpatterns = patterns(
    '',
    url(r'^$', CompanyIndexView.as_view(
        template_name='company/list.html'), name='list_company'),
    url(r'^new/$', CompanyCreateView.as_view(
    	template_name='company/new.html'), name='new_company'),
    url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(
    	template_name='company/detail.html'), name='detail_company'),
    url(r'^edit/(?P<pk>\d+)/$', CompanyUpdateView.as_view(
    	template_name='company/edit.html'), name='edit_company'),
    url(r'^delete/(?P<pk>\d+)/$', CompanyDeleteView.as_view(
    	template_name='company/delete.html'), name='delete_company'),
    url(r'^filter/(?P<let>[a-z]{1})/$', CompanyLetterFilteredView.as_view(
    	template_name='company/list.html'), name='letter_filter'),
)
