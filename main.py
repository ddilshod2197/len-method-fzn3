class Masala:
    def __init__(self, nom, qiymat):
        self.nom = nom
        self.qiymat = qiymat

    def __len__(self):
        return len(self.qiymat)

masala = Masala("Masala", "Tajriba")
print(len(masala))  # 8
