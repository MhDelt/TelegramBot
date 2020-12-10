import json
import random
import nltk


class ChatAI:

    def __init__(self):
        file = open('res/phrasebook.json')
        if file:
            text = file.read()
            if text:
                self.__phrasebook = json.loads(text)

    def get_intent(self, request):
        for intent, intent_data in self.__phrasebook['intents'].items():
            for example in intent_data['examples']:
                filtered_example = self.filter_text(example)
                distance = nltk.edit_distance(filtered_example, self.filter_text(request))
                if distance / len(filtered_example) < 0.7:
                    return intent

    def get_answer_by_intent(self, intent):
        if intent in self.__phrasebook['intents']:
            phrases = self.__phrasebook['intents'][intent]['responses']
            return random.choice(phrases)

    def generate_answer(self, request):

        # 1) Split request into words
        # 2) Normalize words
        # 3) 
        # 4)


        return "I'm not ready to think"  # TODO later

    def get_fail_phrase(self):
        phrases = self.__phrasebook['fail_phrases']
        return random.choice(phrases)

    def create_answer(self, request):

        # NLU
        intent = self.get_intent(request)

        # Response creation
        # Get default answer
        if intent:
            answer = self.get_answer_by_intent(intent)
            if answer:
                return answer
            # Generate answer
        answer = self.generate_answer(request)
        if answer:
            return answer
            # Use fail phrase
        return self.get_fail_phrase()

    def filter_text(self, text):
        text = text.lower()
        text = [c for c in text if c in "abcdefghigklmnopqrstuvwxyz'- 1234567890"]
        text = ''.join(text)
        return text

