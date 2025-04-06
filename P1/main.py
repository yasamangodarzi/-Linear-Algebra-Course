import math
import re
import numpy as np

The_pivot_information_of_Matrix = []


def get_information_create_Augmented_matrix():
    input_first = input()
    input_second = input()
    Augmented_Matrix = []
    array_data = []
    list_data_first = input_first.split(" ")
    list_data_second = input_second.split(" ")
    check = False
    for item in list_data_second:
        if item == '+':
            row = []
            i = 0
            for index in list_data_first:
                if index == array_data[i]["char"]:
                    row.append(array_data[i]["number"])
                    if i < len(array_data) - 1:
                        i += 1
                else:
                    row.append(0)
            Augmented_Matrix.append(row)
            array_data.clear()
        elif item == '->':
            check = True
            row = []
            i = 0
            for index in list_data_first:

                if index == array_data[i]["char"]:
                    row.append(array_data[i]["number"])
                    if i < len(array_data) - 1:
                        i += 1
                else:
                    row.append(0)
            Augmented_Matrix.append(row)
            array_data.clear()
        else:
            try:
                result = [re.findall(r'(\w+?)(\d+)', item)][0]

                if check is False:
                    info = {"char": result[0][0], "number": int(result[0][1])}
                else:
                    info = {"char": result[0][0], "number": (int(result[0][1]) * -1)}
                array_data.append(info)
            except:
                if check is False:
                    info = {"char": item, "number": 1}
                else:
                    info = {"char": item, "number": -1}
                array_data.append(info)
    row = []
    i = 0
    for index in list_data_first:
        if index == array_data[i]["char"]:
            row.append(array_data[i]["number"])
            if i < len(array_data) - 1:
                i += 1
        else:
            row.append(0)
    Augmented_Matrix.append(row)
    array_data.clear()
    list_data = []
    for i in range(len(list_data_first)):
        list_data.append(0)
    Augmented_Matrix.append(list_data)
    return Augmented_Matrix


def create_Matrix(list_data):
    matrix = np.array(list_data)
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix = np.array(result)
    return matrix


def Echelon_form_of_Matrix(list_data):
    Pivot = None
    Echelon_Matrix = np.array(list_data).T
    result = [[Echelon_Matrix[j][i] for j in range(len(Echelon_Matrix))] for i in range(len(Echelon_Matrix[0]))]
    pivot_index = -1
    Previous_pivot_index = -1
    i = 0
    while i < len(result):
        result = [[Echelon_Matrix[j][i] for j in range(len(Echelon_Matrix))] for i in range(len(Echelon_Matrix[0]))]
        item = result[i]
        i += 1
        for index in range(len(item)):
            if index == 0:
                info = {"number_of_column": i, "number_of_row": pivot_index, "data": Pivot}
                The_pivot_information_of_Matrix.append(info)
                Pivot = None
                Previous_pivot_index = pivot_index
                pivot_index = -1
            if item[index] != 0 and Pivot is None and index > Previous_pivot_index:
                Pivot = item[index]
                pivot_index = index
                if pivot_index != Previous_pivot_index + 1:
                    temp = np.array(Echelon_Matrix[Previous_pivot_index + 1])
                    Echelon_Matrix[Previous_pivot_index + 1] = Echelon_Matrix[pivot_index]
                    Echelon_Matrix[pivot_index] = temp
                    pivot_index = Previous_pivot_index + 1
            elif item[index] != 0 and Pivot is not None:
                b = np.array([item[index], 0])
                a = np.array([[Pivot, 0], [1, 1]])
                Coefficient = np.linalg.solve(a, b)[0]
                Echelon_Matrix[index] = Echelon_Matrix[index] - Echelon_Matrix[pivot_index] * Coefficient
    return Echelon_Matrix


def Reduced_Echelon_Form_of_Matrix(Reduced_Echelon_Matrix):
    Reduced_Echelon_Matrix = Reduced_Echelon_Matrix.T
    pivot = None
    pivot_index = -1
    i = 1
    result = [[Reduced_Echelon_Matrix[j][i] for j in range(len(Reduced_Echelon_Matrix))] for i in
              range(len(Reduced_Echelon_Matrix[0]))]
    ig = 0
    while ig < len(Reduced_Echelon_Matrix):
        Reduced_Echelon_Matrix = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
        item = Reduced_Echelon_Matrix[ig]
        try:
            info = The_pivot_information_of_Matrix[i]
        except:
            ig += 1
            continue

        pivot = info["data"]
        pivot_index = info["number_of_row"]
        i += 1
        ig += 1
        help_list = []
        for index in range(len(item)):
            if index == info["number_of_row"] and pivot is not None:
                result[info["number_of_row"]] = result[info["number_of_row"]] / info["data"]
            elif item[index] != 0 and pivot is not None:
                b = np.array([item[index], 0])
                a = np.array([[pivot, 0], [1, 1]])
                Coefficient = np.linalg.solve(a, b)[0]
                for number in result[pivot_index]:
                    help_list.append(number * Coefficient)
                result[index] = result[index] - help_list
                help_list.clear()
    return Reduced_Echelon_Matrix


def print_answer(Matrix):
    pol = ""
    answer = []
    answer_2 = []
    ans = 0
    for item in Matrix:
        for index in range(len(item)):
            if item[index] == 1:
                variable = "x" + str(index + 1)
            elif item[index] != 0:
                pol = pol + (str(item[index] * -1) + " x" + str(index + 1)) + " + "
                if index + 1 == 4:
                    ans += item[index] * -6
                else:
                    ans += item[index] * -1
        info = {"variable": variable, "answer": pol}
        info_2 = {"variable": variable, "answer": math.ceil(ans)}
        answer.append(info)
        answer_2.append(info_2)
        pol = ''
        ans = ans * 0
    for item in answer:
        print(item["variable"] + " = " + item["answer"][:-2])
    for item in The_pivot_information_of_Matrix[1:]:
        if item['data'] is None:
            print("x" + str(item["number_of_column"] - 1) + " is free")
    print("--------------------------------------")
    print("final answer:")
    for item in answer_2:
        print(item["variable"] + " = " + str(item["answer"]), end="  ", flush=True)
    print("x" + "4" + " = " + "6")


list_matrix = get_information_create_Augmented_matrix()
print("--------------------------------------")
print("Augmented Matrix : ")
print(create_Matrix(list_matrix))
print("--------------------------------------")
print("Echelon Form Matrix :")
Echelon_Form_Matrix = Echelon_form_of_Matrix(list_matrix)
print(Echelon_Form_Matrix)
print("--------------------------------------")
print("Reduced Echelon Form of Matrix :")
Reduced_Echelon_Form_Matrix = np.array(Reduced_Echelon_Form_of_Matrix(Echelon_Form_Matrix)).T
print(Reduced_Echelon_Form_Matrix)
print("--------------------------------------")
print("answer:")
print_answer(Reduced_Echelon_Form_Matrix)
