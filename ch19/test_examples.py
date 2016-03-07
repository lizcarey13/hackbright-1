import unittest
from examples import *

class TestExamples(unittest.TestCase):


    def test_get_winner_a(self):
        a = "A"
        b = "B"
        result = get_winner(a, 3, b, 2)
        self.assertEqual(result, a)

    def test_get_winner_b(self):
        a = "A"
        b = "B"
        result = get_winner(a, 2, b, 3)
        self.assertEqual(result, b)

    def test_get_winner_tie(self):

        a = "A"
        b = "B"
        result = get_winner(a, 3, b, 3)
        self.assertEqual(result, a + ' ' + b)


class TestTotal(unittest.TestCase):

    def test_calcuate_total_empty(self):
        result = calculate_total([])
        self.assertEqual(result, 0)

    def test_calculate_total_not_empty(self):
        result = calculate_total([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

class TestContact(unittest.TestCase):

    def setUp(self):
        self.contact_Diana = Contact("Diana", "Smith")
        self.contact_Diana.add_hobby("improv")

    def tearDown(self):
        self.contact_Diana = None

    def test_create_contact(self):
        amy = Contact("Amy", "Monet")
        self.assertEqual(amy.first_name, "Amy")
        self.assertEqual(amy.last_name, "Monet")
        self.assertListEqual(amy.hobbies, [])
        
    def test_add_hobby_not_in_list(self):
        self.contact_Diana.add_hobby("work out")
        self.assertEqual(len(self.contact_Diana.hobbies), 2)
        self.assertListEqual(self.contact_Diana.hobbies, ["improv", "work out"])

    def test_add_hobby_already_in_list(self):
        self.contact_Diana.add_hobby("improv")
        self.assertEqual(len(self.contact_Diana.hobbies), 1)
        self.assertListEqual(self.contact_Diana.hobbies, ["improv"])



if __name__ == '__main__':
    unittest.main()