import flet as ft
import flet_easy as fs

new_article = fs.AddPagesy()


# We add a second page
@new_article.page(route="/new_article", title="Counter")
def new_article_page(data: fs.Datasy):
    page = data.page
    view = data.view

    def plus_click(e):
        print("Plus clicked")
        #page.update()

    return ft.View(
        controls=[
            ft.Text("Counter page", size=30),
            ft.Row(
                [
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )
