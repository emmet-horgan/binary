class Integer():
    def __init__(self, value):
        if isinstance(value, str):
            if value.startswith("0x"):
                self._value = int(value, 16)
            else:
                self._value = int(value)
        else:
            self._value = value

        self._value_str = str(hex(self._value))

    @property
    def float32(self, output=None):
        if self._value < 0:
            self._value = pow(2, 32) + self._value

        bin_str = bin(self._value).split("0b")[1].rjust(32, "0")
        if len(bin_str) != 32:
            raise ValueError(f"Value passed is not single precision, it is {len(tmp) / 2} bytes, single precision" +
                             " floating point is 4 bytes !")

        sign = bin_str[0]
        exponent = bin_str[1:9]
        mantissa = bin_str[9:]
        if output is None:
            sign = int(sign, 2)
            exponent = int(exponent, 2) - 127
            mantissa = float(int(mantissa, 2)) / pow(2, 23)
            if exponent == -127:
                if mantissa > 0:
                    return pow(-1, sign) * pow(2, -126) * (mantissa)
                else:
                    return None

            elif exponent == int("11111111", 2):
                if mantissa > 0:
                    return None
                else:
                    return float("inf")

            else:
                return pow(-1, sign) * pow(2, exponent) * (1 + mantissa)

        if output.upper() == "DISPLAY":
            return sign + "\t" + exponent + "\t" + mantissa


if __name__ == "__main__":
    obj = Integer(6)
    print(pow(2, -127))
    print(obj.float32 - pow(2, -127))
