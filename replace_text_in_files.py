import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(963, 542)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 941, 171))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 791, 34))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(820, 10, 131, 34))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 230, 941, 171))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(870, 500, 85, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 410, 941, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 440, 801, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 470, 941, 20))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(40, 500, 781, 26))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QAction(Form)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.search_files)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "برنامج استبدال جملة فى ملفات كثيرة"))
        self.textEdit.setPlaceholderText(_translate("Form", "ادخل الجملة القديمة التى تريد استبدالها دخل الملفات"))
        self.lineEdit.setPlaceholderText(_translate("Form", "ادخل مسار الفولدر الذى تريد جلب الملفات منه"))
        self.lineEdit_2.setText(_translate("Form", ".html"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "اخل امتداد الملف"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "ادخل الجملة الجديدة التى ستحل محل الجملة القديمة"))
        self.pushButton.setText(_translate("Form", "نفذ"))
        self.label.setText(_translate("Form", "الحالة"))
        self.label_2.setText(_translate("Form", "الحالة"))
        self.label_3.setText(_translate("Form", "الحالة"))
        self.pushButton_2.setText(_translate("Form", "pushButton"))

    def search_files(self):
        folder = self.lineEdit.text()
        ext = self.lineEdit_2.text().strip().lower()

        if not os.path.isdir(folder):
            self.label.setText("خطأ المسار غير صالح!")
            return

        if not ext.startswith("."):
            ext = "." + ext

        result = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(ext):
                    result.append(os.path.join(root, file))


        search_text = self.textEdit.toPlainText()
        replace_text = self.textEdit_2.toPlainText()
        ii = 0


        for file_path in result:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                new_content = content.replace(search_text, replace_text)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)

                
                self.progressBar.setValue(int(ii * 100 / len(result)))
                self.label.setText(str(file_path))
                self.label_2.setText(" رقم الملف" + str(ii))
                self.label_3.setText("المجلد" + str(file_path))
                ii += 1
                with open("search_files.txt", 'a', encoding='utf-8') as file:
                    file.write(file_path + "\n")

            except FileNotFoundError:
                self.label_2.setText("الملف غير موجود: " + str(file_path))
            except Exception as e:
                self.label_3.setText("حدث خطأ مع الملف: " + str(file_path))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
