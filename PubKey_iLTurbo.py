import binascii

with open('PubKey_02compressed.txt') as f:
    text = f.read()
compressed_key_hex = text.split('\n')
print(compressed_key_hex)
computed_uncompressed_key_list = []
p_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'
p = int(p_hex, 16)
for val in compressed_key_hex:
    x_hex = val[2:66]
    x = int(x_hex, 16)
    prefix = val[0:2]

    y_square = (pow(x, 3, p) + 7) % p
    y_square_square_root = pow(y_square, (p+1)//4, p)
    if prefix == "02":
        y = (-y_square_square_root) % p
    else:
        y = y_square_square_root

    computed_y_hex = hex(y)[2:66]
    computed_y_hex = computed_y_hex.zfill(64)
    computed_uncompressed_key = "04" + x_hex + computed_y_hex
    computed_uncompressed_key_list.append(computed_uncompressed_key)
with open('PubKey_04uncompressed.txt', 'w') as f:
    f.write('\n'.join(computed_uncompressed_key_list))