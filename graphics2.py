





from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 30, 941, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 941, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)  # Set the number of columns to 7
        self.tableWidget.setRowCount(5)  # Set the number of rows to 5
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.headerList = ["Name", "Matric No.", "Grade", 'TCP', 'TNU', 'GPA', 'Remarks']
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def display(self, rows):
        self.tableWidget.setHorizontalHeaderLabels(self.headerList)

        for rowPosition, row in enumerate(rows):
            for itemCount, item in enumerate(row):
                table_item = QtWidgets.QTableWidgetItem(str(item))

                if itemCount == 1:  # Check if it's the second cell (index 1)
                    table_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make the item selectable and enabled
                    table_item.setTextAlignment(QtCore.Qt.AlignCenter)  # Center-align the text in the cell
                    table_item.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255)))  # Set blue color for the link

                self.tableWidget.setItem(rowPosition, itemCount, table_item)

                if itemCount == 1:  # Check if it's the second cell (index 1)
                    table_item.setData(QtCore.Qt.UserRole, row)  # Store the row data as user data for the item

                    # Create a link activated signal connection
                    table_item.setData(QtCore.Qt.UserRole + 1, lambda: self.openNewGUI(row))

    def openNewGUI(self, row):
        new_gui = QtWidgets.QMainWindow()
        ui = Ui_NewWindow()
        ui.setupUi(new_gui)
        ui.display(row)
        new_gui.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class Ui_NewWindow(object):
    def setupUi(self, NewWindow):
        NewWindow.setObjectName("NewWindow")
        NewWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(NewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.tableWidget.setObjectName("tableWidget")
        NewWindow.setCentralWidget(self.centralwidget)

    def display(self, row):
        header_list = ["Column 1", "Column 2", "Column 3"]
        self.tableWidget.setColumnCount(len(header_list))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(header_list)

        for i, item in enumerate(row):
            table_item = QtWidgets.QTableWidgetItem(str(item))
            self.tableWidget.setItem(0, i, table_item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Example usage: provide a list of rows to display
    rows = [
        ['John Doe', '12345', 'A', '100', '90', '4.0', 'Excellent'],
        ['Jane Smith', '67890', 'B', '80', '85', '3.5', 'Good'],
        ['Mike Johnson', '54321', 'C', '70', '75', '3.0', 'Average'],
        ['Emily Davis', '98765', 'A', '95', '92', '3.9', 'Excellent'],
        ['Tom Wilson', '24680', 'B', '85', '88', '3.7', 'Good']
    ]

    ui.display(rows)
    MainWindow.show()
    sys.exit(app.exec_())
