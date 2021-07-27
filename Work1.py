class Matrix:
    def __init__(self, new_list_1, new_list_2):
        self.new_list_1 = new_list_1
        self.new_list_2 = new_list_2

    def __add__(self):
        mx = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                  ]
        for el in range(len(self.new_list_1)):
            for el_1 in range(len(self.new_list_2[el])):
                mx[el][el_1] = self.new_list_1[el][el_1] + self.new_list_2[el][el_1]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mx]))



    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in mx]))


my_matrix = Matrix([[5, 8, 11, 14],
                   [12, 13, 15, 17]],
                   [[24, 42, 12, 32],
                    [42, 25, 12, 5]])
print(my_matrix.__add__())