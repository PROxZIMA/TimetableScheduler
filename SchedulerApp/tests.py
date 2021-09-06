from django.test import TestCase

# Create your tests here.
from .views import Schedule
schedule = Schedule().initialize()
schedule.getFitness()