import django_filters

from .models import *

class JobsFilter(django_filters.FilterSet):
    class Meta:
        model = JobInsert
        
        fields = ['job_title','company_name','job_type','location']

class SkillsFilter(django_filters.FilterSet):
    class Meta:
        model = UserResumes

        fields = ['skills','experience_in_year']