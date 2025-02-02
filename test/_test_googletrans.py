import pytest
import asyncio
from googletrans import Translator

test_text = "Every day I has three or four classes"


# def test_result_is_str():
#     trans = Translator()
#     res = trans.translate(
#         test_text,
#         dest='ru',
#         src='en'
#     )
#
#     print(res)
#     assert len(str(res.text)) > 0


def translate(text: str) -> str:
    async def async_translate_text():
        async with Translator() as translator:
            result = await translator.translate(text, src='en', dest='ru')
        return result

    res = asyncio.run(async_translate_text())
    return res.text


if __name__ == '__main__':
    print(translate(test_text))


        # print(result)  # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
        # result = await translator.translate('안녕하세요.', dest='ja')
        # print(result)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
        # result = await translator.translate('veritas lux mea', src='la')
        # print(result)  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
