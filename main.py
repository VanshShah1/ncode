import flet as ft

def main(page: ft.Page):
    page.bgcolor="#d3d3d3"

    row1=ft.Row(controls=[
        ft.Container(content=ft.Text('helo wold'),
                         bgcolor="#2b2b2b",
                         width=620,
                         height=600),
        ft.Container(content=ft.Text('helo wold'),
                             bgcolor="black",
                             width=800,
                             height=600)
        ]       
    )
    row2=ft.Row(controls=[
        ft.Container(content=ft.Text('helo wold'),
                         bgcolor="white",
                         width=620,
                         height=300),
        ft.Container(content=ft.Text('helo wold'),
                             bgcolor="black",
                             width=800,
                             height=300)
        ]       
    )
    

    page.add(row1, row2)

ft.app(main)