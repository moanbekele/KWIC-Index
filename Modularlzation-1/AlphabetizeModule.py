class AlphabetizeModule:
    def __init__(self, shifts):
        self.sorted_shifts = sorted(shifts, key=lambda shift: ' '.join(shift))

    def get_sorted_shifts(self):
        return self.sorted_shifts
