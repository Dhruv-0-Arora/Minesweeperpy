class Graph:

    # constructor
    def __init__(self, lines):
        self.array = []

        # Setting 2D array values
        for row in range(lines):
            self.array.append([])
            for col in range(lines):
                self.array[row].append([])
                self.array[row][col].append(0)

    def print_graph(self):
        print("\n-----------------------------\n")
        for row in self.array:
            print("| ", end="")
            for col in row:
                for x in col:
                    print(col[x], end=" | ")
            print("\n")