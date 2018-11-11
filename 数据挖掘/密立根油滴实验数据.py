def calc(time, voltage):
    den_0 = time*(1 + 1.9 * (10 ** (-2) * time ** (0.5)))
    den = voltage * (den_0 ** 1.5)
    result = (1.43 * (10 ** (-14))) / den
    return result


time = 29.85
voltage = 216.3

print(calc(time, voltage))
