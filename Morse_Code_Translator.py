#python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MorseCode_Chart = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# encrpting English to Morse Code
def encrpt(message):
    encrptedMessage = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            encrptedMessage += MorseCode_Chart[letter] + ' '
        else:
            encrptedMessage += ' '
    return encrptedMessage


# Decripting Morse Code to English
def decrpt(message):
    #extra space added at last to detect the last morse code
    message += ' '

    decrptedMessage = ''
    morseCodeOfsingleLetter = ''
    for letter in message:
        if letter != ' ':
            #counter to keep track of spaces
            i = 0

            morseCodeOfsingleLetter += letter
        else:
            #if i == 1 indicates new character
            i += 1

            # if i == 2 indicates new word
            if i == 2:
                #adding space to saperate english words
                decrptedMessage += ' '
            else:
                #reverse encrption
                decrptedMessage += list(MorseCode_Chart.keys())[list(MorseCode_Chart.values()).index(morseCodeOfsingleLetter)]
                morseCodeOfsingleLetter = ''
    return decrptedMessage

def main():
    message = "SHASHI PREETHAM KANDHAGATLA"
    result = encrpt(message)
    print(result)

    message = '... .... .- ... .... ..  .--. .-. . . - .... .- --  -.- .- -. -.. .... .- --. .- - .-.. .-'
    result = decrpt(message)
    print(result)


if __name__ == '__main__':
    main()
