def ascii_zero():
    return [
        " 000  ",
        "0   0 ",
        "0   0 ",
        "0   0 ",
        " 000  "
    ]

def ascii_one():
    return [
        "  1  ",
        " 11  ",
        "  1  ",
        "  1  ",
        "11111"
    ]

def ascii_two():
    return [
        " 222  ",
        "    2 ",
        " 222  ",
        "2     ",
        " 2222 "
    ]

def ascii_three():
    return [
        " 333  ",
        "    3 ",
        " 333  ",
        "    3 ",
        " 333  "
    ]

def ascii_four():
    return [
        "4   4 ",
        "4   4 ",
        " 4444 ",
        "    4 ",
        "    4 "
    ]

def ascii_five():
    return [
        "55555 ",
        "5     ",
        " 555  ",
        "    5 ",
        " 555  "
    ]

def ascii_six():
    return [
        " 666  ",
        "6     ",
        "6666  ",
        "6   6 ",
        " 666  "
    ]

def ascii_seven():
    return [
        "77777 ",
        "    7 ",
        "   7  ",
        "  7   ",
        " 7    "
    ]

def ascii_eight():
    return [
        " 888  ",
        "8   8 ",
        " 888  ",
        "8   8 ",
        " 888  "
    ]

def ascii_nine():
    return [
        " 9999 ",
        "9   9 ",
        " 9999 ",
        "    9 ",
        " 999  "
    ]

def ascii_colon():
    return [
        "      ",
        "  ::  ",
        "      ",
        "  ::  ",
        "      "
    ]


char = {
            0: ascii_zero(),
            1: ascii_one(),
            2: ascii_two(),
            3: ascii_three(),
            4: ascii_four(),
            5: ascii_five(),
            6: ascii_six(),
            7: ascii_seven(),
            8: ascii_eight(),
            9: ascii_nine(),
            ":": ascii_colon()
}