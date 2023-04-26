class DNA:
    def __init__(self, *sequence):
        self.adenine = "A"
        self.thymine = "T"
        self.guanine = "G"
        self.cytosine = "C"
        self.sequence = list(sequence)

    def __str__(self):
        return f"{self.sequence}"

    @property
    def get_total_adenine(self):
        total_adenine = 0
        for base in range(self.sequence):
            if base == self.adenine:
                total_adenine += 1
        return total_adenine

    @property
    def get_total_thymine(self):
        total_thymine = 0
        for base in range(self.sequence):
            if base == self.thymine:
                total_thymine += 1
        return total_thymine

    @property
    def get_total_guanine(self):
        total_guanine = 0
        for base in range(self.sequence):
            if base == self.guanine:
                total_guanine += 1
        return total_guanine

    @property
    def get_total_cytosine(self):
        total_cytosine = 0
        for base in range(self.sequence):
            if base == self.cytosine:
                total_cytosine += 1
        return total_cytosine
