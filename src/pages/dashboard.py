import flet as ft
from flet import *
import random
import time
import socket
import logging

logging.basicConfig(filename="C:/Users/jacob/Documents/Python/Roscri-Studio/logs/rs-dashboard_ui.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

rand_clr=random.randint(000000,999999)


def page_nav(e):
    e.page.go("/home")

host_name=ft.Text(socket.gethostname(),color="#FFFFFF",size=25,style=ft.TextThemeStyle.TITLE_MEDIUM)

def sw_status(e):
    if(sim_switch.value==True):
        sim_status.value="Simulation Activated"
        e.page.update()
    else:
        page_nav(e)
        sim_status.value="Activate Simulation"
        e.page.update()

def nav1_option(e):
    nav_item_1_overview_status.visible=True
    nav_item_2_overview_status.visible=False
    nav_item_3_overview_status.visible=False
    nav_item_4_overview_status.visible=False
    e.page.update()

def nav2_option(e):
    nav_item_2_overview_status.visible=True
    nav_item_1_overview_status.visible=False
    nav_item_3_overview_status.visible=False
    nav_item_4_overview_status.visible=False
    e.page.update()
    
def nav3_option(e):
    nav_item_3_overview_status.visible=True
    nav_item_1_overview_status.visible=False
    nav_item_2_overview_status.visible=False
    nav_item_4_overview_status.visible=False
    e.page.update()
    
def nav4_option(e):
    nav_item_4_overview_status.visible=True
    nav_item_1_overview_status.visible=False
    nav_item_2_overview_status.visible=False
    nav_item_3_overview_status.visible=False
    e.page.update()


sim_status=ft.Text("Activate Simulation",color="#000000",style=ft.TextThemeStyle.LABEL_LARGE)
sim_switch=ft.Switch(value=False,active_color="0C5473",inactive_thumb_color="#559FBF",active_track_color="#F6F6F6",inactive_track_color="#FFFFFF",on_change=lambda e:sw_status(e))

nav_item_1_overview_icon=ft.Icon(ft.icons.HOME_ROUNDED,color="#FFFFFF",size=28)
nav_item_1_overview_text=ft.Text("Overview",size=11)
nav_item_1_overview_text_con=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_1_overview_text])
nav_item_1_overview_status=ft.Container(height=45,width=3,bgcolor="#FFFFFF",visible=True)
nav_item_1_overview=ft.Container(width=70,height=55,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_1_overview_icon,nav_item_1_overview_status]),
            on_click=lambda e:nav1_option(e))

nav_item_2_overview_icon=ft.Icon(ft.icons.DEVICES_FOLD_ROUNDED,color="#EBEBEB",size=20)
nav_item_2_overview_text=ft.Text("Program",size=11)
nav_item_2_overview_text_con=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_2_overview_text])
nav_item_2_overview_status=ft.Container(height=45,width=3,bgcolor="#FFFFFF",visible=False)
nav_item_2_overview=ft.Container(width=70,height=55,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_2_overview_icon,nav_item_2_overview_status])
            ,on_click=lambda e:nav2_option(e))

nav_item_3_overview_icon=ft.Icon(ft.icons.SETTINGS_SHARP,color="#EBEBEB",size=20)
nav_item_3_overview_text=ft.Text("Settings",size=11)
nav_item_3_overview_text_con=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_3_overview_text])
nav_item_3_overview_status=ft.Container(height=45,width=3,bgcolor="#FFFFFF",visible=False)
nav_item_3_overview=ft.Container(width=70,height=55,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_3_overview_icon,nav_item_3_overview_status])
            ,on_click=lambda e:nav3_option(e))

nav_item_4_overview_icon=ft.Icon(ft.icons.DEVICES_OUTLINED,color="#EBEBEB",size=20)
nav_item_4_overview_text=ft.Text("Devices",size=11)
nav_item_4_overview_text_con=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_4_overview_text])
nav_item_4_overview_status=ft.Container(height=45,width=3,bgcolor="#FFFFFF",visible=False)
nav_item_4_overview=ft.Container(width=70,height=55,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_4_overview_icon,nav_item_4_overview_status])
            ,on_click=lambda e:nav4_option(e))

