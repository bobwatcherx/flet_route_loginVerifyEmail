from flet import * 
from screens.dashboard import DashboardView
from screens.register import RegisterView
from screens.login import LoginView

def main(page: Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/login",
                [
                LoginView(page),
                ElevatedButton("ke dash",
                    on_click=lambda e:page.go("/dashboard")
                    )
                ],
            )
        )
        if page.route == "/register":
            page.views.append(
                View(
                    "/register",
                    [
                    RegisterView(page)
                    ],
                )
            )
        if page.route == "/dashboard":
            print(page.views[-1])
            if not page.client_storage.get("login") :
                page.go("/login")
                print(page.client_storage.get("login"))
                print(page.route)
                page.update()
            else:
                page.views.append(
                    View(
                        "/dashboard",
                        [
                        DashboardView(page)
                        ],
                    )
                )


        if page.route  == "/":
            page.go("/login")

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)