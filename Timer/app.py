import flet as ft
import tiempo
import time

def main(page: ft.Page):

	#setting my page
	page.title = "Expenses Tracker"
	page.theme_mode = "dark"
	page.horizontal_alignment = "center"
	page.padding = 40
	page.scroll = "always"

	timer_on =False

	title = ft.Text("Timer",
			style=ft.TextThemeStyle.TITLE_LARGE)

	timer=ft.Text(
            "00:25:00",
            size=120,
			weight=ft.FontWeight.W_800,
			color=ft.colors.BLUE,
            )

	def descontar_horas(contador):

		while contador.hours > 0 or contador.minutes > 0:

			if contador.hours > 0:
				contador.hours -= 1
				contador.minutes = 60
			elif contador.seconds != 0:
				pass
			else:
				contador.minutes -= 1
				contador.seconds +=60
			while contador.seconds !=0:
				global timer_on
				global reset_on
				if timer_on:
					time.sleep(1)
					contador.seconds -=1
					timer.value=f'{contador.hours}:{contador.minutes}:{contador.seconds}'
					page.update()


				else:
					break

	def start(e):
		global timer_on
		timer_on =True
		if timer.value == "00:25:00":
			Tiempo=tiempo.Tiempo(0,25,0)
		else:
			horas, minutos, segundos = timer.value.split(":")
			Tiempo=tiempo.Tiempo(int(horas),int(minutos),int(segundos))


		descontar_horas(Tiempo)

	def stop(e):
		global timer_on
		timer_on =False

	def reset(e):
		pass
	

	start=ft.IconButton(
                    icon=ft.icons.START,
                    icon_color="green600",
                    icon_size=60,
                    tooltip="Start",
					on_click=start
                )
	stop=ft.IconButton(
                    icon=ft.icons.STOP,
                    icon_color="green600",
                    icon_size=60,
                    tooltip="Stop",
					on_click=stop
                )
	reset=ft.IconButton(
                    icon=ft.icons.RESTART_ALT,
                    icon_color="green600",
                    icon_size=60,
                    tooltip="Reset",
					on_click=reset
                )


	add_buttons=ft.Row(
            controls=[
                start,
				stop,
				reset,
            ],alignment ="center")

	page.add(
		title, #we define the title of the application
		timer, #we define the counter
		add_buttons, #we add the buttons below the timer
		)


ft.app(target = main)



