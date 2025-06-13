class Exponent:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def power(self):
        self.power = self.num1 ** self.num2
        print(self.power)
