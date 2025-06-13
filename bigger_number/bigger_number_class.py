class BiggerNumber:
    def input_num(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
    
    def bigger(self):
        if self.num1 > self.num2:
            print(f"{self.num1} is bigger")
        elif self.num1 < self.num2:
            print(f"{self.num2} is bigger")
