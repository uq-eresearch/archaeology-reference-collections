"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
import unittest
import mock
from bulkimport import BulkDataImportHandler
from django.db import models

class MyModel(models.Model):
    pass



class SimpleTest(unittest.TestCase):

    def test_process_row_single(self):
        mapping = {'one': 'one'}

        save_mock = mock.Mock(return_value=None)

        model = mock.Mock(MyModel)
        model.return_value.save = save_mock

        bdih = BulkDataImportHandler()
        bdih.add_mapping(model, mapping)

        headers = ['one', 'two']
        vals = ['val1', 'spot']

        result = bdih.process_row(headers, vals)[0]

        # make sure class was created
        self.assertEqual(model.call_count, 1)

        # now make sure save was called once
        self.assertEqual(save_mock.call_count, 1)

        self.assertEqual('val1', result.one)

    def test_process_row_multi(self):
        mapping_1 = {'one': 'one'}
        save_mock_1 = mock.Mock(return_value=None)
        model_1 = mock.Mock(MyModel)
        model_1.return_value.save = save_mock_1

        mapping_2 = {'two': 'two'}
        save_mock_2 = mock.Mock(return_value=None)
        model_2 = mock.Mock(MyModel)
        model_2.return_value.save = save_mock_2

        linking_func = mock.Mock()

        bdih = BulkDataImportHandler()
        bdih.add_mapping(model_1, mapping_1)
        bdih.add_mapping(model_2, mapping_2)
        bdih.add_linking_function(linking_func)

        headers = ['one', 'two']
        vals = ['val1', 'spot']

        result_1, result_2 = bdih.process_row(headers, vals)

        # make sure one class each was created
        self.assertEqual(model_1.call_count, 1)
        self.assertEqual(model_2.call_count, 1)

        # now make sure each save was called once
        self.assertEqual(save_mock_1.call_count, 1)
        self.assertEqual(save_mock_2.call_count, 1)

        # check values were saved onto each instance
        self.assertEqual('val1', result_1.one)
        self.assertEqual('spot', result_2.two)

        # check the linking function was called
        self.assertTrue(linking_func.called)
        linking_func.assert_called_with(result_1, result_2)


