class GF24:
    primitive = 0b10011

    def __init__(self, value):
        if isinstance(value, int) and 0 <= value <= 15:
            self.value = value
        elif isinstance(value, str):
            if 0 <= int(value, 16) <= 15:
                self.value = int(value, 16)

    def __add__(self, other):
        return GF24(self.value ^ other.value)

    def __mul__(self, other):
        result = 0
        value_1 = GF24(self.value)
        value_2 = GF24(other.value)

        for i in range(4):
            if value_2.value & 1:
                result ^= value_1.value
            if value_1.value & 0b1000:
                value_1.value = (value_1.value << 1) ^ GF24.primitive
            else:
                value_1.value <<= 1
            value_2.value >>= 1
        return GF24(result)

    def __str__(self):
        return str(self.value)


class SimpleAes:
    s_box = [[9, 4, 10, 11],
             [13, 1, 8, 5],
             [6, 2, 0, 3],
             [12, 14, 15, 7]]
    i_s_box = [[10, 5, 9, 11],
               [1, 7, 8, 15],
               [6, 0, 2, 3],
               [12, 4, 13, 14]]
    mix_box = [1, 4, 4, 1]
    i_mix_box = [9, 2, 2, 9]

    def __init__(self, value):
        try:
            if isinstance(value, int) and 0 <= value < 2 ** 16:
                self.value = [value >> 12, value >> 8 & 15, value >> 4 & 15, value & 15]
            elif isinstance(value, str):
                value = int(value, 16)
                if 0 <= value < 2 ** 16:
                    self.value = [value >> 12, value >> 8 & 15, value >> 4 & 15, value & 15]
            elif isinstance(value, list) and len(value) == 4:
                self.value = [None] * 4
                for i in range(len(value)):
                    if isinstance(value[i], int) and 0 <= value[i] <= 15:
                        self.value[i] = value[i]
                    elif isinstance(value[i], str):
                        value[i] = int(value[i], 16)
                        if 0 <= value[i] <= 15:
                            self.value[i] = value[i]
        except ValueError:
            self.value = None

    @staticmethod
    def s_replace(s, box):
        str_s = bin(s)[2:]
        str_s = "0" * (4 - len(str_s)) + str_s

        h = int(str_s[:2], 2)
        v = int(str_s[2:], 2)
        return box[h][v]

    @staticmethod
    def half_byte_replace(list_s, box):
        return [SimpleAes.s_replace(list_s[i], box) for i in range(len(list_s))]

    @staticmethod
    def row_shift(list_s):
        list_s[1], list_s[3] = list_s[3], list_s[1]
        return list_s

    @staticmethod
    def column_confuse(list_s, box):
        gf_s = [GF24(list_s[i]) for i in range(len(list_s))]
        gf_b = [GF24(box[i]) for i in range(len(box))]

        s = [0] * 4
        s[0] = (gf_b[0] * gf_s[0] + gf_b[2] * gf_s[1]).value
        s[1] = (gf_b[1] * gf_s[0] + gf_b[3] * gf_s[1]).value
        s[2] = (gf_b[0] * gf_s[2] + gf_b[2] * gf_s[3]).value
        s[3] = (gf_b[1] * gf_s[2] + gf_b[3] * gf_s[3]).value
        return s

    @staticmethod
    def key_encrypt(list_s, key):
        return [s ^ k for s, k in zip(list_s, key)]

    @staticmethod
    def g(w):
        n_0 = w >> 4
        n_1 = w & 15
        n_0 = SimpleAes.s_replace(n_0, SimpleAes.s_box)
        n_1 = SimpleAes.s_replace(n_1, SimpleAes.s_box)
        n = n_1 << 4 ^ n_0
        return n

    @staticmethod
    def key_creat(key):
        r_1 = 128
        r_2 = 48

        w_0 = key[0] << 4 ^ key[1]
        w_1 = key[2] << 4 ^ key[3]
        w_2 = w_0 ^ r_1 ^ SimpleAes.g(w_1)
        w_3 = w_2 ^ w_1
        w_4 = w_2 ^ r_2 ^ SimpleAes.g(w_3)
        w_5 = w_4 ^ w_3

        key_1 = [w_2 >> 4, w_2 & 15, w_3 >> 4, w_3 & 15]
        key_2 = [w_4 >> 4, w_4 & 15, w_5 >> 4, w_5 & 15]

        return key_1, key_2

    @staticmethod
    def encrypt(message, key):
        key_1, key_2 = SimpleAes.key_creat(key)
        m = SimpleAes.key_encrypt(message, key)
        m = SimpleAes.half_byte_replace(m, SimpleAes.s_box)
        m = SimpleAes.row_shift(m)
        m = SimpleAes.column_confuse(m, SimpleAes.mix_box)
        m = SimpleAes.key_encrypt(m, key_1)
        m = SimpleAes.half_byte_replace(m, SimpleAes.s_box)
        m = SimpleAes.row_shift(m)
        m = SimpleAes.key_encrypt(m, key_2)
        return m

    @staticmethod
    def decrypt(cipher, key):
        key_1, key_2 = SimpleAes.key_creat(key)
        c = SimpleAes.key_encrypt(cipher, key_2)
        c = SimpleAes.row_shift(c)
        c = SimpleAes.half_byte_replace(c, SimpleAes.i_s_box)
        c = SimpleAes.key_encrypt(c, key_1)
        c = SimpleAes.column_confuse(c, SimpleAes.i_mix_box)
        c = SimpleAes.row_shift(c)
        c = SimpleAes.half_byte_replace(c, SimpleAes.i_s_box)
        c = SimpleAes.key_encrypt(c, key)
        return c

    @staticmethod
    def encrypt_c(message, key, codes):
        try:
            message_s = ""
            message_l = []
            message_input = []
            message_output = []

            for m in message:
                message_c = m.encode(codes)
                message_h = message_c.hex()
                if codes == "ascii":
                    message_s = (2 - len(message_h)) * "0" + message_h
                elif codes == "gb2312" or codes == "gbk":
                    message_s = (4 - len(message_h)) * "0" + message_h
                elif codes == "gb18030":
                    message_s = (8 - len(message_h)) * "0" + message_h
                message_l.append(message_s)

            if codes == "ascii":
                if not len(message_l) % 2 == 0:
                    message_l.append("00")
                message_input = [message_l[i] + message_l[i + 1] for i in range(0, len(message_l), 2)]
            elif codes == "gb2312" or codes == "gbk":
                message_input = message_l
            elif codes == "gb18030":
                message_input = [message_l[i // 2][:4] if i % 2 == 0 else message_l[i // 2][4:]
                                 for i in range(len(message_l * 2))]

            for m_i in message_input:
                m = SimpleAes(m_i)
                k = SimpleAes(key)
                c = SimpleAes.encrypt(m.value, k.value)
                message_output.extend(c)

            message_l = [hex(message_output[i])[2:] for i in range(len(message_output))]
            message_s = "".join(message_l)
            return message_s

        except UnicodeEncodeError:
            return "对应编码不支持该字符"

    @staticmethod
    def decrypt_c(cipher, key, codes):
        try:
            if cipher == "对应编码不支持该字符":
                return cipher

            message_l = []
            cipher_l = []

            for cipher_s in cipher:
                cipher_h = int(cipher_s, 16)
                cipher_l.append(cipher_h)

            for i in range(0, len(cipher_l), 4):
                c = [cipher_l[i], cipher_l[i + 1], cipher_l[i + 2], cipher_l[i + 3]]
                k = SimpleAes(key)
                m = SimpleAes.decrypt(c, k.value)
                message_l.extend(m)

            message_h = [hex(message_l[i])[2:] for i in range(len(message_l))]
            message_s = "".join(message_h)
            message_b = bytes.fromhex(message_s).replace(b'\x00', b'')
            message_s = message_b.decode(codes)
            return message_s

        except UnicodeEncodeError:
            return "对应编码不支持该字符"

    @staticmethod
    def encrypt_b(message, key):
        cipher_l = []

        if len(message) % 4 == 0:
            for i in range(0, len(message), 4):
                message_l = [message[i], message[i + 1], message[i + 2], message[i + 3]]
                m = SimpleAes(message_l)
                if m.value is None:
                    return "明文内容不正确"
                k = SimpleAes(key)
                c = SimpleAes.encrypt(m.value, k.value)
                cipher_l.extend(c)
        else:
            return "明文格式不正确"

        return cipher_l

    @staticmethod
    def decrypt_b(cipher, key):
        message_l = []

        if len(cipher) % 4 == 0:
            for i in range(0, len(cipher), 4):
                cipher_l = [cipher[i], cipher[i + 1], cipher[i + 2], cipher[i + 3]]
                c = SimpleAes(cipher_l)
                if c.value is None:
                    return "密文内容不正确"
                k = SimpleAes(key)
                c = SimpleAes.decrypt(c.value, k.value)
                message_l.extend(c)
        else:
            return "密文格式不正确"

        return message_l

    @staticmethod
    def decode_h(message):
        message_s = ""
        for i in range(0, len(message), 2):
            message_s += chr(int(message[i:i + 2], 16))
        return message_s

    @staticmethod
    def encode_h(message):
        message_h = ""
        for m in message:
            message_s = hex(ord(m))[2:]
            message_h += (2 - len(message_s)) * "0" + message_s
        return message_h

    @staticmethod
    def list_to_string(list_i):
        list_h = [hex(i)[2:] for i in list_i]
        return "".join(list_h)
