class DNA:
    ADENINE = "A"
    THYMINE = "T"
    GUANINE = "G"
    CYTOSINE = "C"

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self) -> str:
        return self.sequence

    @property
    def adenines(self):
        total_adenine = [
            adenines for adenines in self.sequence if adenines.upper() == DNA.ADENINE
        ]
        return len(total_adenine)

    @property
    def thymines(self):
        total_thymine = [
            thymines for thymines in self.sequence if thymines.upper() == DNA.THYMINE
        ]
        return len(total_thymine)

    @property
    def guanines(self):
        total_guanine = [
            guanines for guanines in self.sequence if guanines.upper() == DNA.GUANINE
        ]
        return len(total_guanine)

    @property
<<<<<<< HEAD
    def get_total_cytosine(self):
        total_cytosine = 0
        for base in range(self.sequence):
            if base == self.cytosine:
                total_cytosine += 1
        return total_cytosine

=======
    def cytosines(self):
        total_cytosine = [
            cytosines
            for cytosines in self.sequence
            if cytosines.upper() == DNA.CYTOSINE
        ]
        return len(total_cytosine)

    def sum_sequences(self, *new_sequence):
        self.new_sequence = list(new_sequence)

    def __len__(self):
        return len(self.sequence)

    def __add__(self, other):
        result_sequence = ""
        for self_base, other_base in zip(self.sequence, other.sequence):
            result_sequence += max(self_base, other_base)

        return DNA(result_sequence)

    @staticmethod
    def build_from_file(self, path: str):
        pass

    def dump_from_file(self, path: str):
        pass

    def __getitem__(self):
        pass

    def __setitem__(self):
        """Si la base no existe se pone a"""
        pass


# multiplicacion tienen que ser las bases iguales si no no se añaden
>>>>>>> b1d22f6ebb373532a8a33fbea8564619781175e5
