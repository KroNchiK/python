class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        tmp_str = ""
        for i in self.matrix:
            tmp_str += "\n"
            for j in i:
                tmp_str += str(j) + "\t"
        return tmp_str

    def __add__(self, other):
        result = []
        for sublist in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return Matrix(result)
        # for i in range(len(self.matrix) - 1):
        #     for j in range(len(self.matrix[0]) - 1):
        #         result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)

matrix_1 = Matrix([[60, 45], [65, 98], [23, 67]])
matrix_2 = Matrix([[47, 89], [345, 21], [97, 240]])
matrix_3 = Matrix([[68, 247], [34, 46], [108, 66]])
print(matrix_1)
print(matrix_1+matrix_2)

