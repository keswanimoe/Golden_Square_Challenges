# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            for letter in self.text:
                if letter in self.vowels:
                    self.text = self.text.replace(letter, '')
            i += 1
        return f'{self.text}'