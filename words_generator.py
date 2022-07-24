import requests
class WordsGenerator:
    @staticmethod
    def generate(sentences):
        endpoint = r"http://metaphorpsum.com/paragraphs/1/"
        endpoint += str(sentences)
        response = requests.get(endpoint)
        return response.text