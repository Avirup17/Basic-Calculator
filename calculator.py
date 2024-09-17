#Importing libraries
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit,QGridLayout, QPushButton,QVBoxLayout,QHBoxLayout

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
    
        #Title & Dimensions
        self.setWindowTitle("Basic Calculator")
        self.resize(250,400)

        #AllObjects
        self.text_box=QLineEdit()
        self.text_box.setFont(QFont("Comic Sans MS",16))
        self.grid=QGridLayout()

        self.buttons=["7","8","9","/",
                "4","5","6","*",
                "1","2","3","-",
                ".","0","=","+"]
        self.clear=QPushButton("Clear")
        self.delete=QPushButton("Delete")

        #For displaying 
        row=0
        col=0
        for i in self.buttons:
            button=QPushButton(i)
            button.clicked.connect(self.button_click)
            if i.isdigit():
                button.setStyleSheet("QPushButton { font: 10pt Comic Sans MS ;border-radius: 10px;border: 2px solid #FFFF00;padding: 10px; }")
            else:
                button.setStyleSheet("QPushButton { font: 10pt Comic Sans MS ;border-radius: 10px;border: 2px solid #654321;padding: 10px; }")
            self.grid.addWidget(button,row,col)
            col+=1

            if col>3:
                col=0
                row+=1

        self.clear.setStyleSheet("QPushButton { font: 10pt Comic Sans MS ;border-radius: 10px;border: 2px solid #00008B; }")
        self.delete.setStyleSheet("QPushButton { font: 10pt Comic Sans MS ;border-radius: 10px;border: 2px solid #8B0000; }")
        self.text_box.setStyleSheet("QLineEdit { border-radius: 5px;border: 2px solid #00ab41; }")

        self.text_box.returnPressed.connect(self.enter_key)

        #Design
        master_layout=QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row=QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)

        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    #Functions
    def button_click(self):
        button=app.sender()
        text=button.text()
        if text=="=":
            self.result()

        elif text=="Clear":
            self.text_box.clear()

        elif text=="Delete":
            current_value=self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value=self.text_box.text()
            self.text_box.setText(current_value + text)

    def result(self):
        symbol=self.text_box.text()
        try:
            res=eval(symbol)
            self.text_box.setText(str(res))
            
        except Exception as ex:
            print("Error:",ex)

    def enter_key(self):
        self.result()

if __name__ == "__main__":
    #App settings
    app = QApplication([])
    main_window = Calculator()
    main_window.setStyleSheet("QWidget { background-color:#ADD8E6 }")

    #Display/Execute
    main_window.show()
    app.exec_()
