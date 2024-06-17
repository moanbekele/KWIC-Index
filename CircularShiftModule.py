class CircularShiftModule:
    def __init__(self, lines):
        self.shifts = self._generate_shifts(lines)

    def _generate_shifts(self, lines):
        shifts = []
        for line in lines:
            for i in range(len(line)):
                shifts.append(line[i:] + line[:i])
        return shifts

    def get_shifts(self):
        return self.shifts
