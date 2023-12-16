def find_farthest_orbit(list_of_orbits):
    max_sqr = max([(3.14*els[0]*els[1]) for els in list_of_orbits])
    print(max_sqr)
    return (els for els in list_of_orbits if (3.14*els[0]*els[1]) == max_sqr)


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

