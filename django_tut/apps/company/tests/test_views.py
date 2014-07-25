from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from company.views import *
from company.models import Company


class CompaniesListTestCase(TestCase):
	fixtures = ['company_fixtures.json']
	def setUp(self):
		# Every test needs access to the request factory.
		self.factory = RequestFactory()
		self.companies = Company.objects.all()

	def test_lists_url_resolves_to_company_index_view(self):
		request = self.factory.get(reverse('list_company'))
		view = CompanyIndexView.as_view(template_name='company/list.html')
		response = view(request)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.template_name[0], 'company/list.html')

		# asserts that all elements presented in alphabeted_companies
		num_el = sum(len(item) for item in response.context_data['alphabeted_companies'].itervalues())
		self.assertEqual(num_el, len(self.companies))

		# asserts that each element is associated with appropriate letter
		for key, comp in response.context_data['alphabeted_companies'].items():
			for c in comp:
				self.assertEqual(key.lower(), c.name[0].lower())