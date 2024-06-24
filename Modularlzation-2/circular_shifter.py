class CircularShifter:
    def __init__(self, storage):
        self.storage = storage
        self.shifts = []
        
    def generate_shifts(self):
        for i, line in enumerate(self.storage.get_lines()):
            words = line.split()
            for j in range(len(words)):
                shifted_line = words[j:] + words[:j]
                self.shifts.append((i, ' '.join(shifted_line)))
    
    def get_shifts(self):
        return self.shifts
