from mock import MagicMock, patch
from django.test import TestCase
from company import models


name = 'test_company'


class CompanyModelTestCase(TestCase):

    def setUp(self, *a, **kw):
        super(CompanyModelTestCase, self).setUp(*a, **kw)

    def test_hw(self):
        assert str(True) == 'True'

    def test_basic_mock(self):
        mock_foo = MagicMock()
        mock_foo.__str__.return_value = 'I am cool man'
        self.assertEqual(str(mock_foo), 'I am cool man')

    def test_mock_patch(self):
        with patch.object(models.Company, 'get_company') as co:
            co.return_value = models.Company(name='cool', pk=1)
            c = models.Company.get_company(pk=2)
            self.assertEqual(c.name, 'cool')
            self.assertEqual(c.pk, 1)

    def test_company_create(self):
        c = models.Company(name=name)
        c.save()
        self.assertEqual(models.Company.objects.filter(name=name).count(), 1)


