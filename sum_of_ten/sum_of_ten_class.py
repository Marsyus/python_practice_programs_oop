class Sum:
    def __init__(self):
        self.numbers = []

    def input_num(self):
        for num in range(1, 11):
            self.num = int(input(f"Enter number {num}: "))
            self.numbers.append(self.num)

    def get_total_sum(self):
        self.total_sum = sum(self.numbers)
        print(self.total_sum)
