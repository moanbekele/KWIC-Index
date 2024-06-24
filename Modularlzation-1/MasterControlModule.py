import InputModule
import CircularShiftModule
import AlphabetizeModule
import OutputModule

class MasterControlModule:
    def __init__(self, file_path):
        self.input_module = InputModule.InputModule(file_path)
        self.circular_shift_module = None
        self.alphabetize_module = None
        self.output_module = None

    def execute(self):
        lines = self.input_module.get_lines()
        self.circular_shift_module = CircularShiftModule.CircularShiftModule(lines)
        shifts = self.circular_shift_module.get_shifts()
        self.alphabetize_module = AlphabetizeModule.AlphabetizeModule(shifts)
        sorted_shifts = self.alphabetize_module.get_sorted_shifts()
        self.output_module = OutputModule.OutputModule(sorted_shifts)
        self.output_module.print_output()

# Main execution
if __name__ == '__main__':
    file_path = 'input.txt'
    master_control = MasterControlModule(file_path)
    master_control.execute()
