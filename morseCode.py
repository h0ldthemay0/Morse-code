# Conner Baughman
#
#
# Converts input message into morse code and viceversa
#


morseDict = {'!':'!', '?':'?', ' ': ' ', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}

alphaDict = {'!':'!', '?':'?', ' ': ' ', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'w', '-.--':'y', '--..':'z'}


while True:
    message = input("Enter your message: ")
    message = message.lower()
    morseMsg = message.split()
    #print(morseMsg)
    translatedMsg = []
    if message == "exit!":
        break

    elif message[0] in morseDict:
        for letter in message:
            translatedMsg.append(morseDict[letter])
            #print(morseDict[letter])

    elif morseMsg[0] in alphaDict:
        for letter in morseMsg:
                translatedMsg.append(alphaDict[letter])


    translatedMsg = ' '.join(translatedMsg)
    translatedMsg = translatedMsg.upper()
    print(translatedMsg)