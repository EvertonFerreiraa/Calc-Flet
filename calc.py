import flet as ft


class Calculadora(ft.UserControl):
    def __init__(self):
        super().__init__()

        self._numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        self._operators = ['/', '*', '-', '+']

        self.left_number = ''
        self.operator = ''
        self.right_number = ''

        self.result = ''

        self.info = ft.Text()

        self.display = ft.TextField(
            text_align=ft.TextAlign.END,
            text_size=40, disabled=True
        )

        # linha 1:
        self.button_clear = ft.ElevatedButton('C', data='C')
        self.button_backspace = ft.ElevatedButton('<', data='<')
        self.button_invert = ft.ElevatedButton('+/-', data='+/-')
        self.button_division = ft.ElevatedButton('/', data='/')

        # linha 2:
        self.button_7 = ft.ElevatedButton('7', data='7',)
        self.button_8 = ft.ElevatedButton('8', data='8',)
        self.button_9 = ft.ElevatedButton('9', data='9',)
        self.button_multiplication = ft.ElevatedButton('*', data='*')

        # linha 3:
        self.button_4 = ft.ElevatedButton('4', data='4')
        self.button_5 = ft.ElevatedButton('5', data='5')
        self.button_6 = ft.ElevatedButton('6', data='6')
        self.button_subtraction = ft.ElevatedButton('-', data='-')

        # linha 4:
        self.button_1 = ft.ElevatedButton('1', data='1')
        self.button_2 = ft.ElevatedButton('2', data='2')
        self.button_3 = ft.ElevatedButton('3', data='3')
        self.button_sum = ft.ElevatedButton('+', data='+')

        # linha 5:
        self.button_0 = ft.ElevatedButton('0', data='0', width=140)
        self.button_point = ft.ElevatedButton('.', data='.')
        self.button_equal = ft.ElevatedButton('=', data='=')

    def build(self):
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[self.info]
                    ),
                    ft.Row(
                        controls=[self.display]
                    ),
                    ft.Row(
                        controls=[
                            self.button_clear,
                            self.button_backspace,
                            self.button_invert,
                            self.button_division,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.button_7,
                            self.button_8,
                            self.button_9,
                            self.button_multiplication,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.button_4,
                            self.button_5,
                            self.button_6,
                            self.button_subtraction,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.button_1,
                            self.button_2,
                            self.button_3,
                            self.button_sum
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.button_0,
                            self.button_point,
                            self.button_equal,
                        ]
                    ),
                ]
            )
        )
