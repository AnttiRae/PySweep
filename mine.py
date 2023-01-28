class Mine:
    coordinates = []

    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def __str__(self):
        return f'Mine: {self.coordinates}'

