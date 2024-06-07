class Band:
    all_bands = []
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        Band.all_bands.append(self)

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
        return Concert.all_concerts

    def venues(self):
        return Venue.all_venues

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

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise TypeError("Date must be a non-empty string")
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self,value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise TypeError("venue should be of class Venue")
        
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self,value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise TypeError("Band should be of class Band")
            
    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    all_venues = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all_venues.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Input non-empty strings only")

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            print("Input non-empty strings only")
    
    def concerts(self):
        return Concert.all_concerts

    def bands(self):
        return Band.all_bands
