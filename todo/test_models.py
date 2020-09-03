from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels (TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')


## Useful git Commands for testing ##

# Test all test files # python3 manage.py test                                                    
# Test a specific file # python3 manage.py test todo.test_views                                    
# Test a class in a specific file # python3 manage.py test todo.test_models.TestModels                       
# Test a function in a class in a file # python3 manage.py test todo.test_models.TestModels.test_done_defaults_to_false


# Coverage #

# pip3 install coverage
# coverage run --source=<folder name> manage.py test
# coverage report
# coverage html
# python3 -m http.server

# Then you can view the coverage report in the web browser and view missing coverage.

