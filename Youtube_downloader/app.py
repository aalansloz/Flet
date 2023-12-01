import flet as ft
import time

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


    check_button=ft.FilledButton("Check New Videos")
    download_button=ft.FilledButton("Download new videos")



    page.add(
		title, #we define the title of the application
		check_button,
        download_button #we define the counter
    )


ft.app(target = main)

