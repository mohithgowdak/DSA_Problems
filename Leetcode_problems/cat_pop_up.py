from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
import sys
import datetime

class CountdownWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(50, 50, 300, 100)  # Position and size of the widget

        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18px; color: white; background-color: rgba(0, 0, 0, 150); padding: 10px; border-radius: 10px;")

        self.update_countdown()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(86400000)  # Update every 24 hours

    def update_countdown(self):
        today = datetime.date.today()
        cat_2025 = datetime.date(2025, 11, 30)
        cat_2026 = datetime.date(2026, 11, 29)

        days_left_2025 = (cat_2025 - today).days
        days_left_2026 = (cat_2026 - today).days

        countdown_text = f"Days left for CAT 2025: {days_left_2025}\nDays left for CAT 2026: {days_left_2026}"
        self.label.setText(countdown_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    countdown_widget = CountdownWidget()
    countdown_widget.show()
    sys.exit(app.exec_())
