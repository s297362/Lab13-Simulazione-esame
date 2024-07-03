from dataclasses import dataclass
@dataclass
class State:
    id : str
    Name : str
    Capital : str
    Lat : float
    Lng : float
    Area : int
    Population : int
    Neighbors : str

    def __eq__(self, other):
        self.id = other.id

    def __hash__(self):
        return hash(self.id)