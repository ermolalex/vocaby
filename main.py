import flet as ft
import flet_easy as fs

from views.article_list import article_list_page
from views.article_add import article_add_page
from views.article_read import article_read_page

app = fs.FletEasy(
    route_init='/article/list'
)

app.add_pages([article_list_page, article_add_page, article_read_page])

#app.run(view=ft.AppView.WEB_BROWSER, port=40000)
app.run()