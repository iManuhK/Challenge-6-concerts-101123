class Band:
    all_bands = []
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise TypeError("Name must be of String type")
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise TypeError("Hometown is a non-empty string")
        
    def concerts(self):
        pass

    def venues(self):
        pass

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    all_concerts = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
        pass

    def bands(self):
        pass
