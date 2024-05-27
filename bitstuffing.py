def bit_stuffing(data):
    # Count the consecutive ones
    count = 0
    stuffed_data = ""
    for bit in data:
        if bit == '1':
            count += 1
            stuffed_data += bit
            if count == 5:  # After five consecutive ones, stuff a zero
                stuffed_data += '0'
                count = 0
        else:
            count = 0
            stuffed_data += bit
    return stuffed_data

# Example usage
data = "11111011111101111110"
stuffed_data = bit_stuffing(data)
print("Original Data: ", data)
print("Stuffed Data: ", stuffed_data)
