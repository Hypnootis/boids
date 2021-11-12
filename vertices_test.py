# Takes a tuple of vertices, then returns the coordinates of the centre
def polygon_centre(vertices):
    x_list = [vertex[0] for vertex in vertices]
    y_list = [vertex[1] for vertex in vertices]
    list_length = len(vertices)
    x_centre = sum(x_list) / list_length
    y_centre = sum(y_list) / list_length

    return (x_centre, y_centre)   # Return a tuple with the centre coordinates

my_vertices = ((1, 1), (0, 0), (2, 5), (0, 2))

print(polygon_centre(my_vertices))