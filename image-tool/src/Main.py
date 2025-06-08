inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def read_imagefile(file):
    header = file.readline()
    img_type, width, height, maxval = header.split()
    image_matrix = []
    for _ in range(int(height)):
        row = [int(i) for i in file.readline().split()]
        image_matrix.append(row)
    return image_matrix

def write_imagefile(file, image_matrix):
    height = len(image_matrix)
    width = len(image_matrix[0]) if height > 0 else 0
    maxval = 255

    file.write(f'P2 {width} {height} {maxval}\n')
    for row in image_matrix:
        file.write(' '.join(str(val) for val in row) + '\n')

def misalign(image_matrix):

    new_matrix = [row[:] for row in image_matrix]

    for col in range(len(image_matrix[0])):
        if col % 2 == 1:
            for row in range(len(image_matrix)):
                new_matrix[row][col] = image_matrix[len(image_matrix) - 1 - row][col]

    return new_matrix

def sort_columns(image_matrix):

    for col in range(len(image_matrix[0])):
        column_values = [image_matrix[row][col] for row in range(len(image_matrix))]
        sorted_column = sorted(column_values)
        for row in range(len(image_matrix)):
            image_matrix[row][col] = sorted_column[row]

    return image_matrix

def sort_rows_border(image_matrix):
    def sort_segment(row, start, end):
        segment = row[start:end]
        segment.sort()
        row[start:end] = segment

    for row in image_matrix:
        start = 0
        for i in range(len(row)):
            if row[i] == 0:
                if i > start:
                    sort_segment(row, start, i)
                start = i + 1
        if start < len(row):
            sort_segment(row, start, len(row))

    return image_matrix

def convolution(image_matrix, kernel):
    height = len(image_matrix)
    width = len(image_matrix[0]) if height > 0 else 0

    padded_matrix = [[0 for _ in range(width + 2)] for _ in range(height + 2)]
    for i in range(height):
        for j in range(width):
            padded_matrix[i + 1][j + 1] = image_matrix[i][j]

    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(1,height+1):
        for j in range(1,width+1):
            A00 = padded_matrix[i - 1][j - 1]
            A01 = padded_matrix[i - 1][j]
            A02 = padded_matrix[i - 1][j + 1]
            A10 = padded_matrix[i][j - 1]
            A11 = padded_matrix[i][j]
            A12 = padded_matrix[i][j + 1]
            A20 = padded_matrix[i + 1][j - 1]
            A21 = padded_matrix[i + 1][j]
            A22 = padded_matrix[i + 1][j + 1]

            val1 = A00 * kernel[0][0] + A01 * kernel[0][1] + A02 * kernel[0][2]
            val2 = A10 * kernel[1][0] + A11 * kernel[1][1] + A12 * kernel[1][2]
            val3 = A20 * kernel[2][0] + A21 * kernel[2][1] + A22 * kernel[2][2]

            value = val1 + val2 + val3

            if value > 255:
                value = 255
            if value < 0:
                value = 0
            if 0 <= value <= 255:
                new_matrix[i-1][j-1] = value

    return new_matrix

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
