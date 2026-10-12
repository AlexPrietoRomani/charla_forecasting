"""
Proxy de compatibilidad hacia el motor backend del deck: back/build_deck.py.
Garantiza que llamadas CI/CD o locales a `python scripts/build_deck.py` funcionen sin problemas.
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BACK_DIR = BASE_DIR / "back"

if str(BACK_DIR) not in sys.path:
    sys.path.insert(0, str(BACK_DIR))

from build_deck import build_deck

if __name__ == "__main__":
    build_deck()
