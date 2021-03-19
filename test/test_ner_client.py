import unittest
from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):

    # Expected structure
    # { ents: [{...}}, html: "<span>..."}

    def test_get_ents_returns_dictionary_given_empty_input(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)