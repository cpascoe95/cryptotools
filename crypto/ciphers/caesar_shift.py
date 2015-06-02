
class CaesarShift:
    def __init__(self, alph):
        self.alph = alph

    def encrypt(self, key, text):
        output = []

        for char in self.alph.strip(text):
            output.append(self.alph[(self.alph.index(char) + key) % len(self.alph)])

        return ''.join(output)

    def decrypt(self, key, text):
        return self.encrypt(-key, text)