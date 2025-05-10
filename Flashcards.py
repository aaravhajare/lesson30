class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):

        return self.word + "(" + self.meaning+")"
    
flash = []

while True:
    word = input("enter the word:")
    meaning = input("eneter the meaning:")

    flash.append(flashcard(word,meaning))

    option = int(input("do you want to add more flashcards? 1 for no and 0 for yes"))

    if (option):
        break

print("your flashcards are:")
for i in flash:
    print(">" , i)