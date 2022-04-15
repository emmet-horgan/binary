class Integer:
    def __init__(self, value):
        if isinstance(value, str):
            if value.startswith("0x"):
                self._value = int(value, 16)
            else:
                self._value = int(value)
        else:
            self._value = value

        self._value_str = str(hex(self._value))

    def twoscomplement(self, value=None, size=32):  # Only works for positives
        if value is None:
            return int(pow(2, size) - abs(self._value))
        else:
            return int(pow(2, size) - abs(value))

    def bin(self, value):
        """Displays the binary of a number"""

    @property
    def float32(self):
        """Interprets the value object attribute binary as a float32 as per the IEEE 754 standard"""
        if self._value < 0:
            self._value = pow(2, 32) + self._value

        sign = [1, -1][self._value & 0x80000000 >> 31]  # 0x80000000 = 1000 0000 0000 0000 0000 0000 0000 0000
        mantissa = (self._value & 0x007FFFFF) / pow(2, 23)  # 0x007FFFFF = 0000 0000 0111 1111 1111 1111 1111 1111
        exponent = ((self._value & 0x7F800000) >> 23) - 127  # 0x7F800000 = 0111 1111 1000 0000 0000 0000 0000 0000

        if exponent == -127:
            if mantissa > 0:
                return sign * pow(2, -126) * mantissa
            else:
                return 0
        elif exponent == 128:
            if mantissa > 0:
                return None
            else:
                return float("inf")
        else:
            return sign * pow(2, exponent) * (1 + mantissa)  # add one for hidden bit

    @property
    def float64(self):
        """Interprets the value object attribute binary as a float64 as per the IEEE 754 standard"""
        if self._value < 0:
            self._value = pow(2, 64) + self._value

        sign = [1, -1][self._value & 0x8000000000000000 >> 63]
        mantissa = (self._value & 0x000FFFFFFFFFFFFF) / pow(2, 52)
        exponent = ((self._value & 0x7F800000) >> 52) - 1023

        if exponent == -1023:
            if mantissa > 0:
                return sign * pow(2, -1022) * mantissa
            else:
                return 0

        elif exponent == 1024:
            if mantissa > 0:
                return None
            else:
                float("inf")
        else:
            return sign * pow(2, exponent) * (1 + mantissa)  # add one for hidden bit

    def q(self, m: int, n: int):
        nibbles = int((m + n) / 4)
        hx = int(pow(16, nibbles) - 1)
        # hx = int("0x" + ("F" * nibbles), 16)
        value = self._value & hx
        return value / pow(2, n)
