# custom_converters.py
import datetime
from django.urls.converters import StringConverter
from django.urls import register_converter

class DateTimeConverter(StringConverter):
    regex = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'  # Adjust the regex as needed

    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def to_url(self, value):
        return value.strftime('%Y-%m-%dT%H:%M:%S')

register_converter(DateTimeConverter, 'datetime')
