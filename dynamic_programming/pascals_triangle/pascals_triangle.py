class Solution:
    @cache
    def get_row(self, row: int):
        # base cases
        if row == 1:
            return [1]
        if row == 2:
            return [1, 1]
        previous_row = self.get_row(row-1)
        current_row = [1]
        for x, y in zip(previous_row[:-1], previous_row[1:]):
            current_row.append(x+y)
        current_row.append(1)
        return current_row
        
    
    def generate(self, numRows: int) -> List[List[int]]:
        return [self.get_row(row) for row in range(1, numRows+1)]