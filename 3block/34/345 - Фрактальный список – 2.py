def defractalize(fractal):
    return print([el for el in fractal if el is not fractal])


def main():
    fractal = [2, 5]
    fractal.append(fractal)
    fractal.append(3)
    fractal.append(fractal)
    fractal.append(9)
    defractalize(fractal)
    print(fractal)


main()
