class EvenCount:
    def __init__(self):
        self.even_count = 0

    def input_num(self):
        for num in range(1, 11):
            self.num = int(input(f"Enter number {num}: "))
            if self.num % 2 == 0:
                self.even_count += 1
    
    def get_even_count(self):
        print(self.even_count)
