from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    if value.title() != value:
        raise ValidationError("Subject must be in title case format.")


def validate_professor_name(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError('Professor name must be in the format "Professor Adam".')

    if words[0] != "Professor" or words[1].title() != words[1]:
        raise ValidationError('Professor name must be in the format "Professor Adam".')