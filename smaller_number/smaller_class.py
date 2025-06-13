class Smaller:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def get_smaller(self):
        if self.num1 > self.num2:
            print(f"{self.num2} is smaller")
        elif self.num1 < self.num2:
            print(f"{self.num1} is smaller")
