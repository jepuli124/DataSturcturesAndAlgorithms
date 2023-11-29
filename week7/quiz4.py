class shit:
    def __init__(self):
        self.numbers= []
        self.n = 5
        self.included = []
        self.permutation = 0
        for x in range(100):
            self.included.append(False)
            

    def procedurePermutations(self, k):
        n = self.n
        if k == n:
            self.permutation += 1
            print("permutaion: ", self.permutation, self.numbers)
        else:
            for i in range(n):
                if not self.included[i]:
                    self.included[i] = True
                    if len(self.numbers)-1 < i:
                        self.numbers.append(i)
                    else:   
                        self.numbers[k] = i
                    
                    self.procedurePermutations(k+1)
                    self.included[i] = False


OS = shit()
OS.procedurePermutations(0)