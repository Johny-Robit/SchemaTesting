from django.test import TestCase
from .odm2adapter import OdmAdapter

# Create your tests here.
class Odm2AdapterTestCases(TestCase):
    databases = {'default', 'farm'}

    def test_insertion(self):
        adapter = OdmAdapter()
        self.assertTrue(adapter.insert_parcel("Farm1", "Plot1"))