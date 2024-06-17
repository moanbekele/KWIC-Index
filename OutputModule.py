class OutputModule:
    def __init__(self, sorted_shifts):
        self.sorted_shifts = sorted_shifts

    def print_output(self):
        for shift in self.sorted_shifts:
            print(' '.join(shift))
