# Variable size zigzag encoding
# https://developers.google.com/protocol-buffers/docs/encoding#signed-integers

def zigzag_encode(num):
    n = num.bit_length() + 1
    return (num << 1) ^ (num >> n)

def zigzag_decode(num):
    return (num >> 1) ^ -(num & 1)