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





