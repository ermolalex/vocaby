import flet as ft
import flet_easy as fs

from sqlmodel import  Session
from db import db

from models import Article

article_list_page = fs.AddPagesy(
    route_prefix='/article'
)

@article_list_page.page(route='/list', title='List')
def article_list(data:fs.Datasy):
    page = data.page
    session = Session(db.engine)

    appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.SORT_BY_ALPHA),
        leading_width=40,
        title=ft.Text("Список"),
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

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def read_article(e):
        control = e.control
        id = int(control.data)
        page.go((f'{article_list_page.route_prefix}/read/{id}'))

    def delete_article(e):
        control = e.control
        id = int(control.data)
        db.delete_article(id, session)


    def create_card(article: Article):
        card = ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(f"{article.name} {id}"),
                            subtitle=ft.Text("Первые ххх слов."),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(
                                        text="Читать",
                                        on_click=read_article,
                                        data=article.id,
                                    ),
                                    ft.PopupMenuItem(
                                        text="Удалить",
                                        on_click=delete_article,
                                        data=article.id
                                    ),
                                ],
                            ),
                        ),
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=2),
            )
        )

        return card

    articles = db.get_article_list(session)

    print(f'Найдено {len(articles)} текстов...')
    for article in articles:
        #print(article)
        lv.controls.append(create_card(article))

    return ft.View(
        controls=[
            lv,
            ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                on_click=data.go(f'{article_list_page.route_prefix}/add'),
                bgcolor=ft.colors.LIME_300
            )
        ],
        appbar=appbar,
        vertical_alignment = "center",
        horizontal_alignment = "center",
    )


# page.appbar = ft.AppBar(
#         leading=ft.Icon(ft.Icons.PALETTE),
#         leading_width=40,
#         title=ft.Text("AppBar Example"),
#         center_title=False,
#         bgcolor=ft.Colors.SURFACE_VARIANT,
#         actions=[
#             ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
#             ft.IconButton(ft.Icons.FILTER_3),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text="Item 1"),
#                     ft.PopupMenuItem(),  # divider
#                     ft.PopupMenuItem(
#                         text="Checked item", checked=False, on_click=check_item_clicked
#                     ),
#                 ]
#             ),
#         ],
#     )