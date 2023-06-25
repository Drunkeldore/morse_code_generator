from graphic import img
import os


def morse_encoder():
    og_string = input(("What is yo code?: ").lower())
    code_string = ""
    for each in og_string:
        if each in morse_dict:
            code_string += morse_dict[each]
    clear()
    print(code_string)


morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "h": "....",
    "i": ".---",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": "-.-",
    "s": "...",
    "t": "-",
    "u": "..-",
    "w": ".--",
    "y": "-.--",
    "z": "--..",
    ".": "  ",
    " ": " ",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "-...",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

clear = lambda: os.system("cls")
onmode = True
print("Welcome to my Morse Code Generator!\n\n\n")

while onmode == True:
    print(img)
    start = input("Ready to input code? y/n: ")
    if start == "y":
        morse_encoder()
        repeat = input("Do you have more code? y/n: ")

        if repeat == "n":
            onmode = False
        elif repeat == "y":
            continue
        else:
            print("Also, conveniently, not an option.")
    elif start == "n":
        onmode = False
    else:
        print("That wasn't an option, dingus.")

clear()
print("Well then okiedoke. Goodbye!")
