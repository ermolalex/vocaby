import flet as ft
import flet_easy as fs

from sqlmodel import  Session
from db import db

from models import Article

articles = fs.AddPagesy()


# We add a page
@articles.page(route="/home", title="Home")
def index_page(data: fs.Datasy):
    page = data.page
    view = data.view

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    session = Session(db.engine)

    def func1(e):
        control = e.control
        id = int(control.data)
        #page.update()

        print(control.text, control.data, lv.controls[id])


    def create_card(r: Article):
        card = ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(f"{r.name} {id}"),
                            subtitle=ft.Text("Here is a second title."),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(
                                        text="Item 1",
                                        on_click=func1,
                                        data=id,
                                    ),
                                    ft.PopupMenuItem(text="Item 2"),
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
    for r in articles:
        print(r)
        lv.controls.append(create_card(r))

    def add_pressed(e):
        # page.dialog = dlg_modal
        # dlg_modal.open = True
        # page.update()
        print("Add pressed")
        data.go("/new_article")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=add_pressed,
        bgcolor=ft.colors.LIME_300
    )


    return ft.View(
        controls=[
            lv,
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.appbar,
    )
