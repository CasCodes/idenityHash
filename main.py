import matplotlib.pyplot as plt
import numpy as np

s = "Hello, world!"
MIN_HASH_LEN = 1250

# polynomial rolling hash function
def hash(s: str):
    sum = 0
    p = 89 # TODO for uppercase
    m = 10 ** 9 + 9

    for i in range(len(s)):
        sum += (ord(s[i]) * (p ** i)) % m

    # extend number 
    while len(str(sum)) < MIN_HASH_LEN:
        sum = sum * 9829 # make the number bigger till it reached the minimum size
    
    return str(sum)

def to_grid(hsh: str):
    grid = []
    # get values
    for i in range(MIN_HASH_LEN): 
        grid.append(int(hsh[i]))
    return grid

def draw(grid: list[chr]):
    # set rgb colors
    color1 = (grid[0] / 9, grid[1] / 9, grid[2] / 9)
    color2 = (grid[29] / 9, grid[28] / 9, grid[27] / 9)

    # cluster 
    # create a 50x50 grid
    grid_array = np.ones((50, 50, 3))

    for i in range(50):
        for j in range(25):  # only fill the first 3 columns
            if grid[i * 25 + j] % 2 == 0:
                grid_array[i, j] = color1
                grid_array[i, 49 - j] = color1  # mirror on x = 3 axis
            else:
                
                grid_array[i, j] = color2
                grid_array[i, 49 - j] = color2  # mirror on x = 3 axis
    plt.imshow(grid_array)
    plt.axis('off')
    plt.show()

# TODO: user input

# call the functions
h = hash(s)
grid = to_grid(h)
draw(grid)