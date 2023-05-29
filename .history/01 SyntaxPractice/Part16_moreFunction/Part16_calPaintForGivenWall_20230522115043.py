# number of cans = (wall height x* wall width) / coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 x 4) / 5 = 1.6 --> we need to cans of paint

wall_height = int(input("Height of  wall: "))
wall_width = int(input("Widty of  wall: "))
coverage = 5
def paint_calculation(wall_height, wall_width):
    print((wall_height * wall_width) / coverage)
    total_paint = round(paint_calculation())
    print(f"We need {total_paint} cans of paint in total")

paint_calculation(wall_height, wall_width)