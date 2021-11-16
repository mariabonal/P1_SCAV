# random constants
R = 37
G = 148
B = 63
Y = 105
U = 104
V = 79


# functions
def convert_rgb_yuv(r, g, b):  # RGB to YUV
    # Apply formula for converting rgb to yuv
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128
    return y, u, v


def convert_yuv_rgb(y, u, v): # YUV to RGB
    # Apply formula for converting yuv to rgb
    R = 1.164 * y + 1.596 * v
    G = 1.164 * y - 0.392 * u - 0.813 * v
    B = 1.164 * y + 2.017 * u
    return R, G, B

# call functions
y, u, v = convert_rgb_yuv(R, G, B) 
r, g, b = convert_yuv_rgb(Y, U, V)
# print converted values
print(y,u,v)
print(r,g,b)