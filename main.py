import flet as ft
import flet_easy as fs

from views.article_list import article_list_page
from views.article_add import article_add_page
from views.article_read import article_read_page

app = fs.FletEasy(
    #route_init='/article/list',
    route_init = "/login",
    route_login = "/login"
)

db = ["Sasa"]  # Database

@app.login
def login_x(data: fs.Datasy):
    page = data.page
    username = page.client_storage.get("login")

    """ We check if a value exists with the key login """
    if username is not None and username in db:
        """We verify if the username that is stored in the browser
        is in the simulated database."""
        return True

    page.snack_bar = ft.SnackBar(ft.Text(f"Такого пользователя нет!"))
    page.snack_bar.open = True
    page.update()

    return False


@app.page(route="/login", title="Login")
def login_page(data: fs.Datasy):
    # create login stored user
    username = ft.TextField(label="Username")

    def store_login(e):
    #def store_login(user_name: str):
        #db.append(username.value)  # We add to the simulated database

        """First the values must be stored in the browser, then in the login
        decorator the value must be retrieved through the key used and then
        validations must be used."""
        data.login(key="login", value=username.value, next_route="/article/list")

    #store_login("sasaErm")

    return ft.View(
        controls=[
            ft.Text("login", size=30),
            username,
            ft.ElevatedButton("Login", on_click=store_login),
            #ft.ElevatedButton("Login", on_click=data.go("/article/list")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )

app.add_pages([article_list_page, article_add_page, article_read_page, ])

#app.run(view=ft.AppView.WEB_BROWSER, port=40000)
app.run()