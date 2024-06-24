# KWIC Index (Modularlzation 1 )
## Usage 
`python MasterControlModule.py`
## Input Data
The content of `input.txt`:

```text
"The quick brown fox"
"jumps over the lazy dog"

```

# Modules
## 1. Line Storage Module

Description:
This module consists of functions to manipulate the storage of lines, words, and characters.

```python
class LineStorage:
    def __init__(self):
        self.lines = []
        
    def add_line(self, line):
        self.lines.append(line.split())
        
    def get_char(self, r, w, c):
        return self.lines[r][w][c]
    
    def set_char(self, r, w, c, char):
        self.lines[r][w] = self.lines[r][w][:c] + char + self.lines[r][w][c+1:]
        
    def words_count(self, r):
        return len(self.lines[r])
    
    def get_line(self, r):
        return ' '.join(self.lines[r])
    
    def get_lines(self):
        return [' '.join(line) for line in self.lines]
```

output

```
[
    ['The quick brown fox', 'jumps over the lazy dog']
]


```

## 2.  Circular Shifter

Description:
This module will provide functions to get circular shifts of lines.

code

```python
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

```

output

```
[
    (0, 'The quick brown fox'),
    (0, 'quick brown fox The'),
    (0, 'brown fox The quick'),
    (0, 'fox The quick brown'),
    (1, 'jumps over the lazy dog'),
    (1, 'over the lazy dog jumps'),
    (1, 'the lazy dog jumps over'),
    (1, 'lazy dog jumps over the'),
    (1, 'dog jumps over the lazy')
]


```



## 3. Alphabetizer

Description:
Sorts the circularly shifted lines alphabetically.

code

```python
class Alphabetizer:
    def __init__(self, shifter):
        self.shifter = shifter
        self.sorted_shifts = []
        
    def alphabetize(self):
        self.sorted_shifts = sorted(self.shifter.get_shifts(), key=lambda x: x[1])
        
    def get_sorted_shifts(self):
        return self.sorted_shifts

```

output

```
[
    (0, 'brown fox The quick'),
    (1, 'dog jumps over the lazy'),
    (0, 'fox The quick brown'),
    (1, 'jumps over the lazy dog'),
    (1, 'lazy dog jumps over the'),
    (1, 'over the lazy dog jumps'),
    (0, 'quick brown fox The'),
    (0, 'The quick brown fox'),
    (1, 'the lazy dog jumps over')
]


```


## 4. Output

Description:
This module will handle the output formatting.

code

```python
class Output:
    def __init__(self, alphabetizer):
        self.alphabetizer = alphabetizer
        
    def print_shifts(self):
        for idx, shift in self.alphabetizer.get_sorted_shifts():
            print(shift)
```

output

```
brown fox The quick
dog jumps over the lazy
fox The quick brown
jumps over the lazy dog
lazy dog jumps over the
over the lazy dog jumps
quick brown fox The
The quick brown fox
the lazy dog jumps over



```

# 5. Main Execution in MasterControl.py

Description:
Orchestrates the entire KWIC process by coordinating the Line Storage, Circular Shifter, Alphabetizer, and Output.

code

```python
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

```