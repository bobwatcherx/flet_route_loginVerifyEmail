from flet import *

def DashboardView(page):


    # if page.client_storage.get("login") is  None or page.client_storage.get("login") == '':
    #     page.go("/login")
    #     print(page.client_storage.get("login"))
    #     print(page.route)
    #     page.update()
    # else:
    #     page.go("/dashboard")
    #     page.update()

    def logoutnow(e):
        page.client_storage.remove("login")
        page.go("/login")
        print(page.route)
        page.update()

    def backtologin(e):
    	if page.client_storage.get("login") is not None:
    		page.go("/dashboard")
    		page.snack_bar =  SnackBar(
    			Text("You cannot Back TO login Again before logout",
    				size=30
    				)
    			)
    		page.snack_bar.open = True

    	else:
    		page.go("/login")
    	page.update()



    return Column(
        controls=[
            Text("You are in Dashboard", size=30, weight="bold"),
            ElevatedButton("Logout",
                bgcolor="red", color="white",
                on_click=logoutnow
            ),
            ElevatedButton("test ",
                bgcolor="red", color="white",
                on_click=backtologin
            )

        ]
    )
