class OddNumbers:
    def __init__(self):
        self.num = 0
    
    def loop(self):
        while self.num <= 100:
            if self.num % 2:
                print(self.num)
            self.num += 1
