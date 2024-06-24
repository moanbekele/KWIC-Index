from line_storage import LineStorage
from circular_shifter import CircularShifter
from alphabetizer import Alphabetizer
from output import Output

class MasterControl:
    def __init__(self):
        self.storage = LineStorage()
        self.shifter = CircularShifter(self.storage)
        self.alphabetizer = Alphabetizer(self.shifter)
        self.output = Output(self.alphabetizer)
        
    def execute(self, lines):
        for line in lines:
            self.storage.add_line(line)
        
        self.shifter.generate_shifts()
        self.alphabetizer.alphabetize()
        self.output.print_shifts()

if __name__ == "__main__":
    lines = [
        "The quick brown fox",
        "jumps over the lazy dog"
    ]
    control = MasterControl()
    control.execute(lines)
