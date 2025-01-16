import pytest
from models import FragmentBase, Fragment

test_text = "Every day I has three or four classes, so I did not usually have much time for meals."


def test_fragment_creation():
    frag = FragmentBase(
        text = "Test"
    )

    assert frag.text == "Test"

def test_lemmatize():
    frag = FragmentBase(
        text=test_text
    )
    lemmas = frag.lemmatize()
    assert len(lemmas) == 18