class anime:
    def __init__(self, janr, country, osenka):
        self.janr = janr
        self.country = country
        self.osenka = osenka

    def __str__(self):
        return f'{self.janr}, {self.country}, {self.osenka}'

forsaj = anime('Фантастика', 'Япония', '8.4')
print(forsaj)