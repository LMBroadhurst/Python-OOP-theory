class TempMixin:
    """Convert temperatures from metric to imperial, and reverse."""

    def f_to_c(self, f):
        """Convert imperial to metric."""
        return (f - 32) / 1.8

    def c_to_f(self, c):
        """Convert metric to imperial."""
        return (c * 1.8) + 32


class DistanceMixin:
    """Convert distances from metric to imperial and v.v."""

    def m_to_km(self, miles):
        return miles * 1.60934
    
    def km_to_m(self, km):
        return km * 0.6213717


class DigitalStorageMixin:

    def gb_to_mb(self, gb):
        return gb * 1000

    def mb_to_gb(self, mb):
        return mb / 1000


class Weather(TempMixin, DistanceMixin):
    """Details about weather."""

    def __init__(self, celcius, kmph):
        """Initialise data."""
        self._celcius = celcius
        self._kmph = kmph

    def display(self, metric=True):
        """Display weather values."""
        if metric:
            temp = self._celcius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celcius)
            wind = self.km_to_m(self._kmph)
        
        print(f"Temp: {temp}, Wind Speed: {wind}.")


london = Weather(12, 7)
london.display()

london.display(metric=False)



class HardDrive(TempMixin, DigitalStorageMixin):
    """dididi."""

    def __init__(self, space, celcius):
        """hihiihi"""
        self._space = space
        self._celcius = celcius
    
    def status(self, metric=True):
        """fififi"""
        if metric:
            temp = self._celcius
        else:
            temp = self.c_to_f(self._celcius)

        space = self.mb_to_gb(self._space)

        print(f"Space: {space}GB, temp: {temp}.")

hd = HardDrive(800000, 22)
hd.status(metric=False)
