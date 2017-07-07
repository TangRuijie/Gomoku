#created by Wang Zerun
#2017/6/28
#gobang gui 
#pip install PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from isWin import *
from naive_mode import *
import sys
import os
import os.path
import math

#global_variables
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
BOARD_SIZE = 750
BOARD_OFFSET = 50 
BOARD_WIDTH_OFFSET = 137
BOARD_HEIGHT_OFFSET = 9
CHESS_SIZE = 48
CURSOR_SIZE = 50
LISTSIZE = 15
CURSOR_OFFSET = 50
CHESS_OFFSET = 2
NUM_SIZE = 40
NUMPAD_OFFSET = 40
ROPE_WIDTH = 50
ROPE_HEIGHT = 500
ROPE_OFFSET_X = 100
ROPE_OFFSET_Y = -200
SELECT_WIDTH = 161
SELECT_HEIGHT = 35
SELECT1_OFFSET_X = 630
SELECT1_OFFSET_Y = 200
SELECT2_OFFSET_X = 630
SELECT2_OFFSET_Y = 250
CHOOSE_WIDTH = 30
CHOOSE_HEIGHT = 30
MAX_CHESS = 114
PVP_SELECT_WIDTH = 276
PVP_SELECT_HEIGHT = 63
PVP_SELECT_OFFSET_X = 130
PVP_SELECT_OFFSET_Y = 100
DOOR_WIDTH = 512
DOOR_HEIGHT = 768
DOORLEFT_OFFSET_X = -512+137
DOORRIGHT_OFFSET_X = 1024 -137
BUTTON_WIDTH = 223
BUTTON_HEIGHT = 74
BUTTON_OFFSET_X = (1024-223) // 2
AI_BLACK = 2
AI_WHITE = 1
WHITE_VIC = 1
BLACK_VIC = 2

win_x = 0
win_y = 0
win_x_f = 0
win_y_f = 0
your_choose = 0 #0 for white and 1 for black
start_handle = 0
count_white = 0
count_black = 0
cursor_x = 0
cursor_y = 0
black_or_white = 1 #0 for white and 1 for black
last_chess_type = 0 #128 for empty 255 for black 0 for white
last_cursor_x = 0#remain the last chess
last_cursor_y = 0
last_black_x = 0
last_black_y = 0
last_white_x = 0
last_white_y = 0
you_can_regret = 0
rope_under_click = 0
select1_clicked = 0
select2_clicked = 0
pvp_flag = 0 #0 for pvp and 1 for pve
victor = 0 #1 for white and 2 for black
enable_chess = 0

board_list = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
              ]

class back_button(QLabel):
    up = pyqtSignal()
    down = pyqtSignal()
    back = pyqtSignal()
    def __init__(self,parent):
        super(back_button,self).__init__(parent)
        self.buttonimage = QImage("src/back.png")
        self.buttonimage_2 = QImage("src/back_p.png")
        self.setGeometry(QRect(BUTTON_OFFSET_X,-64,BUTTON_WIDTH,BUTTON_HEIGHT))
        self.buttonimage = self.buttonimage.scaled(self.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation)
        self.buttonimage_2 = self.buttonimage_2.scaled(self.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.buttonimage))

    def mouseReleaseEvent(self, QMouseEvent):
        self.setPixmap(QPixmap.fromImage(self.buttonimage))
        return super().mouseReleaseEvent(QMouseEvent)
    def mousePressEvent(self, QMouseEvent):
        self.setPixmap(QPixmap.fromImage(self.buttonimage_2))
        self.back.emit()
        return super().mousePressEvent(QMouseEvent)
    def enterEvent(self, QEvent):   
        self.up.emit()
        return super().enterEvent(QEvent)
    def leaveEvent(self, QEvent):
        self.down.emit()
        return super().leaveEvent(QEvent)

class left_door(QLabel):
    def __init__(self,parent):
        super(left_door,self).__init__(parent)
        self.door_image = QImage("src/door_left.png")
        self.setGeometry(QRect(0,0,DOOR_WIDTH,DOOR_HEIGHT))
        self.door_image = self.door_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.door_image))
    def restart(self):
        self.setGeometry(QRect(0,0,DOOR_WIDTH,DOOR_HEIGHT))

class right_door(QLabel):
    def __init__(self,parent):
        super(right_door,self).__init__(parent)
        self.door_image = QImage("src/door_right.png")
        self.setGeometry(QRect(0 + 512,0,DOOR_WIDTH,DOOR_HEIGHT))
        self.door_image = self.door_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.door_image))
    def restart(self):
        self.setGeometry(QRect(0 + 512,0,DOOR_WIDTH,DOOR_HEIGHT))
                
class pvp_p_button(QLabel):
    opacity = 1
    pvp_select = pyqtSignal()
    stop_timer = pyqtSignal()
    def __init__(self,parent):
        super(pvp_p_button,self).__init__(parent)
        self.button_image = QImage("src/pvp_p.png")
        self.setGeometry(QRect(PVP_SELECT_OFFSET_X,PVP_SELECT_OFFSET_Y,PVP_SELECT_WIDTH,PVP_SELECT_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.button_image = self.button_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.button_image))
    def mousePressEvent(self, QMouseEvent):
        global pvp_flag
        self.pvp_select.emit()
        pvp_flag = 0
        return super().mousePressEvent(QMouseEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
        self.hide()
    def restart(self):
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(PVP_SELECT_OFFSET_X,PVP_SELECT_OFFSET_Y,PVP_SELECT_WIDTH,PVP_SELECT_HEIGHT))
        self.show()

class pvp_e_button(QLabel):
    opacity = 1
    pvp_select = pyqtSignal()
    stop_timer = pyqtSignal()
    def __init__(self,parent):
        super(pvp_e_button,self).__init__(parent)
        self.button_image = QImage("src/pvp_e.png")
        self.setGeometry(QRect(PVP_SELECT_OFFSET_X + 500,PVP_SELECT_OFFSET_Y,PVP_SELECT_WIDTH,PVP_SELECT_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.button_image = self.button_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.button_image))
    def mousePressEvent(self, QMouseEvent):
        global pvp_flag
        self.pvp_select.emit()
        pvp_flag = 1
        return super().mousePressEvent(QMouseEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
        self.hide()
    def restart(self):
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(PVP_SELECT_OFFSET_X + 500,PVP_SELECT_OFFSET_Y,PVP_SELECT_WIDTH,PVP_SELECT_HEIGHT))
        self.show()

