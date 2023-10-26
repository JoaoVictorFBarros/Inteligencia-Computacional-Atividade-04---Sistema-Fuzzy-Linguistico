def high_activation(inclination, speed, march):
    return max(
        min(inclination[2],march[0],speed[2]),
        min(inclination[2],march[1],speed[2]),
    )

def mid_activation(inclination, speed, march):
    return max(
        min(inclination[1],march[0],speed[1]),
        min(inclination[1],march[1],speed[1]),
        min(inclination[1],march[2],speed[1]),
    )

def low_activation(inclination,speed,march):
    return max(
        min(inclination[0],march[1],speed[0]),
        min(inclination[0],march[2],speed[0]),
    )



# def high_activation(inclination, speed, march):
#     return max(
#         (inclination[2] * march[0] * speed[2]),
#         (inclination[2] * march[1] * speed[2]),
#     )

# def mid_activation(inclination, speed, march):
#     return max(
#         (inclination[1] * march[0] * speed[1]),
#         (inclination[1] * march[1] * speed[1]),
#         (inclination[1] * march[2] * speed[1]),
#     )

# def low_activation(inclination,speed,march):
#     return max(
#         (inclination[0] * march[1] * speed[0]),
#         (inclination[0] * march[2] * speed[0]),
#     )