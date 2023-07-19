import flet as ft
from flet import *
import time
import os
import socket

def master(page=ft.Page):
    page.title="Roscri Studio"
    page.window_center()
    page.padding=0
    page.window_center()
    # page.window_height=300
    # page.window_width=500
    page.bgcolor="#EAF4F9"
    page.window_frameless=True
    page.window_maximized=True
    page.window_minimized=False
    page.window_resizable=False
    page.update()


    # def check_on(e):
    #    home_login.visible=False
    #    loader.visible=True
    #    page.update()


    def nav1_option(e):
        nav_item_1_overview_status.visible=True
        nav_item_2_overview_status.visible=False
        nav_item_3_overview_status.visible=False
        nav_item_4_overview_status.visible=False
        overview.visible=True
        programs.visible=False
        settings.visible=False
        devices.visible=False
        e.page.update()

    def nav2_option(e):
        nav_item_2_overview_status.visible=True
        nav_item_1_overview_status.visible=False
        nav_item_3_overview_status.visible=False
        nav_item_4_overview_status.visible=False
        overview.visible=False
        programs.visible=True
        settings.visible=False
        devices.visible=False
        e.page.update()
        
    def nav3_option(e):
        nav_item_3_overview_status.visible=True
        nav_item_1_overview_status.visible=False
        nav_item_2_overview_status.visible=False
        nav_item_4_overview_status.visible=False
        overview.visible=False
        programs.visible=False
        settings.visible=True
        devices.visible=False
        e.page.update()
        
    def nav4_option(e):
        nav_item_4_overview_status.visible=True
        nav_item_1_overview_status.visible=False
        nav_item_2_overview_status.visible=False
        nav_item_3_overview_status.visible=False
        overview.visible=False
        programs.visible=False
        settings.visible=False
        devices.visible=True
        e.page.update()

    def update_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("No supported version found for beta version."))
        page.snack_bar.open = True
        page.update()

    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!"),
        action="Alright!",)
    
    sim_status=ft.Text("Activate Simulation",color="#000000",style=ft.TextThemeStyle.LABEL_LARGE)
    sim_switch=ft.Switch(value=False,active_color="0C5473",inactive_thumb_color="#559FBF",active_track_color="#F6F6F6",inactive_track_color="#FFFFFF")

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
    nav_item_6_overview=ft.Container(width=70,height=55,content=
                ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[nav_item_6_overview_icon])
                ,)
    
    sim_status=ft.Text("Activate Simulation",color="#000000",style=ft.TextThemeStyle.LABEL_LARGE)
    sim_switch=ft.Switch(value=False,active_color="0C5473",inactive_thumb_color="#559FBF",active_track_color="#F6F6F6",inactive_track_color="#FFFFFF")

    loader=ft.ProgressRing(visible=False)


    navbar=ft.Row(spacing=0,controls=[
        ft.Container(width=80,height=600,bgcolor="#0C5473",padding=padding.all(5),border_radius= ft.border_radius.all(15),content=
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

    overview=ft.Container(visible=True,width=1200,height=600,bgcolor="#FFFFFF",border_radius= ft.border_radius.all(15),content=
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
                                            
                                        ])),
                            ft.Text("Netwok Ping Status",size=15,color="#000000",style=ft.TextThemeStyle.TITLE_MEDIUM),
                            ft.Container(width=550,height=300,bgcolor="#000000")            
                            ])),
                    ft.Container(width=550,height=570,bgcolor="#000000"
                                )
            ]))

    programs=ft.Container(visible=False, width=1200,height=600,bgcolor="#FFFFFF",padding=ft.padding.all(20),border_radius= ft.border_radius.all(15),content=
                          ft.Column(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                              ft.Container(width=1190,height=90,content=
                                    ft.Row(controls=[
                                        ft.Container(width=600,height=60,content=
                                            ft.Column(spacing=2,controls=[
                                                ft.Text("Programs",size=25,color="#000000"),
                                                ft.Text("Track on live scripts",size=15,color="#000000")])
                                               ),
                                               ft.Container(width=500,height=60,content=
                                                            ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
                                                                ft.ElevatedButton("New Program", icon="add",bgcolor="#0C5473",color="#FFFFFF")
                                                            ])),
                                           ])),
                              ft.Container(width=1190,height=30,padding=padding.all(5),content=
                                           ft.Row(spacing=0,controls=[
                                               ft.Container(width=18,height=28),
                                               ft.Container(width=480,height=28,content=
                                                            ft.Text("Program Name",color="#000000",size=11)),
                                               ft.Container(width=18,height=28),
                                               ft.Container(width=270,height=28,content=
                                                            ft.Text("Date",color="#000000",size=11)),
                                               ft.Container(width=18,height=28),
                                               ft.Container(width=180,height=28,content=
                                                            ft.Text("Status",color="#000000",size=11)),
                                               ft.Container(width=18,height=28),
                                               ft.Container(width=80,height=28,content=
                                                            ft.Text("Actions",color="#000000",size=11))
                                           ])),
                              ft.Divider(height=3, thickness=1),
                              ft.Container(width=1190,height=420,padding=padding.only(left=20,top=10,right=20),content=
                                           ft.Column(controls=[
                                               ft.Container(width=1100,height=40,bgcolor="#FFFFFF",border_radius=border_radius.all(5),border=border.all(1,"#7A7A7A"),content=
                                                            ft.Row(spacing=0,controls=[
                                                                ft.Container(padding=padding.all(5),width=500,height=39,content=
                                                                            ft.Text("Program #1",color="#000000")),
                                                                ft.Container(padding=padding.all(5),width=150,height=39,content=
                                                                            ft.Text("Date",color="#000000")),
                                                                ft.Container(width=300,height=39,content=
                                                                             ft.Icon(name=ft.icons.INCOMPLETE_CIRCLE, color=ft.colors.GREEN_400, size=30)),
                                                                ft.Container(width=75,height=39,content=
                                                                             ft.Icon(name=ft.icons.REMOVE_RED_EYE_OUTLINED, color="#000000", size=20)),
                                                                ft.Container(width=75,height=39,bgcolor="#FF6C6C",content=
                                                                             ft.Icon(name=ft.icons.DELETE_SWEEP_ROUNDED, color="#FFFFFF", size=20)),
                                                            ]))]
                                                )),
                            
                          ]))
    
    settings=ft.Container(visible=False,width=1200,height=600,bgcolor="#FFFFFF",padding=ft.padding.all(20),border_radius= ft.border_radius.all(15),content=
                          ft.Column(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                              ft.Container(width=1190,height=90,content=
                                           ft.Row(controls=[
                                               ft.Container(width=600,height=60,content=
                                                   ft.Column(spacing=2,controls=[
                                                        ft.Text("Settings",size=25,color="#000000"),
                                                        ft.Text("Beta version has no support for settings",size=15,color="#FD5454")])
                                               ),
                                               ft.Container(width=500,height=60,content=
                                                            ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
                                                                ft.ElevatedButton("Check Updates", bgcolor="#0C5473",color="#FFFFFF",on_click=update_click)
                                                            ])),
                                           ])),
                              ft.Container(width=1190,height=30,bgcolor="#000000"),
                              ft.Container(width=1190,height=420,bgcolor="#000000"),
                          ]))
    
    devices=ft.Container(visible=False,width=1200,height=600,bgcolor="#FFFFFF",padding=ft.padding.all(20),border_radius= ft.border_radius.all(15),content=
                          ft.Column(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                              ft.Container(width=1190,height=90,padding=ft.padding.only(left=20),content=
                                           ft.Row(controls=[
                                               ft.Container(width=600,height=60,content=
                                                   ft.Column(spacing=2,controls=[
                                                        ft.Text("Devices",size=25,color="#000000"),
                                                        ft.Text("Connect your Extruder with live polls",size=15,color="#000000")])
                                               ),
                                               ft.Container(width=500,height=60,content=
                                                            ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
                                                                ft.ElevatedButton("Add Extruder", icon="add",bgcolor="#0C5473",color="#FFFFFF")
                                                            ])),
                                           ])),
                              ft.Container(width=1190,height=450,padding=ft.padding.only(top=0,left=20,right=20),content=
                                           ft.Row(alignment=ft.MainAxisAlignment.START,scroll = "AUTO ",wrap=True,controls=[
                                               ft.Container(width=250,height=320,bgcolor="#FFFFFF",border_radius=border_radius.all(15),padding=ft.padding.all(20),shadow=
                                                            ft.BoxShadow(spread_radius=0.5,blur_radius=7,color=ft.colors.BLUE_GREY_100,
                                                                offset=ft.Offset(0, 0),blur_style=ft.ShadowBlurStyle.OUTER,),
                                                                content=
                                                    ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[
                                                        ft.Container(width=200,height=150,image_src='C://Users//jacob//Documents//Python//Roscri-Studio//img//revo.png',image_fit=ImageFit.CONTAIN),
                                                        ft.Container(width=200,height=50,content=
                                                                     ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[
                                                                         ft.Text("revo Hemara", size=17,color="#000000"),
                                                                         ft.Switch(value=True)])),
                                                        ft.Text("Poll & simulate the Extruder with live details.", size=12,color="#000000")
                                                    ])),
                                            ])),
                          ]))
    
    title_bar=ft.Row(spacing=0,controls=[
        ft.Container(expand=0,width=100,height=40,bgcolor='#0C5473',content=ft.Icon(ft.icons.WEBHOOK_OUTLINED,color="#FFFFFF",size=25)),
        ft.Container(expand=0,width=300,padding=padding.only(left=13),height=40,bgcolor='#FFFFFF',content=
                     ft.Row(controls=[
                            sim_status,sim_switch
                            ])),
        ft.Container(expand=0,padding=padding.only(top=5,left=250),width=800,height=40, bgcolor='#FFFFFF',content=
                     ft.Text("Roscri Studio",color="#000000",style=ft.TextThemeStyle.TITLE_SMALL)),
        ft.Container(expand=0,width=120,height=40,bgcolor="#FFFFFF",padding=padding.only(left=80),content=
                     ft.Row(controls=[ft.Icon(ft.icons.VERIFIED_USER,color="#0C5473",size=18)])),
        ft.Container(expand=1,width=130,bgcolor="#FD5454",height=40, content=ft.Icon(ft.icons.WEB,color="#FFFFFF",size=18))
        
    ])

    main_dashboard=ft.Row(controls=[
        ft.Container(width=1300,height=600,bgcolor="#EAF4F9",margin=margin.only(left=30,right=25),border_radius= ft.border_radius.all(10),content=
                     ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[loader,navbar,overview,programs,settings,devices])),
    ])
    
    page.add(title_bar,main_dashboard)

ft.app(target=master,view=ft.WEB_BROWSER)