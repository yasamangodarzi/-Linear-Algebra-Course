
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image


image_1 = image.imread('part1.jpg')

red_chanle=np.copy(image_1)
red_chanle[:,:,1]=0
red_chanle[:,:,2]=0
blue_chanle=np.copy(image_1)
blue_chanle[:,:,0]=0
blue_chanle[:,:,2]=0
green_chanle=np.copy(image_1)
green_chanle[:,:,0]=0
green_chanle[:,:,1]=0
plt.figure()
plt.subplot(131)
y_r = np.arange(0, red_chanle.shape[1])
x_r=np.copy(red_chanle[0])
x_r=x_r[:,0]
plt.plot(x_r,y_r, color="red")
plt.subplot(132)
y_b = np.arange(0,blue_chanle.shape[1])
x_b=np.copy(blue_chanle[0])
x_b=x_b[:,1]
plt.plot(x_b,y_b, color="blue")
plt.subplot(133)
y_g = np.arange(0, green_chanle.shape[1])
x_g=np.copy(green_chanle[0])
x_g=x_g[:,2]
plt.plot(x_g,y_g, color="green")


plt.show()
print(78)
#####################part_2
# def Upper_Triangulr_of_Matrix(list_data):
#     Pivot = None
#     Upper_Triangulr_Matrix = np.array(list_data)
#     result = [[Upper_Triangulr_Matrix[j][i] for j in range(len(Upper_Triangulr_Matrix))] for i in range(len(Upper_Triangulr_Matrix[0]))]
#     pivot_index = -1
#     Previous_pivot_index = -1
#     i = 0
#     while i < len(result):
#         result = [[Upper_Triangulr_Matrix[j][i] for j in range(len(Upper_Triangulr_Matrix))] for i in
#                   range(len(Upper_Triangulr_Matrix[0]))]
#         item = result[i]
#         i += 1
#         for index in range(len(item)):
#             if index == 0:
#                 Pivot = None
#                 Previous_pivot_index = pivot_index
#                 pivot_index = -1
#             if item[index] != 0 and Pivot is None and index > Previous_pivot_index:
#                 Pivot = item[index]
#                 pivot_index = index
#                 if pivot_index != Previous_pivot_index + 1:
#                     temp = np.array(Upper_Triangulr_Matrix[Previous_pivot_index + 1])
#                     Upper_Triangulr_Matrix[Previous_pivot_index + 1] = Upper_Triangulr_Matrix[pivot_index]
#                     Upper_Triangulr_Matrix[pivot_index] = temp
#                     pivot_index = Previous_pivot_index + 1
#             elif item[index] != 0 and Pivot is not None:
#                 b = np.array([item[index], 0])
#                 a = np.array([[Pivot, 0], [1, 1]])
#                 Coefficient = np.linalg.solve(a, b)[0]
#                 Upper_Triangulr_Matrix[index] = Upper_Triangulr_Matrix[index] - Upper_Triangulr_Matrix[pivot_index] * Coefficient
#     return Upper_Triangulr_Matrix
#
#
# def Calculate_det(list_data):
#     Echelon_Matrix = np.array(list_data)
#     det = 1
#     for item in range(len(Echelon_Matrix[0])):
#         det = det * Echelon_Matrix[item, item]
#     return det
#
#
# vector_1 = (input().replace(" ", ''))
# vector_2 = (input().replace(" ", ''))
# size = len(vector_2)
# toeplitz_matrix = np.zeros([size, size])
# for item in range(size):
#     list_element = []
#     mylist = []
#     for x in range(item + 1):
#         mylist.append(int(vector_1[x]))
#     if len(mylist) != 1:
#         list.reverse(mylist)
#         for setr in mylist:
#             list_element.append(setr)
#     else:
#         list_element.append(mylist[0])
#     for y in range(size - item - 1):
#         list_element.append(int(vector_2[y+1]))
#     toeplitz_matrix[item] = list_element
#     # pivot = None
# toeplitz_matrix = Upper_Triangulr_of_Matrix(toeplitz_matrix)
# det = Calculate_det(toeplitz_matrix)
# print(det)
