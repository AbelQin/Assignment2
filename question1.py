# Question 1 - Simple Encryption


# This function encrypts ONE character based on the given rules
def encrypt_char(ch, shift1, shift2):
    # Check if the character is a lowercase letter
    if ch.islower():
        pos = ord(ch) - ord('a')  # convert letter to number (0-25)

        # a-m: move forward
        if ch <= 'm':
            new_pos = (pos + shift1 * shift2) % 26
        # n-z: move backward
        else:
            new_pos = (pos - (shift1 + shift2)) % 26

        return chr(new_pos + ord('a'))  # convert back to letter

    # Check if the character is an uppercase letter
    elif ch.isupper():
        pos = ord(ch) - ord('A')

        # A-M: move backward
        if ch <= 'M':
            new_pos = (pos - shift1) % 26
        # N-Z: move forward by shift2 squared
        else:
            new_pos = (pos + shift2 ** 2) % 26

        return chr(new_pos + ord('A'))

    # Other characters are not changed
    else:
        return ch