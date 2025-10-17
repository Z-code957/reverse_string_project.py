class Reverse():
    def __init__(self, text):
        self.text = text
    def value(self):
        return self.text
    def revalue(self):
        return self.text[::-1]
name = input("Please enter any name: ")
t = Reverse(name)
print("Original value: ", t.value())
print("Reverse value: ", t.revalue())