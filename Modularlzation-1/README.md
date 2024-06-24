# KWIC Index (Modularlzation 1 )
## Usage 
`python MasterControlModule.py`
## Input Data
The content of `input.txt`:

```text
Data Structures and Algorithms
Introduction to Machine Learning
Advanced Python Programming
Fundamentals of Database Systems
Understanding Artificial Intelligence

```

# Modules
## 1. InputModule

Description:
The InputModule reads text from a specified file, processes each line by splitting it into words, and prepares the data for further processing.

```python
class InputModule:
    def __init__(self, file_path):
        self.lines = self._read_file(file_path)
        self.processed_lines = self._process_lines()

    def _read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read().split('\n')

    def _process_lines(self):
        processed = []
        for line in self.lines:
            processed.append(line.split())
        return processed

    def get_lines(self):
        return self.processed_lines
```

output

```
[
    ['Data', 'Structures', 'and', 'Algorithms'],
    ['Introduction', 'to', 'Machine', 'Learning'],
    ['Advanced', 'Python', 'Programming'],
    ['Fundamentals', 'of', 'Database', 'Systems'],
    ['Understanding', 'Artificial', 'Intelligence']
]


```

## 2. CircularShiftModule

Description:
Generates all possible circular shifts for each line of words.

code

```
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

```

output

```
[
    ['Data', 'Structures', 'and', 'Algorithms'],
    ['Structures', 'and', 'Algorithms', 'Data'],
    ['and', 'Algorithms', 'Data', 'Structures'],
    ['Algorithms', 'Data', 'Structures', 'and'],
    ['Introduction', 'to', 'Machine', 'Learning'],
    ['to', 'Machine', 'Learning', 'Introduction'],
    ['Machine', 'Learning', 'Introduction', 'to'],
    ['Learning', 'Introduction', 'to', 'Machine'],
    ['Advanced', 'Python', 'Programming'],
    ['Python', 'Programming', 'Advanced'],
    ['Programming', 'Advanced', 'Python'],
    ['Fundamentals', 'of', 'Database', 'Systems'],
    ['of', 'Database', 'Systems', 'Fundamentals'],
    ['Database', 'Systems', 'Fundamentals', 'of'],
    ['Systems', 'Fundamentals', 'of', 'Database'],
    ['Understanding', 'Artificial', 'Intelligence'],
    ['Artificial', 'Intelligence', 'Understanding'],
    ['Intelligence', 'Understanding', 'Artificial']
]

```



## 3. AlphabetizeModule

Description:
Sorts the circularly shifted lines alphabetically.

code

```
class AlphabetizeModule:
    def __init__(self, shifts):
        self.sorted_shifts = sorted(shifts, key=lambda shift: ' '.join(shift))

    def get_sorted_shifts(self):
        return self.sorted_shifts

```

output

```
[
    ['Advanced', 'Python', 'Programming'],
    ['Algorithms', 'Data', 'Structures', 'and'],
    ['and', 'Algorithms', 'Data', 'Structures'],
    ['Artificial', 'Intelligence', 'Understanding'],
    ['Data', 'Structures', 'and', 'Algorithms'],
    ['Database', 'Systems', 'Fundamentals', 'of'],
    ['Fundamentals', 'of', 'Database', 'Systems'],
    ['Intelligence', 'Understanding', 'Artificial'],
    ['Introduction', 'to', 'Machine', 'Learning'],
    ['Learning', 'Introduction', 'to', 'Machine'],
    ['Machine', 'Learning', 'Introduction', 'to'],
    ['of', 'Database', 'Systems', 'Fundamentals'],
    ['Programming', 'Advanced', 'Python'],
    ['Python', 'Programming', 'Advanced'],
    ['Structures', 'and', 'Algorithms', 'Data'],
    ['Systems', 'Fundamentals', 'of', 'Database'],
    ['to', 'Machine', 'Learning', 'Introduction'],
    ['Understanding', 'Artificial', 'Intelligence']
]

```


## 4. OutputModule

Description:
Prints the alphabetically sorted circularly shifted lines to the terminal.

code

```
class OutputModule:
    def __init__(self, sorted_shifts):
        self.sorted_shifts = sorted_shifts

    def print_output(self):
        for shift in self.sorted_shifts:
            print(' '.join(shift))


```

output

```
Advanced Python Programming
Algorithms Data Structures and
and Algorithms Data Structures
Artificial Intelligence Understanding
Data Structures and Algorithms
Database Systems Fundamentals of
Fundamentals of Database Systems
Intelligence Understanding Artificial
Introduction to Machine Learning
Learning Introduction to Machine
Machine Learning Introduction to
of Database Systems Fundamentals
Programming Advanced Python
Python Programming Advanced
Structures and Algorithms Data
Systems Fundamentals of Database
to Machine Learning Introduction
Understanding Artificial Intelligence


```

# 5. Main Execution in MasterControl.py

Description:
Orchestrates the entire KWIC process by coordinating the InputModule, CircularShiftModule, AlphabetizeModule, and OutputModule.

code

```
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


```

output

```
Advanced Python Programming
Algorithms Data Structures and
and Algorithms Data Structures
Artificial Intelligence Understanding
Data Structures and Algorithms
Database Systems Fundamentals of
Fundamentals of Database Systems
Intelligence Understanding Artificial
Introduction to Machine Learning
Learning Introduction to Machine
Machine Learning Introduction to
of Database Systems Fundamentals
Programming Advanced Python
Python Programming Advanced
Structures and Algorithms Data
Systems Fundamentals of Database
to Machine Learning Introduction
Understanding Artificial Intelligence
```
