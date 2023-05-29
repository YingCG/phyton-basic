# number of cans = (wall height x* wall width) / coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 x 4) / 5 = 1.6 --> we need to cans of paint
import math

wall_height = int(input("Height of  wall: "))
wall_width = int(input("Widty of  wall: "))
coverage = 5

def paint_calculation(height = wall_height, width = wall_width, cover = coverage):
    area = height * width
    # num_of_cans = round(area / cover)
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint in total")

paint_calculation(height = wall_height, width = wall_width, cover = coverage)