import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from login import Ui_login
from hitung import Ui_menuUtama
from register import Ui_regis

user = {}
with open('akun.txt', 'r') as file:  # membaca file akun
    for line in file:
        line = line.split()
        user.update({line[0]: line[1]})

catatanBulanan = {}  # catatan tiap bulan akan di simpan disini setiap diganti bulanya


class loginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.login)  # Tombol Login
        self.ui.btnregister.clicked.connect(
            self.registerasi)  # Tombol register

    def login(self):
        # https://stackoverflow.com/questions/4663207/masking-qlineedit-text
        for username in user:
            password = user[username]
            # Mencocokan username  & Password masukkan
            if self.ui.username.text() == username and self.ui.password.text() == password:
                self.window = hitungWindow()
                self.window.show()
                self.close()
                break
        else:
            # https://stackoverflow.com/questions/40227047/python-pyqt5-how-to-show-an-error-message-with-pyqt5
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Password atau Username Anda Salah")
            msg.setWindowTitle("Error")
            msg.exec_()

    def registerasi(self):  # Membukan window register
        self.window = registerWindow()
        self.window.show()
        self.close()


class registerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(registerWindow, self).__init__()
        self.ui = Ui_regis()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.buka_login)
        self.ui.btn_register.clicked.connect(self.regis)

    def regis(self):
        self.dataAkun()
        registrasiakun = self.ui.line_username.text()
        registrasipassword = self.ui.line_password.text()
        msg = QMessageBox()
        try:
            if registrasiakun in user:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("User Name Sudah ada")
                msg.setWindowTitle("Failed")
                msg.exec_()
            else:
                if registrasiakun == "" and registrasipassword == "":
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText(
                        "Masukan Username & Passowrd Tidak boleh kosong")
                    msg.setWindowTitle("Failed")
                    msg.exec_()

                else:
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Berhasil membuat akun")
                    msg.setWindowTitle("Success")

                    akunregistrasi = open("akun.txt", "a")
                    akunregistrasi.write(
                        f"\n{registrasiakun} {registrasipassword}")
                    akunregistrasi.close()
                    with open("akun.txt") as file:
                        for line in file:
                            username, password = line.split()
                            user[username] = password
                    msg.exec_()
                    self.buka_login()
        except ValueError:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Masukan Username & Passowrd Tidak boleh kosong")
            msg.setWindowTitle("Failed")
            msg.exec_()

    def buka_login(self):
        self.login = loginWindow()
        self.login.show()
        self.close()

    def dataAkun(self):
        with open("akun.txt") as file:
            for line in file:
                username, password = line.split()
                user[username] = password


class hitungWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(hitungWindow, self).__init__()
        self.ui = Ui_menuUtama()
        self.ui.setupUi(self)
        self.row = 0
        self.laba = 0
        self.catatanBulanan = catatanBulanan
        self.ui.tableWidget.clicked.connect(self.dataTabel) # table pengeluaran dan table pemasukan
        self.ui.btnHitungUlang.clicked.connect(self.updateTable)
        self.ui.bulan.activated.connect(self.gantiBulan) 
        self.ui.btnsimpan.clicked.connect(self.updateDataText)

    def gantiBulan(self): # untuk mengganti bulan 
        if(self.ui.bulan.currentText() == "January"):
            with open('1.txt', 'r+') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    self.catatanBulanan[hari] = [pemasukan, pengeluaran]
                file.close()
            self.updateTable()
        if(self.ui.bulan.currentText() == "Febuary"):
            with open('2.txt', 'r+') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    self.catatanBulanan[hari] = [pemasukan, pengeluaran]
                file.close()

            self.updateTable()
        if(self.ui.bulan.currentText() == "Maret"):
            with open('3.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "April"):
            with open('4.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Mei"):
            with open('5.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Juni"):
            with open('6.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Juli"):
            with open('7.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Agustus"):
            with open('8.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "September"):
            with open('9.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Oktober"):
            with open('10.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "November"):
            with open('11.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()
        if(self.ui.bulan.currentText() == "Desember"):
            with open('12.txt', 'r') as file:  # membaca file akun
                for line in file:
                    hari, pemasukan, pengeluaran = line.split()
                    catatanBulanan[hari] = [pemasukan, pengeluaran]
            self.updateTable()

    def dataTabel(self): # memasukkan data dari database ke dalam tabel
        kolomPilihan = self.ui.tableWidget.currentRow()
        barisPilihan = self.ui.tableWidget.currentColumn()
        self.catatanBulanan['{}'.format(
            kolomPilihan + 1)][barisPilihan] = self.ui.tableWidget.item(kolomPilihan, barisPilihan).text()
        self.ui.tableWidget.cellChanged.connect(self.updateDataText)

    def updateDataText(self): # mengganti database bulan yang akan tampil di tabel
        if(self.ui.bulan.currentText() == "January"):
            with open('1.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Febuary"):
            with open('2.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Maret"):
            with open('3.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "April"):
            with open('4.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Mei"):
            with open('5.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Juni"):
            with open('6.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Juli"):
            with open('7.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Agustus"):
            with open('8.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "September"):
            with open('9.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Oktober"):
            with open('10.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "November"):
            with open('11.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()
        if(self.ui.bulan.currentText() == "Desember"):
            with open('12.txt', 'w') as file:
                file.truncate(0)
                for i in self.catatanBulanan:
                    file.write(
                        f'{i} {self.catatanBulanan[i][0]} {self.catatanBulanan[i][1]}\n')
                file.close()

    def updateTable(self): # melakukkan update pada tabel 
        for x in self.catatanBulanan:
            self.ui.tableWidget.setRowCount(int(x))
            self.ui.tableWidget.setItem(
                int(x) - 1, 0, QTableWidgetItem(str(self.catatanBulanan[x][0])))
            self.ui.tableWidget.setItem(
                int(x)-1, 1, QTableWidgetItem(str(self.catatanBulanan[x][1])))
        self.hitungLaba()

    def hitungLaba(self): # melakukan perhitungan laba dan perhitungan pengeluaran,pemasukan
        self.laba = 0
        self.pengeluaranPerhari = 0
        self.pemasukanPerhari = 0
        try:
            for x in self.catatanBulanan:
                self.laba += int(self.catatanBulanan[x][0]) - \
                    int(self.catatanBulanan[x][1])
                self.pengeluaranPerhari += int(self.catatanBulanan[x][1])
                self.pemasukanPerhari += int(self.catatanBulanan[x][0])
            self.ui.lblpemasukanPerharinomial.setText(
                '{}'.format(round(self.pemasukanPerhari/31)))
            self.ui.lblpengeluaranPerharinominal.setText(
                '{}'.format(round(self.pengeluaranPerhari/31)))
            self.ui.lblNominal.setText('{}'.format(self.laba))
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Hanya Boleh Memasukkan Angka")
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = loginWindow()
    window.show()
    sys.exit(app.exec_())
