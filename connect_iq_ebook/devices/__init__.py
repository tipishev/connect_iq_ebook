from .fenix5 import Fenix5
from .fenix5s import Fenix5S

# convention: names should match ebook/manifest.xml
fenix5 = Fenix5()
fenix5s = Fenix5S()

__all__ = [
    fenix5,
    fenix5s,
]
