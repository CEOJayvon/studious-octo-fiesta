# Import the DES encryption algorithm from PyCryptodome
from Crypto.Cipher import DES


# ---------------------------------------------------------
# FUNCTION: binary_to_bytes
# ---------------------------------------------------------
# DES works with bytes, but we want the user to enter
# plaintext and keys as strings of 0s and 1s.
#
# Example:
# "0000000100100011..."  -->  bytes
#
def binary_to_bytes(binary_string):

    # Convert the binary string into an integer.
    value = int(binary_string, 2)

    # DES operates on blocks of 8 bytes = 64 bits.
    # Convert the integer into exactly 8 bytes.
    return value.to_bytes(8, byteorder="big")


# ---------------------------------------------------------
# FUNCTION: bytes_to_binary
# ---------------------------------------------------------
# Convert the encrypted bytes produced by DES back into
# a string of 0s and 1s so that we can easily compare bits.
#
def bytes_to_binary(byte_string):

    # Convert each byte into an 8-bit binary value.
    # Then join all eight bytes together.
    return ''.join(format(byte, '08b') for byte in byte_string)


# ---------------------------------------------------------
# FUNCTION: flip_bit
# ---------------------------------------------------------
# Change ONE bit in a binary string.
#
# 0 becomes 1
# 1 becomes 0
#
# This allows us to demonstrate the avalanche effect.
#
def flip_bit(binary_string, position):

    # Convert the string into a list so that we can
    # modify an individual character.
    bits = list(binary_string)

    # Flip the selected bit.
    if bits[position] == '0':
        bits[position] = '1'
    else:
        bits[position] = '0'

    # Convert the list back into a string.
    return ''.join(bits)


# ---------------------------------------------------------
# FUNCTION: count_different_bits
# ---------------------------------------------------------
# Compare two binary strings and count how many
# bit positions are different.
#
def count_different_bits(binary1, binary2):

    count = 0

    # Examine every bit position.
    for i in range(len(binary1)):

        # If the two bits are different,
        # increase the counter.
        if binary1[i] != binary2[i]:
            count += 1

    return count


# =========================================================
# STEP 1: GET PLAINTEXT AND KEY FROM USER
# =========================================================

# DES uses a 64-bit plaintext block.
plaintext = input(
    "Enter a 64-bit plaintext (0s and 1s): "
)

# DES accepts a 64-bit key.
# Note: 8 of these bits are traditionally parity bits,
# so DES has an effective key size of 56 bits.
key = input(

    "Enter a 64-bit DES key (0s and 1s): "
)


# =========================================================
# STEP 2: CHECK THE INPUT
# =========================================================

# Make sure the plaintext contains exactly 64 bits
# and contains only 0s and 1s.
if len(plaintext) != 64 or any(bit not in "01" for bit in plaintext):
    print("Error: Plaintext must contain exactly 64 bits.")
    exit()


# Make sure the key contains exactly 64 bits
# and contains only 0s and 1s.
if len(key) != 64 or any(bit not in "01" for bit in key):
    print("Error: Key must contain exactly 64 bits.")
    exit()


# =========================================================
# STEP 3: CONVERT BINARY STRINGS TO BYTES
# =========================================================

# DES cannot directly encrypt strings such as
# "010101...".
#
# Therefore, convert the binary plaintext into bytes.
plaintext_bytes = binary_to_bytes(plaintext)

# Convert the binary key into bytes.
key_bytes = binary_to_bytes(key)


# =========================================================
# STEP 4: CREATE THE DES CIPHER
# =========================================================

# Create a DES cipher using the supplied key.
#
# ECB mode is used because we are encrypting exactly
# ONE 64-bit block.
#
# Using one block also allows us to clearly observe
# the avalanche effect of DES itself.
cipher = DES.new(
    key_bytes,
    DES.MODE_ECB
)


# =========================================================
# STEP 5: ENCRYPT THE ORIGINAL PLAINTEXT
# =========================================================

# Encrypt the 64-bit plaintext block.
ciphertext_bytes = cipher.encrypt(
    plaintext_bytes
)

# Convert the ciphertext bytes back into a
# 64-bit binary string.
ciphertext = bytes_to_binary(
    ciphertext_bytes
)


# Display the original values.
print("\nOriginal plaintext:")
print(plaintext)

print("\nKey:")
print(key)

print("\nCiphertext:")
print(ciphertext)


# =========================================================
# STEP 6: CHANGE ONE PLAINTEXT BIT
# =========================================================
#
# To demonstrate the avalanche effect, we change
# exactly ONE bit of the plaintext.
#
# Python starts counting positions from 0.
# Therefore, position 0 is the first bit.
#
for bit_to_flip in range(64):

    # Flip the selected plaintext bit.
    modified_key = flip_bit(
        key,
        bit_to_flip
    )

    # Convert the modified plaintext into bytes.
    modified_key_bytes = binary_to_bytes(
        modified_key
    )

    modified_cipher = DES.new(
        modified_key_bytes,
        DES.MODE_ECB
    )
# =========================================================
# STEP 7: ENCRYPT THE MODIFIED PLAINTEXT
# =========================================================

# Encrypt the plaintext again after changing
# only one bit.
    modified_ciphertext_bytes = modified_cipher.encrypt(
        plaintext_bytes
    )


    # Convert the new ciphertext into binary.
    modified_ciphertext = bytes_to_binary(
        modified_ciphertext_bytes
    )


# =========================================================
# STEP 8: DISPLAY THE RESULTS
# =========================================================

    print("\n========================================")
    print("          AVALANCHE EFFECT")
    print("========================================")


    print("\nOriginal plaintext:")
    print(plaintext)


    print("\nPlaintext after flipping ONE bit:")
    print(plaintext)


    print("\nOriginal ciphertext:")
    print(ciphertext)

    print("\nOriginal key:")
    print(key)


# =========================================================
# STEP 9: COUNT CHANGED CIPHERTEXT BITS
# =========================================================

# Compare the original ciphertext with the new
# ciphertext and count how many bits changed.
    different_bits = count_different_bits(
        ciphertext,
        modified_ciphertext
    )


# DES ciphertext contains 64 bits.
# Calculate the percentage that changed.
    percentage = (
        different_bits / 64
    ) * 100


# =========================================================
# STEP 10: DISPLAY THE AVALANCHE EFFECT
# =========================================================

    print("Bit flipped:", bit_to_flip + 1)

    print("Modified key:")
    print(modified_key)

    print("New key:")
    print(modified_key)

    print("\nNew ciphertext:")
    print(modified_ciphertext)

    print(
        "\nNumber of key bits changed:",
        different_bits
    )

    print(
        "Percentage of key bits changed:",
        f"{percentage:.2f}%"
    )


# =========================================================
# INTERPRETATION
# =========================================================
#
# A good block cipher should exhibit the avalanche effect.
#
# This means that changing just ONE input bit should cause
# many output bits to change.
#
# Ideally, approximately 50% of the ciphertext bits
# should change.
#
# Since DES has a 64-bit block size, we would expect
# approximately:
#
#              64 / 2 = 32 bits
#
# to change.
#
# The exact number will vary depending on the plaintext
# and key.
#
# IMPORTANT:
# The avalanche effect does NOT mean that exactly 32 bits
# must change every time. Approximately half should change
# on average over many experiments.
