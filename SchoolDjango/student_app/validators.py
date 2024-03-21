from django.core.exceptions import ValidationError
import re

def validate_name_format(value):
    if not re.match(r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$', value):
        raise ValidationError('Name must be in the format "First M. Last"')

def validate_school_email(value):
    if not value.endswith('@school.com'):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_combination_format(value):
    if not re.match(r'^\d{2}-\d{2}-\d{2}$', value):
        raise ValidationError('Combination must be in the format "12-12-12"')
    
