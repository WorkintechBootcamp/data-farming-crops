"""Rice için belirlenmiş özel metotlar tanımlandı.
Corn ve Rice metotları belirlenen Crop sınıfı import edildi."""
from farm.crop import Crop


class Rice(Crop):
    """Rice sınıfına özgü metotlar Crop'a bağlı olan classta tanımlandı."""

    def water(self):
        """Rice'a özgü sulama metodu tanımlandı. Bu metot grain'i 5 arttırıyor."""
        self.grains += 5

    def transplant(self):
        """Rice'a özgü transplant metodu tanımlandı. Bu metot grain'i 10 arttırıyor."""
        self.grains += 10
