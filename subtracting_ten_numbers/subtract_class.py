class Substract:
    def __init__(self):
        self.first_num = 0
        self.remaining_num = []

    def input_num(self):
        for num in range(1, 11):
            self.num = int(input(f"Enter for number {num}: "))
            if num == 1:
                self.first_num = self.num
            else:
                self.remaining_num.append(self.num)
    
    def substract(self):
        self.rest = sum(self.remaining_num)
        self.result = self.first_num - self.rest
        print(self.result)
