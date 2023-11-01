from termcolor import colored

# LOGIC GATES
# 1 = True
# 0 = False


# AND GATE
# If both inputs are 1 then output will be True
# If one input is 0 then output will be False

def AND(a, b):
    # You can change one of the 1s to a 0 to make output False
    if a == 1 and b == 1:
        return True
    else:
        return False


# NAND gate
# Negated AND gate
# Gives an output of 1 if both inputs are 0

def NAND(a, b):
    # Change one of the 0s to a 1 to make the output False
    if a == 0 and b == 0:
        return True
    else:
        return False


# OR gate
# If one of the inputs are 1 then returns with 1
# Return 0 otherwise

def OR(a, b):
    # Change one of these 1s to a 0 to make the output True
    if a == 1 or b == 1:
        return True
    else:
        return False


# XOR gate
# If the inputs are different it gives an output of 1
# Gives 0 if they are the same

def XOR(a, b):
    # Yeah idk
    if a != b:
        return True
    else:
        return False


# NOT gate
# Acts as an inverter
# If input is 1 it will output 0, and vise-versa

def NOT(a):
    return not a


# NOR gate
# Negated OR gate
# If both inputs are 0 outputs a 1
# Outputs 0 otherwise

def NOR(a, b):
    if a == 0 and b == 0:
        return True
    else:
        return False


# XNOR gate
# Negated XOR gate
# If both inputs are the same it gives an output of 1
# Gives an output of 0 otherwise

def XNOR(a, b):
    if a == b:
        return True
    else:
        return False


if __name__=='__main__':
    print()
    print(colored('AND gate output', 'dark_grey'))     # AND
    print(AND(1, 1))
    print()

    print(colored('NAND gate output', 'dark_grey'))    # NAND
    print(NAND(1, 0))
    print()

    print(colored('OR gate output', 'dark_grey'))      # OR
    print(OR(0, 0))
    print()

    print(colored('XOR gate output', 'dark_grey'))     # XOR
    print(XOR(5, 5))
    print()

    print(colored('NOT gate output', 'dark_grey'))     # NOT
    print(NOT(0))
    print()

    print(colored('NOR gate output', 'dark_grey'))     # NOR
    print(NOR(0, 0))
    print()

    print(colored('XNOR gate output', 'dark_grey'))    # XNOR
    print(XNOR(1, 1))
    print()