import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QLabel, QComboBox, QLineEdit, QTextEdit, QMessageBox, QProgressBar
from PyQt6.QtGui import QIcon, QFont, QPalette, QColor, QLinearGradient, QBrush
from PyQt6.QtCore import Qt
import string
import secrets

# Apply a modern style to the application
def apply_modern_style(app):
    app.setStyle('Fusion')
    palette = QPalette()
    gradient = QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QColor(53, 53, 53))
    gradient.setColorAt(1.0, QColor(25, 25, 25))
    palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
    app.setPalette(palette)

# Modify the PasswordGeneratorApp class
class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon('logo.png'))  # Set window icon
        self.setFixedSize(500, 600)  # Set fixed size for the window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.mode_label = QLabel("Select Mode:")
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Generative", "Customized"])
        self.mode_combo.currentTextChanged.connect(self.show_mode_frame)

        self.layout.addWidget(self.mode_label)
        self.layout.addWidget(self.mode_combo)

        self.generative_frame = GenerativePasswordFrame()
        self.customized_frame = CustomizedPasswordFrame()

        self.layout.addWidget(self.generative_frame)
        self.layout.addWidget(self.customized_frame)

        self.show_mode_frame()

        self.copy_right_label = QLabel("© 2024 Developed by Sathsara Karunarathne")
        self.layout.addWidget(self.copy_right_label)

    def show_mode_frame(self):
        mode = self.mode_combo.currentText()
        if mode == "Generative":
            self.generative_frame.show()
            self.customized_frame.hide()
        elif mode == "Customized":
            self.customized_frame.show()
            self.generative_frame.hide()

# Modify the GenerativePasswordFrame class
class GenerativePasswordFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Generative Random Password")
        self.title_label.setFont(QFont('Arial', 20))
        self.layout.addWidget(self.title_label)

        self.check_lowercase = QCheckBox("Lowercase Letters")
        self.check_uppercase = QCheckBox("Uppercase Letters")
        self.check_digits = QCheckBox("Digits")
        self.check_symbols = QCheckBox("Symbols")

        self.layout.addWidget(self.check_lowercase)
        self.layout.addWidget(self.check_uppercase)
        self.layout.addWidget(self.check_digits)
        self.layout.addWidget(self.check_symbols)

        self.length_label = QLabel("Password Length:")
        self.length_combo = QComboBox()
        self.length_combo.addItems(["8", "12", "14", "16"])

        self.layout.addWidget(self.length_label)
        self.layout.addWidget(self.length_combo)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.setStyleSheet("""
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
            padding: 10px;
            min-width: 200px; /* Set minimum width */
            max-width: 200px; /* Set maximum width */
        """)  # Set button style and width
        self.generate_button.clicked.connect(self.generate_password)

        self.layout.addWidget(self.generate_button)

        self.generated_password_display = QTextEdit()
        self.generated_password_display.setReadOnly(True)
        self.generated_password_display.setFixedSize(300, 100)  # Set text box size
        self.layout.addWidget(self.generated_password_display)

        self.copy_button = QPushButton("Copy Password")
        self.copy_button.setStyleSheet("""
            background-color: #28a745;
            color: white;
            border-radius: 5px;
            padding: 10px;
            min-width: 200px; /* Set minimum width */
            max-width: 200px; /* Set maximum width */
        """)  # Set button style and width
        self.copy_button.clicked.connect(self.copy_password)

        self.layout.addWidget(self.copy_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedSize(300, 10)  # Set progress bar size
        self.layout.addWidget(self.progress_bar)

    def generate_password(self):
        if not any([self.check_lowercase.isChecked(), self.check_uppercase.isChecked(), self.check_digits.isChecked(),
                    self.check_symbols.isChecked()]):
            self.generated_password_display.setText("Please select at least 1 option.")
            return

        self.progress_bar.setRange(0, 0)

        character_sets = []
        if self.check_lowercase.isChecked():
            character_sets.append(string.ascii_lowercase)
        if self.check_uppercase.isChecked():
            character_sets.append(string.ascii_uppercase)
        if self.check_digits.isChecked():
            character_sets.append(string.digits)
        if self.check_symbols.isChecked():
            character_sets.append(string.punctuation)

        password_length = int(self.length_combo.currentText())
        if password_length < 8:
            self.generated_password_display.setText("Password length must be at least 8 characters.")
            self.progress_bar.setRange(0, 1)
            return

        generated_password = ''.join(secrets.choice(char_set) for char_set in character_sets)
        while len(generated_password) < password_length:
            generated_password += secrets.choice(secrets.choice(character_sets))
        generated_password = generated_password[:password_length]  # Truncate to desired length
        self.progress_bar.setRange(0, 1)
        self.generated_password_display.setText(generated_password)

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.generated_password_display.toPlainText())
        QMessageBox.information(self, "Password Copied", "Password copied to clipboard.")

