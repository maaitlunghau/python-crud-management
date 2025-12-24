class PatientIterator:
    def __init__(self, patients):
        self.patients = patients
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.patients):
            result = self.patients[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration