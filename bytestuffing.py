def byte_stuffing(data, flag_byte, escape_byte):
    stuffed_data = flag_byte  # Start with the flag byte
    for byte in data:
        if byte in [flag_byte, escape_byte]:
            stuffed_data += escape_byte + byte
        else:
            stuffed_data += byte
    stuffed_data += flag_byte  # End with the flag byte
    return stuffed_data

# Example usage
data = "ABCDEFABC"
flag_byte = "F"
escape_byte = "X"
stuffed_data = byte_stuffing(data, flag_byte, escape_byte)
print("Original Data: ", data)
print("Stuffed Data: ", stuffed_data)
