from django.conf.urls import patterns, url
from company.views import CompanyIndexView


urlpatterns = patterns(
    '',
    url(r'^list/$', CompanyIndexView.as_view(
        template_name='company/index.html'))
)
