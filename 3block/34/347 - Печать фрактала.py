def fractal_print(obj):
    i = obj.index(obj)
    obj[i] = [*obj]
    print(obj)


def main():
    fractal = [3]
    fractal.append(fractal)
    fractal.append(2)
    fractal_print(fractal)


main()
