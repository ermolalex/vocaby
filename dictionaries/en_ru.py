import asyncio
from pathlib import Path
import enum

from pystardict import Dictionary
from googletrans import Translator

DICTIONARIES_DIR = Path(__file__).parent.resolve() # BASE_DIR / 'dictionaries'
#DICTIONARIES_DIR.mkdir(parents=True, exist_ok=True)
eng_ru_full = DICTIONARIES_DIR / 'eng_rus_full' / 'eng_rus_full'
DICT_EN_RU_FULL = Dictionary(eng_ru_full, in_memory=True)


class TranslationMethod(int, enum.Enum):
    FullDict = 1
    GoogleTrans = 2

def google_translate(text: str) -> str:
    async def async_translate_text():
        async with Translator() as translator:
            result = await translator.translate(text, src='en', dest='ru')
        return result

    res = asyncio.run(async_translate_text())
    return res.text


def get_word_translation(text: str, method: int) -> str:
    result = ''
    if method == TranslationMethod.FullDict:
        result = DICT_EN_RU_FULL[text]
    elif method == TranslationMethod.GoogleTrans:
        result = google_translate(text)

    return result