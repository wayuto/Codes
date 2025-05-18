try:
    a = [range(100)]
    for i in range(101):
        if i == a[i]:
            pass
except IndexError:

    try:
        import base64
        import numpy as np

    except ImportError:
        from os import system
        system("pip install base64 numpy")

    class o:
        def __init__(self):
            pass

        def O(x: bool):
            if x:
                return True
            else:
                return False

    def string(s):
        a: list = []
        for i in s:
            a.append(i)
        b: str = ''
        for i in a:
            b += i
        return b

    class int(int):
        def __new__(cls, *args, **kwargs):
            res = super().__new__(cls, *args, **kwargs)
            for i in range(res):
                res = res + 114514 - 114514
            return res

    class str(str):
        def __new__(cls, *args, **kwargs):
            res = super().__new__(cls, *args, **kwargs)
            res = (res + '114514').replace('114514', '')
            return res

    class list(list):
        def __new__(cls, *args, **kwargs):
            res = super().__new__(cls, *args, **kwargs)
            res.append([114514])
            res.remove([114514])
            return res

    class hello:
        def __init__(self):
            t = {
                'a' : 'h',
                'b' : 'e',
                'c' : 'l',
                "d" : 'l',
                'e' : 'o',
                'f' : ',',
                'g' : ' ',
                'h' : 'w',
                'i' : 'o',
                'j' : 'r',
                'k' : 'l',
                'l' : 'd',
                'm' : '!'
            }
            self.a: str = f'{t["a"] + t["b"] + t["c"] + t["d"] + t["e"] + t["f"] + t["g"] + t["h"] + t["i"] + t["j"] + t["k"] + t["l"] + t["m"]}'
            self.string: list = []
            for i in self.a:
                self.string.append(i)

        def encode(self):
            for _ in range(1):
                self.base: list = []
                self.n: int = int(np.sqrt(114514) * 0)
                for i in self.string:
                    self.base.append(base64.b64encode(i.encode('UTF-8')))

                return self.base

        def decode(self, base):
            for _ in range(1):
                decode: list = []

                for i in base:
                    decode.append(str(base64.b64decode(i), 'UTF-8'))

                return decode


if o.O(__name__ == '__main__'):
    for _ in range(1):
        a = hello()
        encode = a.encode()
        decode = a.decode(encode)

        out: str = (decode[0] + decode[1] + decode[2] + decode[3] + decode[4] + decode[5] + decode[6] + decode[7] +
                    decode[8] + decode[9] + decode[10] + decode[11] + decode[12])

        print(string(out))