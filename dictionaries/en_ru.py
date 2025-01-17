from pathlib import Path
from pystardict import Dictionary

DICTIONARIES_DIR = Path(__file__).parent.resolve() # BASE_DIR / 'dictionaries'
#DICTIONARIES_DIR.mkdir(parents=True, exist_ok=True)
eng_ru_dict = DICTIONARIES_DIR / 'eng_rus_full' / 'eng_rus_full'
DICT = Dictionary(eng_ru_dict, in_memory=True)