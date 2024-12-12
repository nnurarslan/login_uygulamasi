import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from user_form import Ui_MainWindow  # login_form.py dosyasındaki sınıf
from pymongo import MongoClient

class CrudWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # MONGODB'YE BAĞLANMA
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["users_db"]
        self.collection = self.db["users"]

        self.pushButton_add.clicked.connect(self.create_user)
        self.pushButton_update.clicked.connect(self.update_user)
        self.pushButton_delete.clicked.connect(self.delete_user)
        self.load_users()

    def load_users(self):
        users = self.collection.find()
        for user in users:
            if "username" in user and "password" in user:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position,0,QTableWidgetItem(user["username"]))
                self.tableWidget.setItem(row_position,1,QTableWidgetItem(user["password"]))
            else:
                print("Veritabanındaki kullanıcıda eksik veri var")
    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrudWindow()
    window.show()
    sys.exit(app.exec_())