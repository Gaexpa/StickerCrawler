from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt, QTimer
from PyQt6 import QtGui
import sys
import StickerCrawler

class Layout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CS2 Sticker Crawler')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnBottomHint)
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        width = 200
        height = 130
        margin = 30
        self.setGeometry(1920-width-margin, 1080-height-margin-40, width, height)
        self.ui()

    def ui(self):
        self.label1 = QLabel(self)
        self.label1.setText('2024 Copenhagen SAW(黃金)')
        self.label1.setStyleSheet('font-size:14px')
        self.label1.setContentsMargins(0,0,0,0)          # 設定邊界
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        r = 100
        self.grview = QGraphicsView(self)
        self.grview.setGeometry(5, 25, r, r)
        img_path = r'C:\Users\Cliff\Desktop\Programs\Python\Crawler\SAW.png'
        img = QtGui.QPixmap(img_path)
        img = img.scaled(80, 80)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 80, 80)
        self.scene.addPixmap(img)
        self.grview.setScene(self.scene)

        self.label3 = QLabel(self)
        self.label3.setText('買家最高出價')
        self.label3.setStyleSheet('font-size:12px')
        self.label3.move(115, 25)

        self.HBP = QLabel(self)
        self.HBP.setText(str(StickerCrawler.order_data['highest_buy_order']*32)+' TWD')
        self.HBP.setStyleSheet('font-size:15px')
        self.HBP.move(110, 45)

        self.label4 = QLabel(self)
        self.label4.setText('賣家最低出價')
        self.label4.setStyleSheet('font-size:12px')
        self.label4.move(115, 80)

        self.LSP = QLabel(self)
        self.LSP.setText(str(StickerCrawler.order_data['lowest_sell_order']*32)+' TWD')
        self.LSP.setStyleSheet('font-size:15px')
        self.LSP.move(110, 100)

        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1800000)   #3600000ms = 1hr

    def refresh(self):
        StickerCrawler.refresh()
        self.HBP.setText(str(StickerCrawler.order_data['highest_buy_order']*32)+' TWD')
        self.LSP.setText(str(StickerCrawler.order_data['lowest_sell_order']*32)+' TWD')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)	# 視窗程式開始
    widgets = Layout()	# 建立基層元件
    widgets.show()	# 顯示基層元件
    sys.exit(app.exec())