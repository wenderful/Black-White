class Temparature:
    def __init__(self):
        self._temp_fahr = 0
    @property
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9
    @temp.setter
    def temp(self,new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32