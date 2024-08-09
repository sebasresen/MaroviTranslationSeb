import unittest
from unittest.mock import Mock, patch
from MaroviTranslation.translation.core import Translator
from MaroviTranslation.translation.GoogleTranslator import GoogleTranslator

class TestCore(unittest.TestCase):
    def test_setter(self):
        trans = Translator()
        mock_trans = Mock()
        trans.set_translator(mock_trans)
        self.assertEqual(trans.translator, mock_trans)

    def test_not_implemented(self):
        trans = Translator()
        with self.assertRaises(NotImplementedError):
            trans.translate("Hello")


class TestGoogleTranslation(unittest.TestCase):
    @patch('googletrans.Translator')
    def test_basic_exp(self, MockGTrans):
        mock_trans = MockGTrans.return_value
        mock_trans.translate.return_value.text = "Hola"

        gTrans = GoogleTranslator()
        result = gTrans.translate("Hello")

        self.assertEqual(result, "Hola")
        mock_trans.translate.assert_called_once_with("Hello", src='en', dest='es')

    @patch('googletrans.Translator')
    def test_expression(self, MockGTrans):
        mock_trans = MockGTrans.return_value
        mock_trans.translate.return_value.text = "¡Buen día!"\
        
        gTrans = GoogleTranslator()
        result = gTrans.translate("Good morning!")

        self.assertEqual(result, "¡Buen día!")
        mock_trans.translate.assert_called_once_with("Good morning!", src='en', dest='es')

    @patch('googletrans.Translator')
    def test_empty(self, mockGTrans):
        mock_trans = mockGTrans.return_value
        mock_trans.translate.return_value.text = ""

        gTrans = GoogleTranslator()
        result = gTrans.translate("")

        self.assertEqual(result, "")
        mock_trans.translate.assert_called_once_with("", src='en', dest='es')


if __name__ == "__main__":
    unittest.main()
