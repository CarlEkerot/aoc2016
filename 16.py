def generate_data(s, l):
    while len(s) < l:
        s += '0' + ''.join(['1' if c == '0' else '0' for c in s[::-1]])
    return s[:l]


def checksum(s):
    while True:
        pairs = [s[i:i+2] for i in range(0, len(s), 2)]
        s = ''.join([str(int(p[0] == p[1])) for p in pairs])
        if len(s) % 2 == 1:
            return s


print(checksum(generate_data('11100010111110100', 272)))
print(checksum(generate_data('11100010111110100', 35651584)))
