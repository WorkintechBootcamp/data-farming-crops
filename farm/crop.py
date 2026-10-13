# pylint: disable=too-few-public-methods
"""Corn ve Rice'ın ortak parent sınıfı Crop bu dosyada."""


class Crop:
    """Crop isimli ebeveyn sınıf tanımlandı. Rice ve Corn içinde kullanılacak."""

    def __init__(self):
        """Crop'un objesi oluşturuldu ve başlangıç sıfır olarak belirlendi."""
        self.grains = 0

    def ripe(self):
        """Corn ve Rice'da ortak olan Ripe metodu tanımlandı."""
        return self.grains >= 15