class chess_button1(QLabel):
    go_w = pyqtSignal()
    stop_timer = pyqtSignal()
    stop_appear = pyqtSignal()
    opacity = 1
    def __init__(self,parent):
        super(chess_button1,self).__init__(parent)
        self.button_image = QImage("src/chess_w.png")
        self.button_image2 = QImage("src/chess_w2.png")
        self.setGeometry(QRect(-100,-100,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.button_image = self.button_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.button_image2 = self.button_image2.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.button_image))
    def mousePressEvent(self, QMouseEvent):
        global your_choose
        your_choose = 0
        self.go_w.emit()
        return super().mousePressEvent(QMouseEvent)
    def enterEvent(self, QEvent):
        self.setPixmap(QPixmap.fromImage(self.button_image2))
        return super().enterEvent(QEvent)
    def leaveEvent(self, QEvent):
        self.setPixmap(QPixmap.fromImage(self.button_image))
        return super().leaveEvent(QEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
    def restart(self):
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(-100,-100,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.setPixmap(QPixmap.fromImage(self.button_image))
        self.show()

class chess_button2(QLabel):
    go_b = pyqtSignal()
    stop_timer = pyqtSignal()
    stop_appear = pyqtSignal()
    opacity = 1
    def __init__(self,parent):
        super(chess_button2,self).__init__(parent)
        self.button_image = QImage("src/chess_b.png")
        self.button_image2 = QImage("src/chess_b2.png")
        self.setGeometry(QRect(-100,-100,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.button_image = self.button_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.button_image2 = self.button_image2.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.button_image))
    def mousePressEvent(self, QMouseEvent):
        global your_choose
        your_choose = 1
        self.go_b.emit()
        return super().mousePressEvent(QMouseEvent)
    def enterEvent(self, QEvent):
        self.setPixmap(QPixmap.fromImage(self.button_image2))
        return super().enterEvent(QEvent)
    def leaveEvent(self, QEvent):
        self.setPixmap(QPixmap.fromImage(self.button_image))
        return super().leaveEvent(QEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
    def restart(self):       
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(-100,-100,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.setPixmap(QPixmap.fromImage(self.button_image))
        self.show()
class select_button1(QLabel):
    change2 = pyqtSignal()
    stop_timer = pyqtSignal()
    stop_appear = pyqtSignal()
    opacity = 0
    def __init__(self,parent):
        super(select_button1,self).__init__(parent)
        self.select_image_1_1 = QImage("src/select_easy_1.png")
        self.select_image_1_2 = QImage("src/select_easy_2.png")
        self.select_image_1_3 = QImage("src/select_easy_3.png")
        self.setGeometry(QRect(SELECT1_OFFSET_X,SELECT1_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.select_image_1_1 = self.select_image_1_1.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.select_image_1_2 = self.select_image_1_2.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.select_image_1_3 = self.select_image_1_3.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.select_image_1_1))
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.hide()
    def enterEvent(self, QEvent):
        global select1_clicked
        if select1_clicked == 0:
            self.setPixmap(QPixmap.fromImage(self.select_image_1_3))
        return super().enterEvent(QEvent)
    def mousePressEvent(self, QMouseEvent):
        global select1_clicked
        global select2_clicked
        if select1_clicked == 0:
            select1_clicked = 1
            select2_clicked = 0
            self.setPixmap(QPixmap.fromImage(self.select_image_1_2))
            self.change2.emit()
        return super().mousePressEvent(QMouseEvent)
    def leaveEvent(self, QEvent):
        global select1_clicked
        if select1_clicked == 0:
            self.setPixmap(QPixmap.fromImage(self.select_image_1_1))
        return super().leaveEvent(QEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
    def appear(self):
        if self.opacity >= 1.0:
            self.stop_appear.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity += 0.1
    def restart(self):
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(SELECT1_OFFSET_X,SELECT1_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.setPixmap(QPixmap.fromImage(self.select_image_1_1))

class select_button2(QLabel):
    change1 = pyqtSignal()
    stop_timer = pyqtSignal()
    stop_appear = pyqtSignal()
    opacity = 0
    def __init__(self,parent):
        super(select_button2,self).__init__(parent)
        self.select_image_2_1 = QImage("src/select_lunatic_1.png")
        self.select_image_2_2 = QImage("src/select_lunatic_2.png")
        self.select_image_2_3 = QImage("src/select_lunatic_3.png")
        self.setGeometry(QRect(SELECT2_OFFSET_X,SELECT2_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.setMouseTracking(True)
        self.effect = QGraphicsOpacityEffect()
        self.select_image_2_1 = self.select_image_2_1.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.select_image_2_2 = self.select_image_2_2.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.select_image_2_3 = self.select_image_2_3.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.select_image_2_1))
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.hide()
    def enterEvent(self, QEvent):
        #print("enter")
        global select2_clicked
        if select2_clicked == 0:
            self.setPixmap(QPixmap.fromImage(self.select_image_2_3))
        return super().enterEvent(QEvent)
    def mousePressEvent(self, QMouseEvent):
        global select1_clicked
        global select2_clicked
        if select2_clicked == 0:
            select1_clicked = 0
            select2_clicked = 1
            self.setPixmap(QPixmap.fromImage(self.select_image_2_2))
            self.change1.emit()
        return super().mousePressEvent(QMouseEvent)
    def leaveEvent(self, QEvent):
        global select2_clicked
        if select2_clicked == 0:
            self.setPixmap(QPixmap.fromImage(self.select_image_2_1))
        return super().leaveEvent(QEvent)
    def fade(self):
        if self.opacity <= 0.0:
            self.stop_timer.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity -= 0.1
    def appear(self):
        if self.opacity >= 1.0:
            self.stop_appear.emit()
        else:
            self.effect.setOpacity(self.opacity)
            self.setGraphicsEffect(self.effect)
        self.opacity += 0.1
    def restart(self):
        self.opacity = 1
        self.effect.setOpacity(self.opacity)
        self.setGraphicsEffect(self.effect)
        self.setGeometry(QRect(SELECT2_OFFSET_X,SELECT2_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.setPixmap(QPixmap.fromImage(self.select_image_2_1))

class numpadb(QLabel):
    def __init__(self,parent):
        super(numpadb,self).__init__(parent)
        self.setGeometry(QRect(-100,-100,NUM_SIZE,NUM_SIZE))
        self.num_list = []
        self.num_list.append(QImage("src/num_0.png"))
        self.num_list.append(QImage("src/num_1.png"))
        self.num_list.append(QImage("src/num_2.png"))
        self.num_list.append(QImage("src/num_3.png"))
        self.num_list.append(QImage("src/num_4.png"))
        self.num_list.append(QImage("src/num_5.png"))
        self.num_list.append(QImage("src/num_6.png"))
        self.num_list.append(QImage("src/num_7.png"))
        self.num_list.append(QImage("src/num_8.png"))
        self.num_list.append(QImage("src/num_9.png"))
        for i in range(10):
            self.num_list[i] = self.num_list[i].scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
    def shownum(self,num):
        self.setPixmap(QPixmap.fromImage(self.num_list[num]))
        self.show()

class dragrope(QLabel):   
    back_signal = pyqtSignal()
    move_signal = pyqtSignal()
    def __init__(self,parent):
        self.pos_x = ROPE_OFFSET_X
        self.pos_y = ROPE_OFFSET_Y
        self.click_x = 0
        self.click_y = 0
        
        #self.back_animation.setEasingCurve(QEasingCurve.OutInExpo)
        super(dragrope,self).__init__(parent)
        table_image = QImage("src/rope.png")
        table_image = table_image.scaled(parent.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(table_image))
        self.setGeometry(QRect(ROPE_OFFSET_X,ROPE_OFFSET_Y,ROPE_WIDTH,ROPE_HEIGHT))
        self.show()
    def mousePressEvent(self, QMouseEvent):
        global rope_under_click
        if QMouseEvent.buttons() == Qt.LeftButton:
            rope_under_click = 1
            self.click_y = QMouseEvent.globalPos().y()
        return super().mousePressEvent(QMouseEvent)
    def mouseReleaseEvent(self, QMouseEvent):
        global rope_under_click
        rope_under_click = 0
        self.back_signal.emit()
        return super().mouseReleaseEvent(QMouseEvent)
    def mouseMoveEvent(self, QMouseEvent):
        global rope_under_click
        if rope_under_click == 1:
            if self.pos().y() <= 0 and QMouseEvent.pos().y() > self.click_y:
                self.setGeometry(QRect(ROPE_OFFSET_X,ROPE_OFFSET_Y + (QMouseEvent.globalPos().y() - self.click_y),ROPE_WIDTH,ROPE_HEIGHT))
                self.move_signal.emit()
        return super().mouseMoveEvent(QMouseEvent)


class start_board(QLabel):
    def __init__(self,parent):
        super(start_board,self).__init__(parent)
        table_image = QImage("src/start_bg.png")
        table_image = table_image.scaled(parent.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(table_image))
        self.setGeometry(QRect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
        self.show()
class numpadw(QLabel):
    def __init__(self,parent):
        super(numpadw,self).__init__(parent)
        self.setGeometry(QRect(-100,-100,NUM_SIZE,NUM_SIZE))
        self.num_list = []
        self.num_list.append(QImage("src/numw_0.png"))
        self.num_list.append(QImage("src/numw_1.png"))
        self.num_list.append(QImage("src/numw_2.png"))
        self.num_list.append(QImage("src/numw_3.png"))
        self.num_list.append(QImage("src/numw_4.png"))
        self.num_list.append(QImage("src/numw_5.png"))
        self.num_list.append(QImage("src/numw_6.png"))
        self.num_list.append(QImage("src/numw_7.png"))
        self.num_list.append(QImage("src/numw_8.png"))
        self.num_list.append(QImage("src/numw_9.png"))
        for i in range(10):
            self.num_list[i] = self.num_list[i].scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
    def shownum(self,num):
        self.setPixmap(QPixmap.fromImage(self.num_list[num]))
        self.show()
                
class background(QLabel):
    def __init__(self,parent):
        super(background,self).__init__(parent)
        table_image = QImage("src/bg.png")
        table_image = table_image.scaled(parent.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(table_image))
        self.setGeometry(QRect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
        self.show()
 
class chess_black(QLabel):
    def __init__(self,parent):
        super(chess_black,self).__init__(parent)
        chess_black_image = QImage("src/chess_b.png")
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
        chess_black_image = chess_black_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(chess_black_image))  
        self.setMouseTracking(True)   
        self.show()
    def mouseMoveEvent(self, QMouseEvent):
        return super().mouseMoveEvent(QMouseEvent)
    def restart(self):
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))

class chess_white(QLabel):
    def __init__(self,parent):
        super(chess_white,self).__init__(parent)
        chess_white_image = QImage("src/chess_w.png")
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
        chess_white_image = chess_white_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(chess_white_image)) 
        self.setMouseTracking(True)    
        self.show()
    def mouseMoveEvent(self, QMouseEvent):
        return super().mouseMoveEvent(QMouseEvent)
    def restart(self):
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))   

class cursorrect(QLabel):

    cursor_signal = pyqtSignal()
    def __init__(self,parent):

        super(cursorrect,self).__init__(parent)
        cursor_image = QImage("src/cursor.png")
        self.setGeometry(QRect(BOARD_WIDTH_OFFSET,BOARD_HEIGHT_OFFSET,CURSOR_SIZE,CURSOR_SIZE))
        cursor_image = cursor_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(cursor_image)) 
        self.setMouseTracking(True) 
        self.show()
    def mouseMoveEvent(self, QMouseEvent):
        return super().mouseMoveEvent(QMouseEvent)  
    def mousePressEvent(self,QMouseEvent):
        global start_handle
        if start_handle == 1:
            self.cursor_signal.emit()
        return super().mousePressEvent(QMouseEvent)

class chess_last(QLabel):
    def __init__(self,parent):
        super(chess_last,self).__init__(parent)
        last_image = QImage("src/chess_last.png")
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
        last_image = last_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(last_image)) 
        self.setMouseTracking(True) 
    def mouseMoveEvent(self, QMouseEvent):
        return super().mouseMoveEvent(QMouseEvent)
    def restart(self):
        self.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))

