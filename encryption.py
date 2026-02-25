alphabet = "abcdefghijklmnñopqrstuvwxyz"

def encryption(phrase: str, shift: int):
    encrypted = ""

    for letter in phrase:
        isUpper = letter.isupper()
        
        if letter == " ":
            encrypted += " "
        else:
            index = alphabet.find(letter.lower())
            
            if index == -1:
                encrypted += letter
                continue

            new_index = int(index + shift)

            if new_index >= 26:
                new_index -= 26

            if isUpper:
                encrypted += alphabet[new_index].upper()
                continue
            
            encrypted += alphabet[new_index]

    return encrypted


def decryption(phrase: str, shift: int):
    encrypted = ""

    for letter in phrase:
        isUpper = letter.isupper()
        
        if letter == " ":
            encrypted += " "
        else:
            index = alphabet.find(letter.lower())
            
            if index == -1:
                encrypted += letter
                continue

            new_index = int(index - shift)

            if new_index < 0:
                new_index -= 26

            if isUpper:
                encrypted += alphabet[new_index].upper()
                continue
            
            encrypted += alphabet[new_index]

    return encrypted


while True:
    
    option = str(input("Action to do: ").lower())
    
    if option != '1' and option != '2':
        break
    
    match option:
        case '1':
            phrase = str(input("Phrase to encrypt: "))

            shift = int(input("Number of shifts: "))

            result = encryption(phrase, shift)

            print(result)

        case '2':
            phrase = str(input("Phrase to decrypt: "))

            shift = int(input("Number of shifts: "))

            result = decryption(phrase, shift)

            print(result)
    