# Modify the CustomizedPasswordFrame class
class CustomizedPasswordFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Customize your password with your Inputs")
        self.title_label.setFont(QFont('Arial', 20))
        self.layout.addWidget(self.title_label)

        self.name_label = QLabel("Favorite Name:")
        self.name_entry = QLineEdit()

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_entry)

        self.numbers_label = QLabel("Favorite Number:")
        self.numbers_entry = QLineEdit()

        self.layout.addWidget(self.numbers_label)
        self.layout.addWidget(self.numbers_entry)

        self.colors_label = QLabel("Favorite Color:")
        self.colors_entry = QLineEdit()

        self.layout.addWidget(self.colors_label)
        self.layout.addWidget(self.colors_entry)

        self.symbols_label = QLabel("Favorite Symbol:")
        self.symbols_entry = QLineEdit()

        self.layout.addWidget(self.symbols_label)
        self.layout.addWidget(self.symbols_entry)

        self.length_label = QLabel("Password Length:")
        self.length_combo = QComboBox()
        self.length_combo.addItems(["8", "12", "14", "16"])

        self.layout.addWidget(self.length_label)
        self.layout.addWidget(self.length_combo)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.setStyleSheet("""
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
            padding: 10px;
            min-width: 200px; /* Set minimum width */
            max-width: 200px; /* Set maximum width */
        """)  # Set button style and width
        self.generate_button.clicked.connect(self.generate_password)

        self.layout.addWidget(self.generate_button)

        self.generated_password_display = QTextEdit()
        self.generated_password_display.setReadOnly(True)
        self.generated_password_display.setFixedSize(300, 100)  # Set text box size
        self.layout.addWidget(self.generated_password_display)

        self.copy_button = QPushButton("Copy Password")
        self.copy_button.setStyleSheet("""
            background-color: #28a745;
            color: white;
            border-radius: 5px;
            padding: 10px;
            min-width: 200px; /* Set minimum width */
            max-width: 200px; /* Set maximum width */
        """)  # Set button style and width
        self.copy_button.clicked.connect(self.copy_password)

        self.layout.addWidget(self.copy_button)

    def generate_password(self):
        inputs = [self.name_entry.text(), self.numbers_entry.text(), self.colors_entry.text(),
                  self.symbols_entry.text()]
        inputs = [i for i in inputs if i]  # Remove empty inputs

        if len(inputs) < 2:
            self.generated_password_display.setText("Please enter at least 2 inputs.")
            return

        password_length = int(self.length_combo.currentText())
        while True:
            generated_password = ''.join(secrets.choice(inputs) for _ in range(password_length))
            if len(generated_password) >= password_length:
                break
        generated_password = generated_password[:password_length]  # Truncate to desired length
        self.generated_password_display.setText(generated_password)

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.generated_password_display.toPlainText())
        QMessageBox.information(self, "Password Copied", "Password copied to clipboard.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_modern_style(app)  # Apply the modern style
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())
