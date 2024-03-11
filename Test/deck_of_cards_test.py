import re
import unittest
from Infra.api_wrapper import APIWrapper
from Logic.deck_page import DeckPage


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = DeckPage(self.my_api)

    def test_check_code_in_shuffle_the_card_by_count_api(self):
        count = "1"
        result = self.api_logic.shuffle_the_card_by_count_api(count)
        self.assertEqual(result['success'], True)

    def test_check_code_in_all_shuffle_the_card_by_count_api(self):
        result = self.api_logic.all_shuffle_the_card_by_count_api()
        self.assertIsNone(result, "The max number of Decks is 20.")

    def test_check_status_shuffle_the_card_by_count_api(self):
        result = self.api_logic.shuffle_the_card_by_count_api_status()
        self.assertTrue(result.ok)

    def test_random_card_url(self):
        card_url = self.api_logic.open_random_card()
        url_pattern = re.compile(r'https://deckofcardsapi.com/static/img/[0-9JQKA][HDSC].png')
        self.assertRegex(card_url, url_pattern, f"Invalid URL format: {card_url}")
