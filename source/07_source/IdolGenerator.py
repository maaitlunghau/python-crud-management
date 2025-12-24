class IdolGenerator:
    def __init__(self, idols):
        self.idols = idols

    def __iter__(self):
        for idol in self.idols:
            yield idol