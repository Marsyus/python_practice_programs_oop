class OddCount:
    def __init__(self):
        self.numbers = []
        self.odd_count = 0

    def input_num(self):
        for num in range(1, 11):
            self.num = int(input(f"Enter number {num}: "))
            self.numbers.append(self.num)
    
    def count_odds(self):
        for num in self.numbers:
            if num % 2:
                self.odd_count += 1
        print(f"There are {self.odd_count} odd numbers")