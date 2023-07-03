import flet as ft

from calc import Calculadora


def main(page: ft.Page):
    page.title = 'Calculadora-python'
    page.window_width = 350
    page.window_height = 550

    def button_clicked(e):
        data = e.control.data

        if data in app._numbers:
            app.display.value = app.display.value + data

        if data in app._operators and app.left_number == '':
            app.left_number = app.display.value
            app.operator = data
            app.display.value = ''
            app.info.value = f'{app.left_number} {app.operator} ? = ?'

        if data == '=' and app.right_number == '':
            app.right_number = app.display.value
            app.result = eval(
                f'{app.left_number}{app.operator}{app.right_number}'
            )
            app.info.value = (f'{app.left_number} '
                              f'{app.operator} {app.right_number} '
                              f'= {app.result}'
                              )
            app.display.value = str(app.result)

        if data in app._operators and app.result != '':
            app.left_number = app.result
            app.operator = data
            app.right_number = ''
            app.result = ''
            app.display.value = ''
            app.info.value = f'{app.left_number} {app.operator} ? = ?'

        if data == 'C':
            app.display.value = ''
            app.info.value = ''
            app.left_number = ''
            app.right_number = ''
            app.result = ''

        if data == '<':
            app.display.value = app.display.value[:-1]

        if data == '+/-':
            n = float(app.display.value).is_integer()
            if n:
                app.display.value = str(-int(app.display.value))
            else:
                app.display.value = str(-float(app.display.value))

        page.update(app)

    app = Calculadora()
    app.button_0.on_click = button_clicked
    app.button_1.on_click = button_clicked
    app.button_2.on_click = button_clicked
    app.button_3.on_click = button_clicked
    app.button_4.on_click = button_clicked
    app.button_5.on_click = button_clicked
    app.button_6.on_click = button_clicked
    app.button_7.on_click = button_clicked
    app.button_8.on_click = button_clicked
    app.button_9.on_click = button_clicked
    app.button_point.on_click = button_clicked
    app.button_clear.on_click = button_clicked
    app.button_backspace.on_click = button_clicked
    app.button_invert.on_click = button_clicked
    app.button_division.on_click = button_clicked
    app.button_multiplication.on_click = button_clicked
    app.button_subtraction.on_click = button_clicked
    app.button_sum.on_click = button_clicked
    app.button_equal.on_click = button_clicked
    app.button_0.on_click = button_clicked

    page.add(app)


ft.app(target=main)
