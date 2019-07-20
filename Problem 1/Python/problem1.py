class Problem1:

    def __init__(self, limit: int, *args, **kwargs):
        self.limit = limit
        self.denominators = args
        args = ()
        return super().__init__(*args, **kwargs)

    def calculateSeries(self, denominator, limit):
        return denominator * int(limit/denominator) * (1 + int(limit/denominator))/2
    
    def calculate(self):
        summation = 0
        commonMultiples = 1
        for denominator in self.denominators:
            summation += self.calculateSeries(denominator, self.limit)
            commonMultiples *= denominator
        if len(self.denominators) > 1:
            summation -= self.calculateSeries(commonMultiples, self.limit)
        return summation

if __name__ == "__main__":
    denominators = (3, 5)
    ten = Problem1(9, 3, 5)
    oneThousand = Problem1(999, 3, 5)
    print(ten.calculate())
    print(oneThousand.calculate())