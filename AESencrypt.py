from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a 256-bit AES key
key = get_random_bytes(32)

# Generate a random 128-bit IV for CBC mode
iv = get_random_bytes(16)

# Create AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Read the BMP file
with open("tiger.bmp", "rb") as f:
    data = bytearray(f.read())

# BMP pixel-data offset is stored at bytes 10–13
pixel_offset = int.from_bytes(
    data[10:14],
    byteorder="little"
)

print("File size:", len(data))
print("Pixel data starts at byte:", pixel_offset)

# Separate the BMP header from the pixel data
header = data[:pixel_offset]
pixel_data = data[pixel_offset:]

# Encrypt only the pixel data
encrypted_pixels = cipher.encrypt(
    pad(bytes(pixel_data), AES.block_size)
)

# Keep the BMP header unchanged
encrypted_data = header + encrypted_pixels

# Write the encrypted image
with open("aes-cbc-encrypted.bmp", "wb") as f:
    f.write(encrypted_data)
