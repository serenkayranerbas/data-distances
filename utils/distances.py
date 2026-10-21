
# def manhattan(a, b):
#     d_x = abs(b[0] - a[0])
#     d_y = abs(b[1] - a [1])
#     distance = d_x + d_y
#     return distance

def minkowski(a, b, p):
    d_x = abs(a[0] - b[0])
    d_y = abs(a[1] - b[1])

    distance = (d_x**p + d_y**p)**(1/p)
    return distance

def manhattan(a, b):
    return minkowski(a, b, 1)

manhattan((5, 2), (1, 7))

def euclidean(a, b):
    return minkowski(a, b, 2)

# def euclidean(a,b):
#     d_x = a[0] - b[0]
#     d_y = a[1] - b[1]
    
#     sum_of_squares = d_x**2 + d_y**2
#     distance = sum_of_squares ** 0.5
#     return distance
    
