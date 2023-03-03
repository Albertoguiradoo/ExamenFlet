import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"
    page.window_height=500
    page.window_width= 500
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    #---------------Función del botón---------------------
    
    def funciónbotón(e):
        if (tfnombre.value==tfpassword.value):
            page.dialog = dlg
            dlg.open = True
            page.update()
    #--------------------fin función btón--------------------------
   
    #Ejercicio 6

    #Fin --- Ejercicio 6


    #Ejercicio 2
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    #page.horizontal_alignment=ft.MainAxisAlignment.CENTER

    #Fin --- Ejercicio 3
  
    
    #Ejercicio 4
    
   #Fin --- Ejercicio 4

    

    #Ejercicio 5
    
    #Fin-- Ejercicio 5


    #------------------variables--------------------
    
    img=ft.Image(src=f"/fotos/Logo.png",width=100,height=100,fit=ft.ImageFit.CONTAIN)
    tfnombre = ft.TextField(label="Nombre",width=200,height=200,)
    tfpassword=ft.TextField(label="Contraseña",width=200,height=200, password=True, can_reveal_password=True)
    dlg = ft.AlertDialog(title=ft.Text("Contraseña Correcta"))
    btnEntrar= ft.ElevatedButton(text="Elevated button",icon="park_rounded", on_click=funciónbotón)
    
    
    
    
    page.add(img,tfnombre,tfpassword, btnEntrar,dlg)
    


ft.app(target=main,assets_dir="fotos")