nav_item_5_overview_img=ft.Image(src="C://Users//jacob//Documents//Python//Roscri-Studio//img//group.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)
nav_item_5_overview=ft.Container(width=70,height=65,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_5_overview_img]),on_click=lambda e:nav4_option())

nav_item_6_overview_icon=ft.Icon(ft.icons.SUPPORT_AGENT_SHARP,color="#EBEBEB",size=20)
nav_item_6_overview=ft.Container(width=70,height=70,content=
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[
                ft.Container(width=50,height=45,content=
                                ft.Column(controls=[nav_item_6_overview_icon,])),
            ]),on_click=lambda e:nav4_option())


navbar=ft.Row(spacing=0,controls=[
        ft.Container(width=80,height=620,bgcolor="#0C5473",padding=padding.all(5),border_radius= ft.border_radius.all(15),content=
            ft.Column(controls=[
                ft.Container(width=70,height=20,bgcolor="#0C5473"),
                nav_item_1_overview,
                nav_item_1_overview_text_con,
                nav_item_2_overview,
                nav_item_2_overview_text_con,
                nav_item_3_overview,
                nav_item_3_overview_text_con,
                nav_item_4_overview,
                nav_item_4_overview_text_con,
                ft.Container(width=70,height=55,bgcolor="#0C5473"),
                nav_item_5_overview,
                nav_item_6_overview,
            ]))
])

overview=ft.Container(width=1200,height=620,bgcolor="#FFFFFF",border_radius= ft.border_radius.all(15),content=
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                    ft.Container(width=550,height=600,content=
                        ft.Column(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                            ft.Container(padding=ft.padding.all(15),width=550,height=220,border_radius=ft.border_radius.all(15),
                                        gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=Alignment(0.8, 1),
                                        colors=[
                                            "0xff0C5473",
                                            "0xff6695A9",],
                                        tile_mode=ft.GradientTileMode.MIRROR),content=
                                        ft.Column(controls=[
                                            ft.Text("Hey there.",color="#FFFFFF",size=13,style=ft.TextThemeStyle.TITLE_MEDIUM),
                                            host_name
                                        ])),
                            ft.Text("Netwok Ping Status",size=15,color="#000000",style=ft.TextThemeStyle.TITLE_MEDIUM),
                            ft.Container(width=550,height=300,bgcolor="#000000")            
                            ])),
                    ft.Container(width=550,height=570,bgcolor="#000000"
                                )
            ]))
loader=ft.ProgressRing()

title_bar=ft.Row(spacing=0,controls=[
    ft.Container(expand=0,width=100,height=40,bgcolor='#0C5473'),
    ft.Container(expand=0,width=300,padding=padding.only(left=13),height=40,bgcolor='#FFFFFF',content=
                    ft.Row(controls=[
                        sim_status,sim_switch
                        ])),
    ft.Container(expand=0,padding=padding.only(top=5,left=250),width=800,height=40, bgcolor='#FFFFFF',content=
                    ft.Text("Roscri Studio",color="#000000",style=ft.TextThemeStyle.TITLE_SMALL),),
    ft.Container(expand=0,width=120,height=40,bgcolor="#FFFFFF",padding=padding.only(left=80),content=
                    ft.Row(controls=[ft.Icon(ft.icons.CLOSE_FULLSCREEN_OUTLINED,color="#0C5473",size=18)])),
    ft.Container(expand=1,width=130,bgcolor="#FD5454",height=40,image_src='C://Users//jacob//Documents//Python//Roscri-Studio//img//Exit.png',on_click=lambda e: e.page.window_destroy())
    
])

main_dashboard=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[
    ft.Container(width=1300,height=670,bgcolor="#EAF4F9",margin=margin.only(left=30,right=25),border_radius= ft.border_radius.all(10),content=
                    ft.Row(controls=[navbar,overview,loader])),
])


def _view_():
    return ft.View(
        "/dashboard",spacing=0,padding=0,bgcolor="#EAF4F9",
        controls=[title_bar,main_dashboard])