# Deck of Cards API Testing

This README provides instructions and examples for testing the Deck of Cards API using Postman and Python.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [API Key](#api-key)
- [Testing with Postman](#testing-with-postman)
  - [Importing Postman Collection](#importing-postman-collection)
  - [Setting Environment Variables](#setting-environment-variables)
  - [Running Tests](#running-tests)
- [Testing with Python](#testing-with-python)
  - [Prerequisites](#prerequisites-python)
  - [Installation](#installation-python)
  - [Running Tests](#running-tests-python)

## Getting Started

### Prerequisites
- Postman: [Download and install Postman](https://www.postman.com/downloads/)
- Python: [Download and install Python](https://www.python.org/downloads/)

### API Key
1. Visit [Deck of Cards API](https://deckofcardsapi.com/) and sign up to obtain your API key.
2. Keep your API key handy for testing.

## Testing with Postman

### Importing Postman Collection
1. Open Postman.
2. Click on "Import" in the top-left corner.
3. Upload the provided `DeckOfCardsAPI.postman_collection.json` file.

### Setting Environment Variables
1. In Postman, click on the gear icon in the top-right corner to open "Manage Environments."
2. Add a new environment, name it, and add a variable for `api_key` with your Deck of Cards API key.

### Running Tests
1. Open the imported collection in Postman.
2. Select the created environment.
3. Run the collection to execute the predefined API tests.

## Testing with Python

### Prerequisites (Python)
- [Requests](https://docs.python-requests.org/en/latest/): Install using `pip install requests`.

### Installation (Python)
Clone the repository:
```bash
git clone https://github.com/yourusername/DeckOfCardsAPITesting.git
cd DeckOfCardsAPITesting
```

### Running Tests (Python)
1. Open the `deck_of_cards_tests.py` file.
2. Replace `'YOUR_API_KEY'` with your actual Deck of Cards API key.
3. Run the Python script:
    ```bash
    python deck_of_cards_tests.py
    ```

---

Feel free to customize the README file according to your specific project structure and requirements. Additionally, you can include more details about specific test cases and expected results in both Postman and Python sections.
