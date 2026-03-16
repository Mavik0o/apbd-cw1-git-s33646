class StatisticsHelper():
    def __init__(self):
        pass
    def calculate_statistics(self, number):
        return sum(number) / len(number)
    def find_minimum(self,  number):
        return min(number)
    def find_maximum(self, number):
        return max(number)