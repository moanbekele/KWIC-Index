class LineStorage:
    def __init__(self):
        self.lines = [] # Input here
        
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
