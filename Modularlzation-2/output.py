class Output:
    def __init__(self, alphabetizer):
        self.alphabetizer = alphabetizer
        
    def print_shifts(self):
        for idx, shift in self.alphabetizer.get_sorted_shifts():
            print(shift)
