# A basic Encryptor and Decryptor for the input you provide 
import string
alphabets=string.ascii_lowercase

def encrypt(text,shift):
    cipher_text=""
    for char in text:
        if char in alphabets:
            position=alphabets.find(char)
            new_position=(position+shift)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    return cipher_text

def decrypt(text,shift):
    decipher_text=""
    for char in text:
        if char in alphabets:
            position=alphabets.find(char)
            new_position=(position-shift)%26
            decipher_text+= alphabets[new_position]
        else:
            decipher_text +=char
    return decipher_text


print("Welcome to A basic String Encryptor!:")
while True:
    message=input("Type your message here: ").lower()
    shift_amount=int(input("Type your shift number :"))
    # A shift number is the amount you want your message to be shifted in
    # the english alphabet 
    encrypted_message=encrypt(message,shift_amount)
    print(f"Here is your encrypted message : {encrypted_message}")
    a= input ("Do you want to decrypt your message? Y/N ").lower()
    if a=='y':
        decrypted_message=decrypt(encrypted_message,shift_amount)
        print(f"Here is your decrypted message: {decrypted_message}")
    else:
        print("The Program has exited successfully")
        break