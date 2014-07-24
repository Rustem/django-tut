from django.forms import ModelForm
from company.models import Company

class CompanyForm(ModelForm):

	class Meta:
		model = Company
		exclude = ('created_at', 'updated_at')