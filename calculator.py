from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
import sys

# Створюємо екземпляр програми
app = QApplication(sys.argv)

# Ініціалізація головного вікна
window = QWidget()
window.setWindowTitle('Калькулятор')
window.setStyleSheet('background-color: #282a36; color: #f8f8f2; font-size: 16px')

# Визначаємо QLineEdit для відображення
line_edit = QLineEdit()

# Виконаємо операцію, коли натиснуто кнопку
def on_operation_click(text):
    line_edit.setText(line_edit.text() + ' ' + text + ' ')

# Обчислюємо вираз
def on_equals_click():
    try:
        line_text = line_edit.text()
        line_text = line_text.replace('^', '**')  # Replace ^ with ** for exponentiation
        result = str(eval(line_text))
        line_edit.setText(result)
    except Exception as e:
        line_edit.setText('Error')

# Очищуємо запис
def clear_entry():
    line_edit.clear()

# Функція піднесення до степеня
def on_exponentiation():
    line_edit.setText(line_edit.text() + ' ^ ')

# Кнопки та їхні відповідні стилі
button_texts = [
    ('7', '#6272a4'), ('8', '#6272a4'), ('9', '#6272a4'), ('+', '#8be9fd'),
    ('4', '#6272a4'), ('5', '#6272a4'), ('6', '#6272a4'), ('-', '#8be9fd'),
    ('1', '#6272a4'), ('2', '#6272a4'), ('3', '#6272a4'), ('*', '#8be9fd'),
    ('0', '#6272a4'), ('.', '#6272a4'), ('/', '#8be9fd'), ('^', '#ffb86c')  # Exponentiation button
]

# Налаштування стилів кнопок і підключення
v_layout = QVBoxLayout()
for i in range(0, len(button_texts), 4):
    h_layout = QHBoxLayout()
    for text, bg_color in button_texts[i:i + 4]:
        button = QPushButton(text)
        button.setStyleSheet(f'background-color: {bg_color}; color: #f8f8f2; font-size: 16px;')
        if text in {'+', '-', '*', '/'}:
            button.clicked.connect(lambda _, text=text: on_operation_click(text))
        elif text == '^':
            button.clicked.connect(on_exponentiation)  # Connect the exponentiation function
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
