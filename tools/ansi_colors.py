# ANSI Text Color Codes
text_color_codes = list(range(30, 38)) 

# Color Names Corresponding to ANSI Codes
color_names = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]

print("The colors shown below might have been affected by the `terminal.integrated.minimumContrastRatio` setting in VS Code.")
print("The default is 4.5 to ensure text will always be legible. Change to 1 to see the actual colors.")
print("")

# Display ANSI Colors with Color Names
for i, code in enumerate(text_color_codes):
    color_name = color_names[i]
    print(f"\033[{code}mColor {color_name} ({code}): This is colored text.\033[0m")

print("")

# ANSI Background Color Codes
bg_color_codes = list(range(40, 48)) 

# Display ANSI Colors in a Table
for text_code in text_color_codes:
    for bg_code in bg_color_codes:
        cell_text = f"{text_code} on {bg_code}"
        formatted_text = f"\033[{text_code}m\033[{bg_code}m{cell_text:^12s}\033[0m\033[0m"
        print(formatted_text, end='')
    print("")

# Reset color
print("")
print("\033[0m==All colors reset.==")
