import unittest


from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
            text = 'Hello'
            result = english_to_french(text)
            self.assertEqual(result, 'Bonjour')

    def test_english_to_french_greeting(self):
            text = 'Hello happy to meet you.'
            result = english_to_french(text)
            self.assertEqual(result, 'Bonjour heureux de vous rencontrer.')

    def test_english_to_french_input_is_null(self):
            text = 'None'
            result = english_to_french(text)
            self.assertNotEqual(result, '')

    def test_french_to_english(self):
            text = 'Bonjour'
            result = french_to_english(text)
            self.assertEqual(result, 'Hello')

    def test_french_to_english_greeting(self):
            text = 'Bonjour heureux de vous rencontrer.'
            result = french_to_english(text)
            self.assertEqual(result, 'Hello happy to meet you.')

    def test_french_to_english_input_is_null(self):
            text = 'None'
            result = french_to_english(text)
            self.assertNotEqual(result, '')

if __name__ == '__main__':
    unittest.main()