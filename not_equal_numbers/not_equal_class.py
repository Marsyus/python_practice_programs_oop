class NotEqual:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def not_equal(self):
        if self.num1 != self.num2:
            print("Not Equal")
            