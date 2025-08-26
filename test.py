from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Example string with whitespace
text = " "

# Replace whitespace with colored versions
colored_text = text.replace(" ", f"{Back.BLUE} {Style.RESET_ALL}") \

print(colored_text)