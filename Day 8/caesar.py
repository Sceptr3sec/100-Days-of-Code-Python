#How did the caesar cipher get its name?
#The caesar cipher is named after Julius Caesar, who is said to have used it to protect his messages. The cipher works by shifting the letters of the alphabet by a certain number of positions. For example, if you shift the letters by 3 positions, then A would become D, B would become E, and so on. This simple method of encryption was used by Caesar to keep his messages secret from his enemies.

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_end = True
        print("Goodbye!")