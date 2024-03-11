import webbrowser


class DeckPage:

    def __init__(self, api_object):
        self.my_api = api_object

    def shuffle_the_card_by_count_api(self, card_id):
        result = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={card_id}')
        return result.json()

    def shuffle_the_card_by_count_api_status(self):
        result = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        return result

    def all_shuffle_the_card_by_count_api(self):
        for deck_count in range(1, 21):
            result = self.shuffle_the_card_by_count_api(str(deck_count))
            print("Result:", result)

    def return_deck_card_id_of_card_by_count(self, deck_count):
        result = self.shuffle_the_card_by_count_api(deck_count)
        return result['deck_id']

    def draw_a_card_by_card_id(self, deck_id):
        card_to_draw = self.my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')
        return card_to_draw.json()

    def open_random_card(self):
        for deck_count in range(1, 21):
            deck_card_id = self.return_deck_card_id_of_card_by_count(str(deck_count))
            card_data = self.draw_a_card_by_card_id(deck_card_id)
            card_to_draw = card_data["cards"][0]["image"]
            webbrowser.open(card_to_draw)
            return card_to_draw
