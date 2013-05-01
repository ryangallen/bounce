import datetime
from django import template
from django.utils.timezone import utc

register = template.Library()

@register.filter(name = 'age')

def age(created_at):
	now = datetime.datetime.utcnow().replace(tzinfo = utc)
	age_in_minutes = int((now - created_at).total_seconds())/60
	
	if age_in_minutes < 60:
		value = age_in_minutes
		precision = 'minute'
	elif age_in_minutes < (60 * 24):
		value = age_in_minutes // 60
		precision = 'hour'
	elif age_in_minutes < (60 * 24 * 365.25):
		value = age_in_minutes // (60 * 24)
		precision = 'day'
	else:
		value = age_in_minutes // (60 * 24 * 365.25)
		precision = 'year'

	age_string = '%d %s%s ago' % (value, precision, ('' if value == 1 else 's'))
	return age_string