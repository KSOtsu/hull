import hull

points = [
    (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
    (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
    (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
    (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
    (366, 122)
]

concave_hull = hull.concave(points, 3)  # Create concave hull
convex_hull = hull.convex(points)  # Create convex hull
