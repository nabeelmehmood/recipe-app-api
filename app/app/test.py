from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test 2 numbers are added correctly"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test 2 numbers are subtracted correctly"""
        self.assertEqual(subtract(11, 5), 6)
