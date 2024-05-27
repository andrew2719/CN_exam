def character_stuffing(data, special_char, escape_char):
    stuffed_data = ""
    for char in data:
        if char == special_char:
            stuffed_data += escape_char + char
        else:
            stuffed_data += char
    return stuffed_data

# Example usage
data = "Hello$World$Example$Here"
special_char = "$"
escape_char = "\\"
stuffed_data = character_stuffing(data, special_char, escape_char)
print("Original Data: ", data)
print("Stuffed Data: ", stuffed_data)
