import sys
import json
import os
# PyQt5 kutubxonasidan kerakli modullarni import qilamiz
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

class BookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.file_name = "books.json"
        self.init_ui()

    def init_ui(self):
        # Oyna sozlamalari
        self.setWindowTitle("Yangi kitob qo'shish ilovasi (PyQt5)")
        self.setFixedSize(450, 320)
        
        # Form Layout yaratish
        self.layout = QFormLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(30, 30, 30, 30)

        # Input (kiritish) maydonlarini yaratish
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.year_input = QLineEdit()
        self.genre_input = QLineEdit()

        # Maydonlarga yordamchi matnlar qo'shish
        self.year_input.setPlaceholderText("Faqat raqam (masalan: 1926)")

        # Formaga qatorlarni qo'shish (Label va Input juftligi)
        self.layout.addRow("Kitob nomi:", self.title_input)
        self.layout.addRow("Muallif:", self.author_input)
        self.layout.addRow("Yili:", self.year_input)
        self.layout.addRow("Janr:", self.genre_input)

        # "Qo'shish" tugmasi
        self.add_button = QPushButton("Qo'shish")
        self.add_button.setFixedHeight(40)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.add_button.clicked.connect(self.handle_add_book)
        
        # Tugmani formaga qo'shish
        self.layout.addRow(self.add_button)

        self.setLayout(self.layout)

    def handle_add_book(self):
        # Ma'lumotlarni yig'ish
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        year_str = self.year_input.text().strip()
        genre = self.genre_input.text().strip()

        # 1. Bo'sh maydonlarni tekshirish
        if not (title and author and year_str and genre):
            QMessageBox.warning(self, "Diqqat", "Iltimos, barcha ma’lumotlarni to‘ldiring!")
            return

        # 2. Yilni raqam ekanligini tekshirish
        if not year_str.isdigit():
            QMessageBox.warning(self, "Xato", "Yil maydoniga faqat raqam kiriting!")
            return

        # Yangi kitob lug'ati
        new_book = {
            "title": title,
            "author": author,
            "year": int(year_str),
            "genre": genre
        }

        # 3. Faylga yozish jarayoni
        self.save_data(new_book)

    def save_data(self, data):
        books_list = []
        
        # Fayl mavjudligini tekshirish va o'qish
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    books_list = json.load(file)
            except (json.JSONDecodeError, ValueError):
                books_list = []

        # Yangi ma'lumotni ro'yxatga qo'shish
        books_list.append(data)

        # JSON faylga qayta saqlash
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(books_list, file, indent=4, ensure_ascii=False)
            
            QMessageBox.information(self, "Muvaffaqiyat", "Kitob muvaffaqiyatli qo‘shildi!")
            self.clear_fields()
        except Exception as e:
            QMessageBox.critical(self, "Tizim xatosi", f"Faylga yozishda muammo: {e}")

    def clear_fields(self):
        """Kiritish maydonlarini tozalash"""
        self.title_input.clear()
        self.author_input.clear()
        self.year_input.clear()
        self.genre_input.clear()
        self.title_input.setFocus() # Kursorni birinchi maydonga qaytarish

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookApp()
    window.show()
    sys.exit(app.exec_())