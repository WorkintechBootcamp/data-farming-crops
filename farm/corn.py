"""Corn için belirlenmiş özel metotlar tanımlandı.
Corn ve Rice metotları belirlenen Crop sınıfı import edildi."""
from farm.crop import Crop


class Corn(Crop):
    """Corn sınıfına özgü metotlar Crop'a bağlı olan classta tanımlandı."""

    def water(self):
        """Corn'a özgü sulama metodu tanımlandı. Bu metot grain'i 10 arttırıyor."""
        self.grains += 10
