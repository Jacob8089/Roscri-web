from flet import View
import flet as ft
import time
from flet import *
import random

rand_clr=random.randint(000000,999999)


def page_nav(e):
    e.page.window_visible=False
    e.page.update()
    time.sleep(2)
    e.page.go("/home")

app_name=ft.Text("Roscri Stduio", color='#FFFFFF', style=ft.TextThemeStyle.DISPLAY_SMALL, weight=ft.FontWeight.BOLD, selectable=False)
app_desc=ft.Text("Robotic Additive Simulator", color='#FFFFFF', style=ft.TextThemeStyle.BODY_MEDIUM, selectable=False )
version_no=ft.Text("v.1.0", color='#FFFFFF', style=ft.TextThemeStyle.BODY_SMALL, selectable=False )
start_bt=ft.ElevatedButton("Get Started",color='#FFFFFF',bgcolor='#0C5473',icon=ft.icons.NAVIGATE_NEXT_ROUNDED,on_click=lambda e: page_nav(e))

#Splash Screen Design<begin>
c1= ft.Column(expand=1, controls=[
        ft.Container(expand=1, bgcolor="#0C5473",width=500, height=370,
                image_src='C://Users//jacob//Documents//Python//Roscri-Studio//img//ss.png',
                image_fit=ImageFit.CONTAIN,
            content=
                ft.Column(controls=[
                    ft.Container(height=260, width=500,padding=padding.only(top=70,left=25),content=
                        ft.Column(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls=[app_name,app_desc]),),
                                ft.Container(height=90, width=500,padding=padding.only(left=25),content=
                                        ft.Column(expand=True, alignment=ft.MainAxisAlignment.START, controls=[start_bt]),)
                    ]))
])

def _view_():
    return ft.View(
        "splash",spacing=0,padding=0,bgcolor="#0C5473",
        controls=[c1])