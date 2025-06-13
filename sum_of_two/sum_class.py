class Sum:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def get_sum(self):
        self.sum = self.num1 + self.num2
        print(self.sum)
