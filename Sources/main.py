import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets
import MainWindow, EmployerForm, AddHotel, HotelRew 
import RegForm
import sqlite3
import hashlib

def hash_ps(password):
    return hashlib.sha256(password.encode()).hexdigest()

class HotelReviewer(HotelRew.Ui_Form):
    def setupUi(self, Form, hotelId: int):
        super().setupUi(Form)
        self.hotelId = hotelId
        self.DBConnector = DBConnector('HotelSystem.db')
        self.addRoomBtn.clicked.connect(self.get_data_for_room)
        self.addEmpBtn.clicked.connect(self.get_data_for_emps)
        self.loadRooms()
        self.loadEmployers()
        
    def get_data_for_emps(self):
        fio = self.fio.text()
        position = self.comboBox.itemText(self.comboBox.currentIndex())
        salary = self.salary.text()

        if self.comboBox.currentIndex() != 0:
            self.DBConnector.addEmployer(fio, position, salary)
            print("OK")
        else:
            QMessageBox.warning(QtWidgets.QWidget(), "Ошибка", "Выберите должность")
        
    def get_data_for_room(self):
        num = self.roomNumInput.text()
        price = self.price.text()
        isBook = "нет"
        visitor = "-"
        self.DBConnector.addRoom(num, self.hotelId, price, isBook, visitor)
        

    # def addRoom_(self, hotelId, num, price, isBook, visitor):

    def loadEmployers(self):
        empl = self.DBConnector.get_employers()

        if not empl:
            return
        
        for emp in empl:
            row_position = self.employersTable.rowCount()
            self.employersTable.insertRow(row_position)  
            for col, data in enumerate(emp):
                self.employersTable.setItem(row_position, col, QTableWidgetItem(str(data)))

    def loadRooms(self):
        rooms = self.DBConnector.get_all_rooms()

        if not rooms:
            return 
         
        for room in rooms:
            row_position = self.roomTable.rowCount()
            self.roomTable.insertRow(row_position)  
            for col, data in enumerate(room):
                self.roomTable.setItem(row_position, col, QTableWidgetItem(str(data))) 
        

class AddHotelForm(AddHotel.Ui_HotelAddForm):
    def setupUi(self, HotelAddForm):
        super().setupUi(HotelAddForm)
        self.buttonBox.accepted.connect(lambda: self.get_info(HotelAddForm))
        self.buttonBox.rejected.connect(HotelAddForm.reject)
        self.DBConnector = DBConnector('HotelSystem.db')
        
    
    def get_info(self, AddHotelForm):
        hotelName = self.hotelName.text()
        try:
            # roomCount = int(self.roomCount.text())
            self.DBConnector.addHotel(hotelName)
            AddHotelForm.accept()
        except Exception as e:
            QMessageBox.warning(AddHotelForm, "Ошибка", f"Неверный ввод данных!\n {e}")

    
