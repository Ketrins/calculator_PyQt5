from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
import sys

# Екземпляр класу вікна
app = QApplication(sys.argv)

# Найголовніше вікно
window = QWidget()
window.setWindowTitle('Калькулятор')
window.setStyleSheet('background-color: #282a36; color: #f8f8f2; font-size: 16px')

# Визначення QLineEdit для відображення
line_edit = QLineEdit()

# Виконуємо операцію, коли натиснуто кнопку
def on_operation_click(text):
    line_edit.setText(line_edit.text() + ' ' + text + ' ')

# Обчислюємо вираз
def on_equals_click():
    try:
        line_edit.setText(str(eval(line_edit.text())))
    except Exception as e:
        line_edit.setText('Error')

# Очищуємо запис
def clear_entry():
    line_edit.clear()

# Кнопки та їхні відповідні стилі
button_texts = [
    ('7', '#6272a4'), ('8', '#6272a4'), ('9', '#6272a4'), ('+', '#8be9fd'),
    ('4', '#6272a4'), ('5', '#6272a4'), ('6', '#6272a4'), ('-', '#8be9fd'),
    ('1', '#6272a4'), ('2', '#6272a4'), ('3', '#6272a4'), ('*', '#8be9fd'),
    ('0', '#6272a4'), ('.', '#6272a4'), ('/', '#8be9fd')
]

# Налаштування стилів кнопок і їх підключення
v_layout = QVBoxLayout()
for i in range(0, len(button_texts), 4):
    h_layout = QHBoxLayout()
    for text, bg_color in button_texts[i:i + 4]:
        button = QPushButton(text)
        button.setStyleSheet(f'background-color: {bg_color}; color: #f8f8f2; font-size: 16px;')
        if text in {'+', '-', '*', '/'}:
            button.clicked.connect(lambda _, text=text: on_operation_click(text))
        else:
            button.clicked.connect(lambda _, text=text: line_edit.setText(line_edit.text() + text))
        button.setFixedHeight(50)
        h_layout.addWidget(button)
    v_layout.addLayout(h_layout)

# Створення макету для кнопок Clear і Equals
buttons_layout = QHBoxLayout()
button_delete = QPushButton('CE')
button_delete.setStyleSheet('background-color: #ff5555; color: #f8f8f2; font-size: 16px;')
button_delete.clicked.connect(clear_entry)
buttons_layout.addWidget(button_delete)
button_equals = QPushButton('=')
button_equals.setStyleSheet('background-color: #50fa7b; color: #f8f8f2; font-size: 16px;')
button_equals.clicked.connect(on_equals_click)
buttons_layout.addWidget(button_equals)

# Установлення макету для головного вікна та відображення його
main_layout = QVBoxLayout()
main_layout.addWidget(line_edit)
main_layout.addLayout(v_layout)
main_layout.addLayout(buttons_layout)
window.setLayout(main_layout)
window.show()

# Входження в основний цикл програми
sys.exit(app.exec_())
