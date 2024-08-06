from django.test import TransactionTestCase
from .odm2adapter import OdmAdapter

class Odm2AdapterTestCases(TransactionTestCase):
    databases = {'farm'}  # Ensure both databases are used in the test

    def test_insertion(self):
        adapter = OdmAdapter()
        self.assertTrue(adapter.insert_parcel("Farm1", "Plot1"))