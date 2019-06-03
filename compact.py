def th(n):
    bits = n.bit_length()
    for i in range(0, 8):
        b = 8*2**i
        if b >= bits:
            return n.to_bytes(int(b/8), byteorder='big').hex()
    return None


def from_compact(compact):
    size = compact >> 24
    word = compact & 0x007fffff
    if size <= 3:
        word >>= 8 * (3 - size)
        u256 = word
    else:
        u256 = word
        u256 <<= 8 * (size - 3)
    negative = word != 0 and (compact & 0x00800000) != 0
    overflow = word != 0 and ((size > 34) or (word > 0xff and size > 33) or (word > 0xffff and size > 32))
    return u256, negative, overflow