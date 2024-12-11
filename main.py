import pyfiglet

text = input("Text to ASCII>: ")
ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)