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
    def check_clicked(e):
        #we enable the progress bar visibility
        progress_bar_check_videos.visible = True

        #trigger the script for checking the new videos

        #once the script is finished run a message to let the user know it has finished
        page.snack_bar = ft.SnackBar(ft.Text(f"Finished checking if there are new videos"))
        page.snack_bar.open = True
        page.update()

    check_button=ft.FilledButton("Check New Videos",
                                on_click=check_clicked)

    download_button=ft.FilledButton("Download new videos")
    progress_bar_check_videos = ft.ProgressRing(width=16, height=16, stroke_width = 2)
    #we disable the progress bar until it is enabled by clicking the check videos button
    progress_bar_check_videos.visible = False

    page.add(
		title, #we define the title of the application
		check_button,
        download_button, #we define the counter
        progress_bar_check_videos #progress bar for checking the videos
    )


ft.app(target = main)