class DBConnector():
    def __init__(self, database):
        self.db = database
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def get_user(self, username) -> tuple:
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = self.cursor.fetchone()
        
        return user # (id, username, password, status)
    
    def close(self):
        self.conn.close()
        self.cursor.close()


    def addUser(self, username: str, password: str, status: int):
        hashed_password = hash_ps(password)
        try:
            self.cursor.execute('INSERT INTO users (username, password, status) VALUES (?, ?, ?)', 
                                (username, hashed_password, status))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Пользователь с таким именем уже существует")
            return False
        except Exception as e:
            print(f'Произошла ошибка {e}')
            return False
        

    def addHotel(self, hotelName: str):
        try:
            self.cursor.execute('INSERT INTO hotels (hotelName) VALUES (?)', 
                                (hotelName, ))
            self.conn.commit()
        except Exception as e:
            print(f"Произошла ошибка {e}")
            return False

    def get_all_hotels(self):
        try:
            self.cursor.execute('SELECT hotelName FROM hotels')
            hotels = self.cursor.fetchall()
            hotels_strings = []
            for hotel in hotels:
                hotel_name = hotel[0]  
                hotels_strings.append(hotel_name) 
            return hotels_strings
        except Exception as e:
            print(f"Ошибка при извлечении отелей: {e}")
            return []

    def delHotel(self, hotelName):
        try:
            self.cursor.execute('DELETE FROM hotels WHERE hotelName=?', 
                                (hotelName,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                print("Отель не найден.")
                return False
        except Exception as e:
            print(f'ERROR >> {e}')
            return False
        
    def addRoom(self, roomnum: int, hotelId: int, price: int, isBook: str, visitor: str):
        try:
            self.cursor.execute('INSERT INTO rooms (roomNum, hotelId, price, isBooked, visitor) VALUES(?,?,?,?,?)',
                                (roomnum, hotelId, price, isBook, visitor))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def addEmployer(self, fio: str, position: str, salary: int):
        try:
            self.cursor.execute('INSERT INTO employers (fio, position, salary) VALUES (?,?,?)',
                                (fio, position, salary))
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_hotel_id(self, hotelName):
        self.cursor.execute('SELECT * FROM hotels WHERE hotelName=?',
                            (hotelName,))
        id_ = self.cursor.fetchone()
        return id_    

    def get_all_rooms(self):
        self.cursor.execute('SELECT * FROM rooms')
        return self.cursor.fetchall() # list = [tuple1: str, tuple2: str, ... , tupleN: str]    
    
    def get_employers(self):
        self.cursor.execute('SELECT * FROM employers')
        return self.cursor.fetchall()

class Register(RegForm.Ui_Dialog):
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.on_ok(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        self.DbConnector = DBConnector('HotelSystem.db')

    def on_ok(self, Dialog):
        username = self.username.text()      
        passwd = self.password.text()    
        if self.comboBox.currentIndex() == 0:
            print("Вы ничего не выбрали")
            QMessageBox.warning(Dialog, "Ошибка", "Пожалуйста, проверьте правильность ввода данных и корректность выбора из списка.")
        else:    
            status = self.comboBox.currentIndex()
            print(status)
            self.addUser(username, passwd, status)
            Dialog.accept()  # Закрываем диалог после успешного добавления

    def addUser(self, username, password, status):
        self.DbConnector.addUser(username, password, status)
        

class EmployerForm_(EmployerForm.Ui_AdminForm):
    def setupUi(self, AdminForm, username: str):
        super().setupUi(AdminForm)
        self.addHotelBtn.clicked.connect(self.openHotelAdder)
        self.lineEdit.setText(username)
        # self.pushButton_4.clicked.connect(self.exit)
        self.addHotelBtn.clicked.connect(self.openAddHotelForm)
        self.DBConnector = DBConnector('HotelSystem.db')
        self.updateBtn.clicked.connect(self.loadHotels)
        self.seeHotelBtn.clicked.connect(self.openHotelForm)
        self.delHotelBtn.clicked.connect(self.delHotel_)
        
        # self.loadHotels()

    def delHotel_(self):
        curHotel = self.comboBox.itemText(self.comboBox.currentIndex())
        if curHotel and curHotel != "Не выбрано":
            print("OK")
            self.DBConnector.delHotel(curHotel)
            self.comboBox.removeItem(self.comboBox.currentIndex())
        else:
            print("Отелей не найдено")



    def openHotelForm(self):
        curHotel = self.comboBox.itemText(self.comboBox.currentIndex())
        id_ = self.DBConnector.get_hotel_id(curHotel)
        w = QtWidgets.QDialog()
        ui = HotelReviewer()
        ui.setupUi(w, id_[0])
        w.exec_()


    def openAddHotelForm(self):
        w = QtWidgets.QDialog()
        ui = AddHotelForm()
        ui.setupUi(w)
        w.exec_()
        
    def loadHotels(self):
        hotels = self.DBConnector.get_all_hotels()  # Получаем названия отелей
        if hotels:
            # for i in hotels:
            self.comboBox.clear()
            self.comboBox.addItems(hotels)  # Добавляем названия отелей в comboBox
        

    def openHotelAdder(self):
        pass

    def set_current_user(self, username):
        self.lineEdit.setText(username)

    def exit(self):        
        self.hide()
        

class MainWin(MainWindow.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.exitBtn.clicked.connect(self.exit)
        # self.clientRB.toggled.connect(self.unlockFields)
        # self.workerRB.toggled.connect(self.unlockFields)
        self.regBtn.clicked.connect(self.openRegisterForm)
        self.loginField.textChanged.connect(self.unlockLogin)
        self.passwdField.textChanged.connect(self.unlockLogin)
        self.loginBtn.clicked.connect(self.get_data)
        self.DbConnector = DBConnector('HotelSystem.db')

    def get_data(self):
        username = self.loginField.text()
        password = hash_ps(self.passwdField.text())
        self.Login(username, password)
        

    def exit(self):
        QtWidgets.QApplication.quit()
    
    def unlockFields(self):
        if self.workerRB.isChecked() or self.clientRB.isChecked():
            self.loginField.setEnabled(True)
            self.passwdField.setEnabled(True)
        else:
            self.loginField.setEnabled(False)
            self.passwdField.setEnabled(False)

    def openRegisterForm(self):
        w = QtWidgets.QDialog()  # Создаем новое диалоговое окно
        ui = Register()  # Создаем экземпляр вашего окна регистрации
        ui.setupUi(w)  # Настраиваем интерфейс регистрации
        w.exec_()  # Показываем диалоговое окно как модальное


    def unlockLogin(self):
        if self.loginField.text() != "" and self.passwdField.text() != "":
            self.loginBtn.setEnabled(True)
        else:
            self.loginBtn.setEnabled(False)

    def Login(self, username, password):
        user = self.DbConnector.get_user(username)
        if user and user[2] == password:
            #print("OK")   
            if user[3] == 0 or user[3] == 4:
                w = QtWidgets.QDialog()
                ui = EmployerForm_()
                ui.setupUi(w, user[1])
                w.exec_()
        else:
            pass

        
if __name__ == "__main__":
    # print(hash_ps("admin"))
    print('11111')
    app = QApplication(sys.argv)  # Создание экземпляра приложения

    # Создание и инициализация главного окна
    w = QMainWindow()  # Создаем экземпляр QMainWindow
    ui = MainWin()  # Создание экземпляра вашего класса из MainWindow
    ui.setupUi(w)  # Настройка интерфейса пользователя на окне

    w.show()  # Отображение окна

    sys.exit(app.exec_())  # Запуск приложения

    

