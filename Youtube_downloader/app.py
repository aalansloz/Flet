import flet as ft
import time
import youtube
import os
from RSS import app
import pandas as pd

def main(page: ft.Page):

    #setting my page
    page.title = "Youtube Downloader"
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.padding = 40
    page.scroll = "always"


    title = ft.Text("Youtube Downloader",
			style=ft.TextThemeStyle.TITLE_LARGE)

#comprobamos si hay nuevos videos y que con una barra de progreso me diga como va el progreso y un check con playsound al finalizar
#le damos a download videos con youtube-dl y same
#otro boton para comprobar el id de un canal de youtube
#input para introducir un video
#ruta de descarga en un config.json
#Descargar solo ese video

    def check_clicked(e):
        #we enable the progress bar visibility
        progress_bar_check_videos.visible = True
        page.update()

        #ejecutar el script de Youtube-RSS


        app.main()


        #trigger the script for checking the new videos and enabling the image
        img.visible = True
        progress_bar_check_videos.visible = False


        #once the script is finished run a message to let the user know it has finished
        page.snack_bar = ft.SnackBar(ft.Text(f"Finished checking if there are new videos"))
        page.snack_bar.open = True
        page.update()

    check_button=ft.FilledButton("Check New Videos",
                                on_click=check_clicked)

    path=os.getcwd()
    img = ft.Image(
        src=f"{path}/assets/check_green.png",
        width=15,
        height=15,
        fit=ft.ImageFit.CONTAIN,
    )
    img.visible = False

    add_checks=ft.Row(
            controls=[
                check_button,
                img,
            ],alignment ="center")

    progress_bar_check_videos = ft.ProgressRing(width=16, height=16, stroke_width = 2)

    def youtube_download(e):

        import pyperclip
        #leemos el excel y copiamos cada enlace
        path = os.getcwd()
        path_full_feed=f'{path}//RSS'
        df=pd.read_csv(f'{path_full_feed}//new_videos.csv')
        #we get the second column the one from the videos
        videos = df.iloc[:, 1]

        copied_links=''
        for video in videos:
            copied_links = copied_links + f'{video}\n'
        pyperclip.copy(copied_links)


    download_button=ft.FilledButton("Download new videos",on_click=youtube_download)

    #we disable the progress bar until it is enabled by clicking the check videos button
    progress_bar_check_videos.visible = False

    tf_youtube_channel_id = ft.TextField(label="Input for getting the channel ID",
                                         value="Youtube channel to get ID")

    #get as value for here !!!!!! the input from the text value from the user
    def id_clicked(e):
        #we enable the chip to display the ID
        cp_youtube_channel_id.visible = True
        #we read the input the input
        channel_to_get_id=tf_youtube_channel_id.value
        #we update the chip for the channel asked for the user
        cp_youtube_channel_id.label.value=youtube.get_youtube_channel_ID(channel_to_get_id)
        #we update the app
        page.update() 


    bt_youtube_channel_id=ft.FilledButton("Get the ID",
                            on_click=id_clicked)


    #copiar al portapapeles el ID cuando se clike sobre el
    #y lo hacemos visible
    def chip_selected(e):
        page.update()

    cp_youtube_channel_id=ft.Chip(
                label=ft.Text(''),
                bgcolor=ft.colors.BLACK,
                disabled_color=ft.colors.GREEN_100,
                autofocus=True,
                on_select=chip_selected,
            )
    cp_youtube_channel_id.visible = False

    add_buttons=ft.Row(
            controls=[
                tf_youtube_channel_id,
				bt_youtube_channel_id,
                cp_youtube_channel_id,
            ],alignment ="center")

    def list_suscriptions(e):
        name_list.visible=True
        page.update()


    def hide_suscriptions(e):
        name_list.visible=False
        page.update()

    bt_list_suscriptions=ft.FilledButton("Show list of subscriptions",
                            on_click=list_suscriptions)

    bt_hide_suscriptions=ft.FilledButton("Hide list of subscriptions",
                            on_click=hide_suscriptions)

    add_buttons_list=ft.Row(
            controls=[
                bt_list_suscriptions,
				bt_hide_suscriptions,
            ],alignment ="center")

#añadir una nueva fuente al dataframe
# asi como añadir una opcion que me ejecute el code colab
    path = os.getcwd()
    path_full_feed=f'{path}//RSS'
    feeds_file=pd.read_excel(f'{path_full_feed}//Feeds.xls')

    name_list = ft.ListView(spacing=10, padding=20, auto_scroll=True, height=300)

    for name in feeds_file['Name']:
        name_list.controls.append(ft.Text(f"{name}"))



    name_list.visible=False

    page.add(
        title, #we define the title of the application
        add_checks,
        progress_bar_check_videos, #progress bar for checking the videos,
        download_button, #we define the counter
        add_buttons,
        add_buttons_list,
        name_list
    )


ft.app(target = main)
