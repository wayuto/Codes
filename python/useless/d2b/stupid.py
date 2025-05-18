def dec2bin(dec: int) -> str:
    bin: str = ""

    while dec >= 1:
        bin = bin + str(dec % 2)
        dec = int(dec / 2)

    return "0b" + bin[::-1]


def bin2dec(bin: str) -> int:
    dec: int = 0
    bin = bin.replace("0b", "")[::-1]

    for i in range(len(bin)):
        dec += int(bin[i]) * 2 ** i

    return dec

print(bin2dec("0b110"))