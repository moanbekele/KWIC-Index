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
