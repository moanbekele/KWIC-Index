class Alphabetizer:
    def __init__(self, shifter):
        self.shifter = shifter
        self.sorted_shifts = []
        
    def alphabetize(self):
        self.sorted_shifts = sorted(self.shifter.get_shifts(), key=lambda x: x[1])
        
    def get_sorted_shifts(self):
        return self.sorted_shifts
