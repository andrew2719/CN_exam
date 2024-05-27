def calculate_parity_bits(data, r):
    n = len(data)
    # Set all parity bits to 0 initially
    for i in range(r):
        data.insert((2 ** i) - 1, 0)

    # Calculate parity bits for the positions
    for i in range(r):
        position = (2 ** i) - 1
        x = 0
        for j in range(position, n, 2 ** (i + 1)):
            x ^= sum(data[j:j + 2 ** i])
        data[position] = x
    return data

def find_error_pos(hamming_code):
    n = len(hamming_code)
    r = 0
    while (2 ** r) < n + 1:
        r += 1
    error_pos = 0
    for i in range(r):
        position = (2 ** i) - 1
        x = 0
        for j in range(position, n, 2 ** (i + 1)):
            x ^= sum(hamming_code[j:j + 2 ** i])
        if x != 0:
            error_pos += (2 ** i)
    return error_pos

def main():
    data = [int(x) for x in input("Enter data bits: ")]
    r = 0
    while (2 ** r) < len(data) + r + 1:
        r += 1
    hamming_code = calculate_parity_bits(data.copy(), r)
    print("Hamming code:", hamming_code)
    received = [int(x) for x in input("Enter received Hamming code: ")]
    error_pos = find_error_pos(received)
    if error_pos:
        print("Error at position:", error_pos)
        received[error_pos - 1] ^= 1
        print("Corrected code:", received)
    else:
        print("No error in the received Hamming code.")

if __name__ == "__main__":
    main()
