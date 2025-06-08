car_height = int(input())
car_length = int(input())
man_height = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

#Initial man head coordinates
man_coordinate_list = [[0,0],[0,1],[0,2],[0,3],[0,4],
[1,0],[1,4],[2,0],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],
[4,2],[5,0],[5,1],[5,2],[5,3],[5,4]]

#Adding coordinates of height
for i in range(1,man_height+1):
    man_coordinate_list.append([5+i,2])

#Adding coordinates of legs
man_coordinate_list.append([5 + man_height + 1, 1])
man_coordinate_list.append([5 + man_height + 1, 3])
man_coordinate_list.append([5 + man_height + 2, 0])
man_coordinate_list.append([5 + man_height + 2, 4])

#Adding coordinates of car
car_coordinate_list = list()
bottom_left_coordinate_of_car = [5 + man_height + 2 - 3, 15]
car_coordinate_list.append(bottom_left_coordinate_of_car)

#Adding rest of the car

#Bottom side
for i in range(1,car_length):
    car_coordinate_list.append([5 + man_height + 2 - 3, 15 + i])

#Top side
for i in range(1,car_length):
    car_coordinate_list.append([5 + man_height + 2 - 3 - car_height + 1, 15 + i])

#Left side
for i in range(1,car_height):
    car_coordinate_list.append([5 + man_height + 2 - 3 - i, 15])

#Right side
for i in range(1,car_height):
    car_coordinate_list.append([5 + man_height + 2 - 3 - i, 15 + car_length -1])

#inside coordinates of the car:
inside_car = list()
top_left_coordinate = [5 + man_height + 2 - 3 - car_height + 1, 15]

for i in range(1,car_length-1):
    for j in range(1,car_height-1):
        inside_car.append([5 + man_height + 2 - 3 - car_height + 1 + j, 15 + i])

total_car_list = inside_car + car_coordinate_list

#printing
for S in range(15 + car_length + 1):
    for i in range(5 + man_height + 2 + 1):
        for j in range(15 + car_length + 1):
            if [i,j] in car_coordinate_list:
                print("X", end ="")
            elif [i,j] in inside_car:
                print(" ", end="")
            elif [i,j] in man_coordinate_list and [i,j] not in total_car_list:
                print("X",end="")
            else:
                print(" ", end="")
        print()
    print()

    for element in car_coordinate_list:
        element[1] = element[1] - 1
    for element in inside_car:
        element[1] = element[1] - 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
