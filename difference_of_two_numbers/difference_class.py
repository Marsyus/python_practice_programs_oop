class Difference:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def get_difference(self):
        self.difference = self.num1 - self.num2
        print(self.difference)
