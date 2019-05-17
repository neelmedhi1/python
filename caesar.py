#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#defines the 'characters' as valid 'symbols' to use
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    #defines 'get mode'
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        #asks user whether or not to encrypt or decrypt message
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            #if user uses e or encrypt, it sends you to encryption page
            #if user uses d or decrypt, it sends you to decryption page
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
            #if user uses e or encrypt, it sends you to encryption page
            #if user uses d or decrypt, it sends you to decryption page

def getMessage():
    #defines 'get message'
    print('Enter your message: ')
    #asks user to enter a message
    return input()

def getKey():
    key = 0
    #key is 0 for the actual message (original)
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        #prompts user to enter the key from 1-52
        key = int(input())
        #forces key given to integer format
        if (key >= 1 and key <= MAX_KEY_SIZE):
            #key must be over 1 and under 52
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            #this is where the shift starts happening here depending on the
            #length of the SYMBOLS entered, decreasing based on encryption and decryption
            symbolIndex -= len(SYMBOLS)
            #the symbol or character becomes the encrypted or decrypted letter
            #using the length of the SYMBOLS and key provided
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

#these are the call functions
mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
#translated text, whether it be encrypted, or decrypted
print(getTranslatedMessage(mode, message, key))