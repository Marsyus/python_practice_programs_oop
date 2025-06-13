class InBetween:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def get_inbetween(self):
        while self.num1 > self.num2 + 1:
            self.num1 -= 1
            print(self.num1)
        while self.num1 < self.num2 - 1:
            self.num1 += 1
            print(self.num1)
