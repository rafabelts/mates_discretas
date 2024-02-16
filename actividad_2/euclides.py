def euclides(num_1, num_2):
    if num_1 == 0:
        return num_2
    elif num_2 == 0:
        return num_1
    else:
        return euclides(num_2, num_1 % num_2)

print(euclides(270, 192))
