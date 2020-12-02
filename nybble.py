class Nybble:

    bits = []

    def add(self, operand):
        output = Nybble(False, False, False, False)
        sum = False
        carry = False
        for i in reversed(range(4)):
            sum = self.bits[i] ^ operand.bits[i] ^ carry
            print(carry)
            carry = ((self.bits[i] ^ operand.bits[i]) & carry) | (self.bits[i] & operand.bits[i])
            print(carry)
            output.bits[i] = sum
        self.bits = output.bits
        return carry

    def subtract(self, operand):
        difference = False
        borrow = False
        for i in reversed(range(4)):
            difference = (self.bits[i] ^ operand.bits[i]) ^ borrow
            borrow = (not (self.bits[i] ^ operand.bits[i]) and borrow) or (not self.bits[i] and operand.bits[i])
            self.bits[i] = difference
        return borrow

    def __init__(self, b0, b1, b2, b3):
        self.bits = [b0, b1, b2, b3]
