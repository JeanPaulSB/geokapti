from beanie import Document


class Locations(Document):
    name: str
    latitude: float
    longitude: float
