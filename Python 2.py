import random
from woordenlijst import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    woord_compleet = "_" * len(word)
    geraden = False
    geraden_letters = []
    geraden_worden = []
    tries = 6
    print("Welkom bij Galgje!")
    print(display_galgje(tries))
    print(woord_compleet)
    print("\n")
    while not geraden and tries > 0:
        guess = input("Raad een letter of het woord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in geraden_letters:
                print("Je hebt al de letter", guess , "geraden.")
            elif guess not in word:
                print(guess, "is helaas niet in het woord.")
                tries -= 1
                geraden_letters.append(guess)
            else:
                print("Goed gedaan,", guess, "is in het woord!")
                geraden_letters.append(guess)
                woord_als_lijst = list(woord_compleet)
                woordlijst = [i for i, letter in enumerate(word) if letter == guess]
                for woord in woordlijst:
                    woord_als_lijst[woord] = guess
                woord_compleet = "".join(woord_als_lijst)
                if "_" not in woord_compleet:
                    geraden = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in geraden_worden:
                print("Je hebt het woord al geraden", guess)
            elif guess != word:
                print(guess, "is niet het woord.")
                tries -= 1
                geraden_woorden.append(guess)
            else:
                geraden = True
                woord_compleet = word
        else:
            print("Dat is niet geldig.")
        print(display_galgje(tries))
        print(woord_compleet)
        print("\n")
    if geraden:
        print("Gefeliciteerd, je hebt het woord geraden! Je hebt gewonnen!")
    else:
        print("Sorry, je hebt helaas geen pogingen meer om het woord te raden. Het woord was " + word + ". Misschien volgende keer!")


def display_galgje(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Nog een keer spelen? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
