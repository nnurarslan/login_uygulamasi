import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login_form import Ui_MainWindow  # login_form.py dosyasındaki sınıf
from pymongo import MongoClient

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.check_credentials)

        #MONGODB'YE BAĞLANMA
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["users_db"]
        self.collection = self.db["users"]

    def check_credentials(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        #Mongodbde kullanıcı arama
        user = self.collection.find_one({"username": username, "password": password})
        print(user)
        if user:
            QMessageBox.information(self, "Başarılı!","Giriş Başarılı")
        else:
            QMessageBox.warning(self,"Başarısız","Giriş Başarısız..")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
