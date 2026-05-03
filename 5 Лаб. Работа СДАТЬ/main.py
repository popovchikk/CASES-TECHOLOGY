import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form.ui", self)

        self.loadButton.clicked.connect(self.load_data)
        self.analyzeButton.clicked.connect(self.analyze)

        self.reviews = []

    # Модуль сбора данных
    def load_data(self):
        brand = self.brandInput.text().strip()

        if not brand:
            self.resultLabel.setText("Ошибка: введите название бренда")
            return

        # имитация отзывов
        self.reviews = [
            "хороший продукт",
            "ужасное качество",
            "нормально"
        ]

        self.resultLabel.setText(f"Отзывы загружены для: {brand}")

    # Модуль анализа
    def analyze(self):
        if not self.reviews:
            self.resultLabel.setText("Сначала загрузите отзывы")
            return

        positive = 0
        negative = 0

        for review in self.reviews:
            if "хорош" in review:
                positive += 1
            elif "ужас" in review:
                negative += 1

        if positive > negative:
            result = "Положительная"
        elif negative > positive:
            result = "Отрицательная"
        else:
            result = "Нейтральная"

        self.resultLabel.setText(f"Репутация бренда: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())