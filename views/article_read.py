import flet
import flet as ft
import flet_easy as fs
from sqlmodel import  Session

from db import db
from models import Fragment
from dictionaries.en_ru import get_word_translation, TranslationMethod

article_read_page = fs.AddPagesy(
    route_prefix='/article'
)


@article_read_page.page(route='/read/{id:int}', title='Read')
def read_article(data:fs.Datasy, id: int):
    page = data.page

    appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            icon_size=30,
            on_click=data.go_back()
        ),
        leading_width=40,
        title=ft.Text(f"Чтение {id}"),
        center_title=False,
        bgcolor=ft.Colors.BLUE_200,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Item 2"),
                ]
            ),
        ],
    )

    lv = ft.ListView(expand=1, spacing=5, padding=5, auto_scroll=False)
    session = Session(db.engine)

    def create_fragment_card(fragment: Fragment):
        trans =  ft.Text(
                    '',
                    expand=True,
                    selectable=True,
                    bgcolor=flet.Colors.AMBER_200
                )

        trans_col = ft.Column(
            [
                trans
            ],
            expand=True,
            visible=False,
        )

        def show_trans(e):
            if trans_col.visible:
                trans_col.visible = False
            else:
                control = e.control
                text = str(control.data['word'])
                method = int(control.data['method'])
                trans.value = get_word_translation(text, method)
                trans_col.visible = True
            page.update()

        card = ft.Card(
            color=ft.Colors.AMBER_300,
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.Row([
                            ft.Text(
                                fragment.text,
                                expand=True,
                                selectable=True,
                            ),
                            ft.IconButton(
                                ft.Icons.ARROW_FORWARD,
                                icon_size=20,
                                on_click=show_trans,
                                data={
                                    "word": fragment.text,
                                    "method": TranslationMethod.GoogleTrans,
                                }
                            ),
                            # ft.PopupMenuButton(
                            #     icon=ft.Icons.MORE_VERT,
                            #     items=[
                            #         ft.PopupMenuItem(
                            #             text="Item 1",
                            #         ),
                            #         ft.PopupMenuItem(text="Item 2"),
                            #     ],
                            # ),
                        ]),
                        trans_col,
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=2),
            )
        )

        return card

    def create_word_card(word: str):
        trans =  ft.Text(
                    '',
                    expand=True,
                    selectable=True
                )

        trans_col = ft.Column(
            [
                trans
            ],
            expand=True,
            visible=False,
            height=300,
        )

        def show_trans(e):
            #if translation_row.visible:
            #translation_row.visible = not translation_row.visible
            if trans_col.visible:
                trans_col.visible = False
            else:
                control = e.control
                word = str(control.data['word'])
                method = int(control.data['method'])
                word = word.lower()
                trans.value = get_word_translation(word, method)
                trans_col.visible = True
            page.update()

        def add_to_vocab(e):
            control = e.control
            word = str(control.data)
            db.add_vocab(word, session)
            card.visible = False
            page.update()

        card = ft.Card(
            color=ft.Colors.AMBER_100,
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.Row([
                            ft.Text(
                                word,
                                expand=True,
                                # weight=ft.FontWeight.W_900,
                                # size=14
                            ),
                            ft.IconButton(
                                ft.Icons.ARROW_FORWARD,
                                icon_size=20,
                                on_click=show_trans,
                                data={
                                    "word": word,
                                    "method": TranslationMethod.FullDict,
                                }
                            ),
                            ft.IconButton(
                                ft.Icons.ADD,
                                icon_size=20,
                                on_click=add_to_vocab,
                                data=word
                            ),
                            ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(
                                        text="Google",
                                        on_click=show_trans,
                                        data={
                                            "word": word,
                                            "method": TranslationMethod.GoogleTrans,
                                        }
                                    ),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ]),
                        #translation_row
                        trans_col,
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=2),
            )
        )

        return card



    fragments = db.get_fragments(id, session)

    print(f'Найдено {len(fragments)} фрагментов...')
    for fragment in fragments:
        #print(article)
        lv.controls.append(create_fragment_card(fragment))

        words = fragment.lemmatize()
        for word in words:
            if (
                len(word) < 3 or
                db.in_vocab(word, session)
            ) :
                continue
            lv.controls.append(create_word_card(word))


    return ft.View(
        controls=[
            lv,
        ],
        appbar=appbar,
        vertical_alignment = "center",
        horizontal_alignment = "center",
    )
