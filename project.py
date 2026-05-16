import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLineEdit, QPushButton,
    QMessageBox, QFormLayout, 
    QLabel, QHBoxLayout
)
class Books(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Yangi kitob qo'shish ilovasi")
        self.setFixedSize(660, 400)
        self.setStyleSheet("font-size: 25px")

        self.file_name = "books.json"

        self.init_ui()

    def init_ui(self):
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.year_input = QLineEdit()
        self.genre_input = QLineEdit()

        self.add_button = QPushButton("Qo'shish:")

        self.main_layout = QFormLayout()
        self.main_layout.addRow("Kitob nomi:", self.title_input)
        self.main_layout.addRow("Muallif:", self.author_input)
        self.main_layout.addRow("Yili:", self.year_input)
        self.main_layout.addRow("Janr:", self.genre_input)

        self.main_layout.addRow(self.add_button)

        self.setLayout(self.main_layout)
        
        self.add_button.clicked.connect(self.handle_add_book)

    def handle_add_book(self):
        title = self.title_input.text().strip()        
        author = self.author_input.text().strip()        
        year = self.year_input.text().strip()        
        genre = self.genre_input.text().strip()

        if not all([title, author, year, genre]):
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos, barcha ma'lumotlarni to'ldiring!"
            )
            return

        if not year.isdigit():
            QMessageBox.warning(
                self,
                "Xatolik",
                "Yil raqam bo'lishi kerak!"
            )
            return
        
        new_book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre
        }

        self.save_data(new_book)

    def save_data(self, data):
        books_list = []

        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as file:
                books_list = json.load(file)
        
        books_list.append(data)

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(books_list, file, indent=4, ensure_ascii=False)
            
        QMessageBox.information(self, "Muvaffaqiyat", "Kitob muvaffaqiyatli qo‘shildi!")
        self.clear_fields()
        
    def clear_fields(self):
        self.title_input.clear()
        self.author_input.clear()
        self.year_input.clear()
        self.genre_input.clear()
        self.title_input.setFocus() 
        
        

app = QApplication([])
win = Books()
win.show()
sys.exit(app.exec_())