from typing import Optional, List
import enum

from sqlmodel import Field, SQLModel, Relationship, Column, Enum
import spacy

# Загрузка модели spaCy для английского языка
nlp = spacy.load("en_core_web_sm")

def remove_punctuations(normalized_tokens):
    punctuations=['?',':','!',',','.',';','|','(',')','--']
    for word in normalized_tokens:
        if word in punctuations:
            normalized_tokens.remove(word)
    return normalized_tokens

class ArticleType(str, enum.Enum):
    Pdf = "pdf"
    Plain = "plain"
    Url = "url"


class ArticleBase(SQLModel):
    name: str
    article_type: ArticleType = Field(
        sa_column=Column(
            Enum(ArticleType),
            nullable=False,
            index=False
        ),
        default=ArticleType.Plain,
    )
    url: Optional[str] = Field(default="")
    text: Optional[str] = Field(default="")

    def fragmentize(self):
        if not self.text:
            raise ValueError("No text to fragmentize.")

        # Анализ текста
        doc = nlp(self.text)

        # Выделение предложений
        sentences = [sent.text for sent in doc.sents]

        # Вывод предложений
        # for i, sentence in enumerate(sentences):
        #     print(f"#{i}: {sentence}")

        return sentences




class Article(ArticleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fragments: List["Fragment"] = Relationship(back_populates="article", cascade_delete=True)


class FragmentBase(SQLModel):
    text: str

    def lemmatize(self):
        doc = nlp(self.text)
        lemmas = [token.lemma_ for token in doc]
        lemmas = remove_punctuations(lemmas)
        #print(lemmas)
        return lemmas


class Fragment(FragmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    article_id: int = Field(default=None, foreign_key="article.id", ondelete="CASCADE")
    article: Article = Relationship(back_populates="fragments")


class Vocab(SQLModel, table=True):
    word: str = Field(primary_key=True)

