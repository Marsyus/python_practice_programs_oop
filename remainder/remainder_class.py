class Remainder:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def get_remainder(self):
        self.remainder = self.num1 % self.num2
        print(self.remainder)
        