class Mythread(QThread):
    finish_signal = pyqtSignal()
    def __init__(self):
        super(Mythread,self).__init__()
    def run(self):
        global board_list
        global black_or_white
        global count_white
        global count_black
        global last_chess_type
        global last_cursor_x
        global last_cursor_y
        global last_black_x
        global last_black_y
        global last_white_x
        global last_white_y
        if black_or_white == 1:
            list_temp = naive_mode(board_list,AI_BLACK)
            board_list[list_temp[0]][list_temp[1]] = 2
            last_chess_type = 1
            last_cursor_x = list_temp[1]
            last_cursor_y = list_temp[0]
            last_black_x = list_temp[1]
            last_black_y = list_temp[0]
            
            print(last_black_x,last_black_y)
            self.finish_signal.emit()
        else:
            list_temp = naive_mode(board_list,AI_WHITE)
            board_list[list_temp[0]][list_temp[1]] = 1
            last_chess_type = 0
            last_cursor_x = list_temp[1]
            last_cursor_y = list_temp[0]
            last_white_x = list_temp[1]
            last_white_y = list_temp[0]
            print(last_white_x,last_white_y)
            self.finish_signal.emit()

class chessboard(QLabel):
    ai = Mythread()
    opacity = 1
    start_chess = pyqtSignal()
    victory = pyqtSignal()
    draw_ai_chess = pyqtSignal()
    def __init__(self,parent):
        super(chessboard,self).__init__(parent)
        self.board_image = QImage("src/chessboard.png") 
        self.setGeometry(QRect(BOARD_WIDTH_OFFSET,BOARD_HEIGHT_OFFSET,BOARD_SIZE,BOARD_SIZE))
        self.board_image = self.board_image.scaled(self.size(),
					Qt.KeepAspectRatio,
					Qt.SmoothTransformation)
        self.setPixmap(QPixmap.fromImage(self.board_image))
        self.setMouseTracking(True)
        self.list_chess_b = []
        self.list_chess_w = []        
        self.lastchess = chess_last(self)
        for i in range(MAX_CHESS):
            chess_b = chess_black(self)
            self.list_chess_b.append(chess_b)
            chess_w = chess_white(self)
            self.list_chess_w.append(chess_w)
        self.cursor = cursorrect(self)
        self.player1_timer = QTimer(self)
        self.player2_timer = QTimer(self)
        self.player1_timer.setInterval(1000)
        self.player2_timer.setInterval(1000)
        self.hide()
        self.cursor.cursor_signal.connect(self.drawChess)        
        self.start_chess.connect(self.drawFirstChess)
        self.ai.finish_signal.connect(self.drawAiChess)
        self.draw_ai_chess.connect(self.enablePress)
    def regret(self):
        global you_can_regret
        global count_black
        global count_white
        global board_list
        global last_black_x
        global last_black_y
        global last_white_x
        global last_white_y
        global black_or_white
        global pvp_flag
        if pvp_flag == 1:
            if you_can_regret == 1:
                if count_black >= 1 and count_white >= 1:
                    count_black -= 1
                    count_white -= 1
                    board_list[last_black_y][last_black_x] = 0
                    board_list[last_white_y][last_white_x] = 0
                    self.list_chess_b[count_black].setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                    self.list_chess_w[count_white].setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                    self.lastchess.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                    self.repaint()
                    you_can_regret = 0
        else:
             if you_can_regret == 1:
                 if black_or_white == 1:
                     self.player2_timer.stop()
                     count_white -= 1
                     board_list[last_white_y][last_white_x] = 0
                     self.list_chess_w[count_white].setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                     self.lastchess.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                     self.repaint()
                     you_can_regret = 0
                     black_or_white = 0
                     self.player1_timer.start()

                 else:
                     self.player1_timer.stop()
                     count_black -= 1
                     board_list[last_black_y][last_black_x] = 0
                     self.list_chess_b[count_black].setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                     self.lastchess.setGeometry(QRect(-100,-100,CHESS_SIZE,CHESS_SIZE))
                     self.repaint()
                     you_can_regret = 0
                     black_or_white = 1
                     self.player2_timer.start()
                     
    def drawFirstChess(self):
        global enable_chess

        global pvp_flag
        if pvp_flag == 1:
            if your_choose == 0:
                self.ai.start()
            else:
                enable_chess = 1
        else:
            enable_chess = 1
    def drawAiChess(self):       
        self.player1_timer.stop()
        global count_white
        global count_black
        global black_or_white
        global board_list
        global last_chess_type
        global last_cursor_x
        global last_cursor_y
        global pvp_flag
        global win_x
        global win_x_f
        global win_y
        global win_y_f
        global victor
        pixel_per_halfchess = ((BOARD_SIZE - BOARD_OFFSET) / (LISTSIZE - 1)) / 2
        if black_or_white == 1:
            self.player2_timer.stop()
            self.lastchess.setGeometry(QRect(last_cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,last_cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
            self.lastchess.show()
            self.list_chess_b[count_black].setGeometry(QRect(last_cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,last_cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
            black_or_white = 0
            count_black += 1
            win_list = isWin(board_list)                    
            if win_list[0] == 2:
                win_x = win_list[1]
                win_y = win_list[2]
                win_x_f = win_list[3]
                win_y_f = win_list[4]
                print("black win")
                self.update()
                victor = BLACK_VIC
                self.victory.emit()
                
            else:
                self.player1_timer.start()        
                self.draw_ai_chess.emit()
        else:
            self.player1_timer.stop()
            self.lastchess.setGeometry(QRect(last_cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,last_cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
            self.lastchess.show()
            self.list_chess_w[count_white].setGeometry(QRect(last_cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,last_cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
            black_or_white = 1
            count_white += 1
            win_list = isWin(board_list)                    
            if win_list[0] == 1:
                win_x = win_list[1]
                win_y = win_list[2]
                win_x_f = win_list[3]
                win_y_f = win_list[4]
                print("white win")
                self.update()
                victor = WHITE_VIC
                self.victory.emit()
                
            else:
                self.player2_timer.start() 
                self.draw_ai_chess.emit()   
    def enablePress(self):
        global enable_chess
        enable_chess = 1          
    def drawChess(self):
        global count_white
        global count_black
        global black_or_white
        global board_list
        global last_chess_type
        global last_cursor_x
        global last_cursor_y
        global last_black_x
        global last_black_y
        global last_white_x
        global last_white_y
        global pvp_flag
        global victor
        global win_x
        global win_y
        global win_x_f
        global win_y_f
        global enable_chess
        global you_can_regret
        if enable_chess == 1:
            pixel_per_halfchess = ((BOARD_SIZE - BOARD_OFFSET) / (LISTSIZE - 1)) / 2
            if board_list[cursor_y][cursor_x] == 0:
                you_can_regret = 1              
                if pvp_flag == 1:
                    enable_chess = 0                
                    if black_or_white == 1:
                        board_list[cursor_y][cursor_x] = 2
                        self.player2_timer.stop()
                        black_or_white = 0                                  
                        self.lastchess.setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.lastchess.show()
                        self.list_chess_b[count_black].setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))               
                        count_black += 1                        
                        last_chess_type = 1
                        last_cursor_x = cursor_x                       
                        last_cursor_y = cursor_y
                        last_black_x = cursor_x
                        last_black_y = cursor_y
                        win_list = isWin(board_list)                    
                        if win_list[0] == 2:
                            win_x = win_list[1]
                            win_y = win_list[2]
                            win_x_f = win_list[3]
                            win_y_f = win_list[4]
                            print("black win")
                            self.update()
                            victor = BLACK_VIC
                            self.victory.emit()
                            
                        else:
                            self.player1_timer.start()
                            self.ai.start()                         
                    else:
                        board_list[cursor_y][cursor_x] = 1
                        self.player1_timer.stop()
                        black_or_white = 1
                        self.lastchess.setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.lastchess.show()
                        self.list_chess_w[count_white].setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.update()
                        last_white_x = cursor_x
                        last_white_y = cursor_y
                        count_white += 1                        
                        win_list = isWin(board_list)                    
                        if win_list[0] == 1:
                            win_x = win_list[1]
                            win_y = win_list[2]
                            win_x_f = win_list[3]
                            win_y_f = win_list[4]
                            print("white win")
                            self.update()
                            victor = WHITE_VIC
                            self.victory.emit()
                            
                        else:
                            self.player2_timer.start()
                            self.ai.start()                        
                else:
                    if black_or_white == 1:
                        self.player2_timer.stop()                                  
                        self.lastchess.setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.lastchess.show()
                        self.list_chess_b[count_black].setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))        
                        self.update()       
                        count_black += 1
                        board_list[cursor_y][cursor_x] = 2                    
                        win_list = isWin(board_list)                    
                        if win_list[0] == 2:
                            win_x = win_list[1]
                            win_y = win_list[2]
                            win_x_f = win_list[3]
                            win_y_f = win_list[4]
                            print("black win")
                            self.update()
                            victor = BLACK_VIC
                            self.victory.emit()                            
                        else:
                            self.player1_timer.start()
                            last_chess_type = 255
                            last_cursor_x = cursor_x
                            last_cursor_y = cursor_y
                            last_black_x = cursor_x
                            last_black_y = cursor_y
                            black_or_white = 0
                    else:
                        self.player1_timer.stop()
                        self.lastchess.setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.lastchess.show()
                        self.list_chess_w[count_white].setGeometry(QRect(cursor_x * pixel_per_halfchess * 2 + CHESS_OFFSET,cursor_y * pixel_per_halfchess * 2 + CHESS_OFFSET,CHESS_SIZE,CHESS_SIZE))
                        self.update()
                        count_white += 1
                        board_list[cursor_y][cursor_x] = 1
                        win_list = isWin(board_list)                    
                        if win_list[0] == 1:
                            win_x = win_list[1]
                            win_y = win_list[2]
                            win_x_f = win_list[3]
                            win_y_f = win_list[4]
                            print("white win")
                            self.update()
                            victor = WHITE_VIC
                            self.victory.emit()
                            
                        else:
                            self.player2_timer.start()
                            last_chess_type = 0
                            last_cursor_x = cursor_x
                            last_cursor_y = cursor_y
                            last_white_x = cursor_x
                            last_white_y = cursor_y
                            black_or_white = 1
    def mouseMoveEvent(self, QMouseEvent):
        mouse_point = QMouseEvent.pos()
        pixel_per_halfchess = ((BOARD_SIZE - BOARD_OFFSET) / (LISTSIZE - 1)) / 2
        #print(pixel_per_halfchess)
        cursor_temp_x = int((mouse_point.x() / pixel_per_halfchess) // 2 )
        cursor_temp_y = int((mouse_point.y() / pixel_per_halfchess) // 2 )
        #print(mouse_point.y(),cursor_temp_y)
        global cursor_x
        global cursor_y
        if cursor_temp_x != cursor_x or cursor_temp_y != cursor_y:
            self.cursor.setGeometry(QRect(cursor_temp_x * pixel_per_halfchess * 2 ,cursor_temp_y * pixel_per_halfchess * 2,CURSOR_SIZE,CURSOR_SIZE))            
            cursor_x = cursor_temp_x
            cursor_y = cursor_temp_y
        return super().mouseMoveEvent(QMouseEvent)
    def mousePressEvent(self, QMouseEvent):
        return super().mousePressEvent(QMouseEvent)
    def restart(self):
        self.hide()
        self.lastchess.restart()
        for i in range(MAX_CHESS):
            self.list_chess_b[i].restart()
            self.list_chess_w[i].restart()
class victory_board(QLabel):
    n = 0
    flag = 0
    stop = 0
    delta = 0
    angle = 0
    clicked = 0
    victory_finished = pyqtSignal()
    def __init__(self,parent):
        super(victory_board,self).__init__(parent)
        self.setGeometry(QRect(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
        self.scaletimer = QTimer(self)
        self.scaletimer.setInterval(20)
        self.hide()
        self.scaletimer.timeout.connect(self.update)
    def paintEvent(self, QPaintEvent):
        global victor
        global win_x
        global win_y       
        if victor != 0:
            #print(win_x,win_y,win_x_f,win_y_f)
            pix = QPixmap("src/123.jpg")
            painter = QPainter(self)
            pixel_per_halfchess = ((BOARD_SIZE - BOARD_OFFSET) / (LISTSIZE - 1)) / 2
            if win_x == win_x_f and win_y != win_y_f:
                x_width = (win_y + 2) * pixel_per_halfchess * 2+ pixel_per_halfchess + BOARD_WIDTH_OFFSET 
                y_width = win_x * pixel_per_halfchess * 2+ pixel_per_halfchess +BOARD_HEIGHT_OFFSET
            if win_x != win_x_f and win_y == win_y_f:
                x_width = win_y * pixel_per_halfchess * 2+ pixel_per_halfchess + BOARD_WIDTH_OFFSET
                y_width = (win_x + 2) * pixel_per_halfchess * 2+ pixel_per_halfchess +BOARD_HEIGHT_OFFSET
            if win_x < win_x_f and win_y < win_y_f:
                x_width = (win_y + 2) * pixel_per_halfchess * 2 + pixel_per_halfchess + BOARD_WIDTH_OFFSET
                y_width = (win_x + 2) * pixel_per_halfchess * 2 + pixel_per_halfchess +BOARD_HEIGHT_OFFSET 
            if win_x > win_x_f and win_y < win_y_f:
                x_width = (win_y + 2) * pixel_per_halfchess * 2 + pixel_per_halfchess + BOARD_WIDTH_OFFSET   
                y_width = (win_x_f + 2) * pixel_per_halfchess * 2 + pixel_per_halfchess +BOARD_HEIGHT_OFFSET    
            x_width = x_width - WINDOW_WIDTH / 6
            y_width = y_width - WINDOW_HEIGHT / 6
            left_per_x = x_width / 20
            left_per_y = y_width / 20
            right_per_x = (WINDOW_WIDTH - (x_width + WINDOW_WIDTH / 3)) / 20
            right_per_y = (WINDOW_HEIGHT - (y_width + WINDOW_HEIGHT / 3)) / 20
            if self.n < 20 and self.flag == 0:
                painter.drawPixmap(QRectF(0,0,WINDOW_WIDTH,WINDOW_HEIGHT),pix,QRectF(0 + self.n * left_per_x, 0 + self.n * left_per_y,WINDOW_WIDTH - self.n * right_per_x - self.n * left_per_x,WINDOW_HEIGHT - self.n * right_per_y - self.n * left_per_y))
                self.n += 0.1 
            else:
                if self.n >= 20 and self.clicked == 0:
                    painter.drawPixmap(QRectF(0,0,WINDOW_WIDTH,WINDOW_HEIGHT),pix,QRectF(0 + self.n * left_per_x, 0 + self.n * left_per_y,WINDOW_WIDTH - self.n * right_per_x - self.n * left_per_x,WINDOW_HEIGHT - self.n * right_per_y - self.n * left_per_y))
                if self.n >= 20 and self.clicked == 1:
                    self.flag = 1
                if self.flag == 1 and self.stop == 0 and self.clicked == 1:
                    painter.rotate(self.angle)
                    painter.drawPixmap(QRectF(0,0,WINDOW_WIDTH,WINDOW_HEIGHT),pix,QRectF(0 + self.n * left_per_x, 0 + self.n * left_per_y,WINDOW_WIDTH - self.n * right_per_x - self.n * left_per_x,WINDOW_HEIGHT - self.n * right_per_y - self.n * left_per_y))
                    self.n -= self.delta
                    self.delta += 1
                    self.angle += 1
                if self.n < -200:
                    self.stop = 1
                    self.hide()
                    self.victory_finished.emit()
        self.update()
        return super().paintEvent(QPaintEvent)
    def mousePressEvent(self, QMouseEvent):
        self.clicked = 1
        return super().mousePressEvent(QMouseEvent)
    def restart(self):
        self.n = 0
        self.flag = 0
        self.stop = 0
        self.clicked = 0
        self.delta = 0
        self.angle = 0
        self.hide()
              
class gobang_gui(QMainWindow):
    pic_ready = pyqtSignal()
    restart_ready = pyqtSignal()
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.setWindowTitle("GoMoKu")
        self.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.screen = QGuiApplication.primaryScreen()
        self.table = background(self)
        self.board = chessboard(self)
        self.backbutton = back_button(self)
        self.door_left = left_door(self)
        self.door_right = right_door(self)
        self.vic_scene = victory_board(self)
        self.pvp = pvp_p_button(self)
        self.pve = pvp_e_button(self)
        self.choosew = chess_button1(self)
        self.chooseb = chess_button2(self)
        self.fadetimer = QTimer(self)
        self.appeartimer = QTimer(self)
        self.appeartimer.setInterval(20)
        self.fadetimer.setInterval(20)
        self.start = start_board(self)
        self.rope = dragrope(self)
        self.select1 = select_button1(self)
        self.select2 = select_button2(self)
        self.openleft_animation = QPropertyAnimation(self.door_left,b"geometry")
        self.openright_animation = QPropertyAnimation(self.door_right,b"geometry")
        self.openleft_animation.setDuration(500)
        self.openright_animation.setDuration(500)
        self.openleft_animation.setEasingCurve(QEasingCurve.InQuad)
        self.openright_animation.setEasingCurve(QEasingCurve.InQuad)
        self.closeleft_animation = QPropertyAnimation(self.door_left,b"geometry")
        self.closeright_animation = QPropertyAnimation(self.door_right,b"geometry")
        self.closeleft_animation.setDuration(1000)
        self.closeright_animation.setDuration(1000)
        self.closeleft_animation.setEasingCurve(QEasingCurve.InQuad)
        self.closeright_animation.setEasingCurve(QEasingCurve.InQuad)
        self.back_animation = QPropertyAnimation(self.rope,b"geometry")
        self.back_animation.setDuration(500)
        self.back_animation.setEasingCurve(QEasingCurve.InQuad)
        self.start_animation = QPropertyAnimation(self.start,b"geometry")
        self.start_animation.setDuration(500)
        self.start_animation.setEasingCurve(QEasingCurve.InQuad)
        self.backup_animation = QPropertyAnimation(self.backbutton,b"geometry")
        self.backup_animation.setDuration(500)
        self.backup_animation.setEasingCurve(QEasingCurve.InQuad)
        self.backdown_animation = QPropertyAnimation(self.backbutton,b"geometry")
        self.backdown_animation.setDuration(500)
        self.backdown_animation.setEasingCurve(QEasingCurve.InQuad)
        self.player1_time = 600 #player1 for white
        self.player2_time = 600 #player2 for black
        self.list_numb = []
        self.list_numw = []
        for i in range(4):
            num_padb = numpadb(self)
            self.list_numb.append(num_padb)
            self.list_numb[i].setGeometry(QRect(WINDOW_WIDTH - (i + 1) * NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
            self.list_numb[i].hide()
        for i in range(4):
            num_padw = numpadw(self)
            self.list_numw.append(num_padw)
            self.list_numw[i].setGeometry(QRect(0,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
            self.list_numw[i].hide()
        self.board.player1_timer.timeout.connect(self.addTime1)
        self.board.player2_timer.timeout.connect(self.addTime2)
        self.rope.back_signal.connect(self.startAnimation)
        self.rope.move_signal.connect(self.move_start)
        self.start_animation.finished.connect(self.start_select)        
        self.select1.change2.connect(self.change_select2)
        self.select2.change1.connect(self.change_select1)
        self.chooseb.go_b.connect(self.start_fade)
        self.choosew.go_w.connect(self.start_fade)

        self.openleft_animation.finished.connect(self.start_game)
        self.fadetimer.timeout.connect(self.choosew.fade)
        self.fadetimer.timeout.connect(self.chooseb.fade)
        self.fadetimer.timeout.connect(self.select1.fade)
        self.fadetimer.timeout.connect(self.select2.fade)
        self.fadetimer.timeout.connect(self.pvp.fade)
        self.fadetimer.timeout.connect(self.pve.fade)
        self.select1.stop_timer.connect(self.door_open)
        self.appeartimer.timeout.connect(self.select1.appear)
        self.appeartimer.timeout.connect(self.select2.appear)
        #self.choosew.stop_timer.connect(self.start_game)
        self.select1.stop_appear.connect(self.appeartimer.stop)
        self.pvp.pvp_select.connect(self.start_fade)
        self.pve.pvp_select.connect(self.start_appear)
        
        self.pvp.pvp_select.connect(self.door_open)
        self.board.victory.connect(self.victory_scene)
        self.pic_ready.connect(self.vic_scene.scaletimer.start)
        self.pic_ready.connect(self.vic_scene.show)
        self.vic_scene.victory_finished.connect(self.door_close)
        self.closeleft_animation.finished.connect(self.restart)
        self.backbutton.up.connect(self.back_up)
        self.backbutton.down.connect(self.back_down)
        self.backbutton.back.connect(self.board.regret)
    def back_down(self):
        self.backdown_animation.setStartValue(QRect(self.backbutton.pos().x(),self.backbutton.pos().y(),BUTTON_WIDTH,BUTTON_HEIGHT))
        self.backdown_animation.setEndValue(QRect(self.backbutton.pos().x(),-64,BUTTON_WIDTH,BUTTON_HEIGHT))
        self.backdown_animation.start()
    def back_up(self):
        self.backup_animation.setStartValue(QRect(self.backbutton.pos().x(),self.backbutton.pos().y(),BUTTON_WIDTH,BUTTON_HEIGHT))
        self.backup_animation.setEndValue(QRect(self.backbutton.pos().x(),0,BUTTON_WIDTH,BUTTON_HEIGHT))
        self.backup_animation.start()
    def restart(self):
        global board_list
        global win_x
        global win_y
        global win_x_f
        global win_y_f
        global your_choose
        global start_handle
        global count_white
        global count_black
        global cursor_x
        global cursor_y
        global black_or_white
        global last_chess_type
        global last_cursor_x
        global last_cursor_y
        global rope_under_click
        global select1_clicked
        global select2_clicked
        global pvp_flag
        global victor
        global enable_chess
        for i in range(15):
            for j in range(15):
                board_list[i][j] = 0
        win_x = 0
        win_y = 0
        win_x_f = 0
        win_y_f = 0
        your_choose = 0 #0 for white and 1 for black
        start_handle = 1
        count_white = 0
        count_black = 0
        cursor_x = 0
        cursor_y = 0
        black_or_white = 1 #0 for white and 1 for black
        last_chess_type = 0 #128 for empty 255 for black 0 for white
        last_cursor_x = 0#remain the last chess
        last_cursor_y = 0
        rope_under_click = 0
        select1_clicked = 0
        select2_clicked = 0
        pvp_flag = 0 #0 for pvp and 1 for pve
        victor = 0 #1 for white and 2 for black
        enable_chess = 0
        self.player1_time = 600 #player1 for white
        self.player2_time = 600 #player2 for black
        self.board.restart()
        self.door_left.restart()
        self.door_right.restart()
        self.vic_scene.restart()
        self.pvp.restart()
        self.pve.restart()
        self.choosew.restart()
        self.chooseb.restart()
        self.select1.restart()
        self.select2.restart()
    def door_close(self):
        for i in range(4):
            self.list_numb[i].hide()
            self.list_numw[i].hide()
        self.closeleft_animation.setStartValue(QRect(self.door_left.pos().x(),self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.closeright_animation.setStartValue(QRect(self.door_right.pos().x(),self.door_right.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.closeleft_animation.setEndValue(QRect(0,self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.closeright_animation.setEndValue(QRect(512,self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.closeleft_animation.start()
        self.closeright_animation.start()
        self.restart_ready.emit()
    def door_open(self):
        self.openleft_animation.setStartValue(QRect(self.door_left.pos().x(),self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.openleft_animation.setEndValue(QRect(DOORLEFT_OFFSET_X,self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.openright_animation.setStartValue(QRect(self.door_right.pos().x(),self.door_right.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.openright_animation.setEndValue(QRect(DOORRIGHT_OFFSET_X,self.door_left.pos().y(),DOOR_WIDTH,DOOR_HEIGHT))
        self.openleft_animation.start()
        self.openright_animation.start()
    def victory_scene(self):
        self.board.repaint()
        winid = self.winId()
        screen = QGuiApplication.primaryScreen()
        screen.grabWindow(winid).save("src/123.jpg")
        self.pic_ready.emit()
    def start_appear(self):
        self.select1.show()
        self.select2.show()
        self.appeartimer.start()
    def start_fade(self):
        self.fadetimer.start()
    def start_game(self):
        global your_choose
        self.fadetimer.stop()
        self.chooseb.hide()
        self.choosew.hide()
        self.select1.hide()
        self.select2.hide()
        self.board.show()
        self.board.start_chess.emit()
    def change_select1(self):
        self.select1.setPixmap(QPixmap.fromImage(self.select1.select_image_1_1))
        self.chooseb.setGeometry(QRect(SELECT2_OFFSET_X + SELECT_WIDTH + 20,SELECT2_OFFSET_Y,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.choosew.setGeometry(QRect(SELECT2_OFFSET_X + SELECT_WIDTH + 20 + 35,SELECT2_OFFSET_Y,CHOOSE_WIDTH,CHOOSE_HEIGHT))
    def change_select2(self):
        self.select2.setPixmap(QPixmap.fromImage(self.select2.select_image_2_1))
        self.chooseb.setGeometry(QRect(SELECT1_OFFSET_X + SELECT_WIDTH + 20,SELECT1_OFFSET_Y,CHOOSE_WIDTH,CHOOSE_HEIGHT))
        self.choosew.setGeometry(QRect(SELECT1_OFFSET_X + SELECT_WIDTH + 20 + 35,SELECT1_OFFSET_Y,CHOOSE_WIDTH,CHOOSE_HEIGHT))
    def start_select(self):
        global start_handle
        #self.select1.setGeometry(QRect(SELECT1_OFFSET_X,SELECT1_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.pvp.show()
        #self.select2.setGeometry(QRect(SELECT2_OFFSET_X,SELECT2_OFFSET_Y,SELECT_WIDTH,SELECT_HEIGHT))
        self.pve.show()
        start_handle = 1
    def move_start(self):
        self.start.setGeometry(QRect(0,0 - 4 * (self.rope.pos().y() - ROPE_OFFSET_Y),WINDOW_WIDTH,WINDOW_HEIGHT))
    def startAnimation(self):
        self.back_animation.setStartValue(QRect(self.rope.pos().x(),self.rope.pos().y(),ROPE_WIDTH,ROPE_HEIGHT))
        self.back_animation.setEndValue(QRect(ROPE_OFFSET_X,-ROPE_HEIGHT,ROPE_WIDTH,ROPE_HEIGHT))       
        self.start_animation.setStartValue(QRect(self.start.pos().x(),self.start.pos().y(),WINDOW_WIDTH,WINDOW_HEIGHT))
        self.start_animation.setEndValue(QRect(self.start.pos().x(),-WINDOW_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT))
        self.back_animation.start()
        self.start_animation.start()
    def addTime1(self):
        if self.player1_time >= 0:
            self.player1_time -= 1
            if self.player1_time >= 0 and self.player1_time < 10:
                self.list_numw[0].shownum(self.player1_time)
                self.list_numw[1].hide()
                self.list_numw[2].hide()
                self.list_numw[3].hide()
            if self.player1_time >= 10 and self.player1_time < 100:
                self.list_numw[0].setGeometry(QRect(NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[1].shownum(self.player1_time // 10)
                self.list_numw[0].shownum(self.player1_time % 10)
                self.list_numw[2].hide()
                self.list_numw[3].hide()
            if self.player1_time >= 100 and self.player1_time < 1000:
                self.list_numw[0].setGeometry(QRect(2 * NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[1].setGeometry(QRect(NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[2].shownum(self.player1_time // 100)
                self.list_numw[1].shownum((self.player1_time % 100) // 10)
                self.list_numw[0].shownum(self.player1_time % 10)
                self.list_numw[3].hide()
            if self.player1_time >= 1000 and self.player1_time <= 9999:
                self.list_numw[0].setGeometry(QRect(3 * NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[1].setGeometry(QRect(2 * NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[2].setGeometry(QRect(NUMPAD_OFFSET,NUMPAD_OFFSET,NUM_SIZE,NUM_SIZE))
                self.list_numw[3].shownum(self.player1_time // 1000)
                self.list_numw[2].shownum((self.player1_time % 1000) // 100)
                self.list_numw[1].shownum((self.player1_time % 100) // 10)
                self.list_numw[0].shownum(self.player1_time % 10)
            #print(self.player1_time)
    def addTime2(self):
        if self.player2_time >= 0:
            self.player2_time -= 1
            if self.player2_time >= 0 and self.player2_time < 10:
                self.list_numb[0].shownum(self.player2_time)
                self.list_numb[1].hide()
                self.list_numb[2].hide()
                self.list_numb[3].hide()
            if self.player2_time >= 10 and self.player2_time < 100:
                self.list_numb[1].shownum(self.player2_time // 10)
                self.list_numb[0].shownum(self.player2_time % 10)
                self.list_numb[2].hide()
                self.list_numb[3].hide()
            if self.player2_time >= 100 and self.player2_time < 1000:
                self.list_numb[2].shownum(self.player2_time // 100)
                self.list_numb[1].shownum((self.player2_time % 100) // 10)
                self.list_numb[0].shownum(self.player2_time % 10)
                self.list_numb[3].hide()
            if self.player2_time >= 1000 and self.player2_time <= 9999:
                self.list_numb[3].shownum(self.player2_time // 1000)
                self.list_numb[2].shownum((self.player2_time % 1000) // 100)
                self.list_numb[1].shownum((self.player2_time % 100) // 10)
                self.list_numb[0].shownum(self.player2_time % 10)
            #print(self.player2_time)
app = QApplication(sys.argv)
gobang_mainwindow = gobang_gui()
gobang_mainwindow.show()

sys.exit(app.exec_())
print(1)
os.system("pause")
