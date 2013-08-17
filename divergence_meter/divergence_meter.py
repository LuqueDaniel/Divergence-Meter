#sys imports
import sys

#random imports
import random

#time imports
import time

#divergence_meter import
from . import __prj__
from . import __version__
from .resources import style_file
from .resources import main_icon
from .resources import IMAGES
from .core import change_pro_name
from .core import get_digit
from .about_popup import aboutWidget

#PyQt4.QtGui imports
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QIcon

#PyQt4.QtCore imports
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import QSettings


class divergenceMeterWidget(QWidget):

    def __init__(self, parent):
        super(divergenceMeterWidget, self).__init__()
        self.parent = parent
        self.l_size = QSize(104, 307)
        self.setUpdatesEnabled(True)

        #Create labels
        self.tube_1 = QLabel()
        self.tube_2 = QLabel()
        self.tube_3 = QLabel()
        self.tube_4 = QLabel()
        self.tube_5 = QLabel()
        self.tube_6 = QLabel()
        self.tube_7 = QLabel()
        self.tube_8 = QLabel()

        #Create horizontal layyout
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setAlignment(Qt.AlignHCenter)
        self.h_layout.setSpacing(0)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        #Add labels to horizontal layout
        self.h_layout.addWidget(self.tube_1)
        self.h_layout.addWidget(self.tube_2)
        self.h_layout.addWidget(self.tube_3)
        self.h_layout.addWidget(self.tube_4)
        self.h_layout.addWidget(self.tube_5)
        self.h_layout.addWidget(self.tube_6)
        self.h_layout.addWidget(self.tube_7)
        self.h_layout.addWidget(self.tube_8)

        #Generate random line
        self.generate_random_line()

        self.setLayout(self.h_layout)

    def generate_random_line(self):
        """This function generate a random line"""

        self.tube_1.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_2.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))
        self.tube_3.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_4.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_5.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_6.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_7.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.tube_8.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
        self.repaint()

    def generate_new_random_lines(self):
        """Generate 100 random lines"""

        for i in range(100):
            self.tube_1.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_2.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))
            self.tube_3.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_4.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_5.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_6.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_7.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.tube_8.setPixmap(QPixmap(IMAGES[random.randint(1, 10)]).scaled(self.l_size))
            self.repaint()

    def generate_random_digits(self):
        """Random results"""

        for i in range(100):
            self.tube_1.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_2.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_3.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_4.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_5.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_6.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_7.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.tube_8.setPixmap(QPixmap(IMAGES[random.randint(0, 10)]).scaled(self.l_size))
            self.repaint()

    def show_date(self):
        """Display date"""

        self.generate_random_digits()

        self.is_running_date = True

        while self.is_running_date is True:
            clock = time.localtime()

            year = str(clock.tm_year)
            mon = str(clock.tm_mon)
            day = str(clock.tm_mday)

            self.parent.setWindowTitle('Divergence Meter - %s' % time.strftime(
                                        '%m/%d/%Y', clock))

            app.processEvents()

            if len(mon) == 1:
                self.tube_1.setPixmap(QPixmap(IMAGES[1]).scaled(self.l_size))
                self.tube_2.setPixmap(QPixmap(IMAGES[get_digit(mon)]).scaled(self.l_size))
            else:
                self.tube_1.setPixmap(QPixmap(IMAGES[get_digit(mon[0])]).scaled(self.l_size))
                self.tube_2.setPixmap(QPixmap(IMAGES[get_digit(mon[1])]).scaled(self.l_size))

            self.tube_3.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))

            if len(day) == 1:
                self.tube_4.setPixmap(QPixmap(IMAGES[1]).scaled(self.l_size))
                self.tube_5.setPixmap(QPixmap(IMAGES[get_digit(day)]).scaled(self.l_size))
            else:
                self.tube_4.setPixmap(QPixmap(IMAGES[get_digit(day[0])]).scaled(self.l_size))
                self.tube_5.setPixmap(QPixmap(IMAGES[get_digit(day[1])]).scaled(self.l_size))

            self.tube_6.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))

            self.tube_7.setPixmap(QPixmap(IMAGES[get_digit(year[2])]).scaled(self.l_size))
            self.tube_8.setPixmap(QPixmap(IMAGES[get_digit(year[3])]).scaled(self.l_size))

            app.processEvents()

    def show_time(self):
        """Display time"""

        self.generate_random_digits()

        self.is_running_time = True

        while self.is_running_time is True:
            clock = time.localtime()

            hour = str(clock.tm_hour)
            mins = str(clock.tm_min)
            sec = str(clock.tm_sec)

            self.parent.setWindowTitle('Divergence Meter - %s' % time.strftime(
                                        '%H:%M:%S', clock))

            app.processEvents()

            if len(hour) == 1:
                self.tube_1.setPixmap(QPixmap(IMAGES[1]).scaled(self.l_size))
                self.tube_2.setPixmap(QPixmap(IMAGES[get_digit(hour)]).scaled(self.l_size))
            else:
                self.tube_1.setPixmap(QPixmap(IMAGES[get_digit(hour[0])]).scaled(self.l_size))
                self.tube_2.setPixmap(QPixmap(IMAGES[get_digit(hour[1])]).scaled(self.l_size))

            self.tube_3.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))

            if len(mins) == 1:
                self.tube_4.setPixmap(QPixmap(IMAGES[1]).scaled(self.l_size))
                self.tube_5.setPixmap(QPixmap(IMAGES[get_digit(mins)]).scaled(self.l_size))
            else:
                self.tube_4.setPixmap(QPixmap(IMAGES[get_digit(mins[0])]).scaled(self.l_size))
                self.tube_5.setPixmap(QPixmap(IMAGES[get_digit(mins[1])]).scaled(self.l_size))

            self.tube_6.setPixmap(QPixmap(IMAGES[0]).scaled(self.l_size))

            if len(sec) == 1:
                self.tube_7.setPixmap(QPixmap(IMAGES[1]).scaled(self.l_size))
                self.tube_8.setPixmap(QPixmap(IMAGES[get_digit(sec)]).scaled(self.l_size))
            else:
                self.tube_7.setPixmap(QPixmap(IMAGES[get_digit(sec[0])]).scaled(self.l_size))
                self.tube_8.setPixmap(QPixmap(IMAGES[get_digit(sec[1])]).scaled(self.l_size))

            app.processEvents()


class divergenceMeterWindow(QMainWindow):

    def __init__(self):
        super(divergenceMeterWindow, self).__init__()
        self.setMaximumSize(832, 307)
        #Load settings
        self.load_settings()
        self.setWindowTitle('Divergence Meter')

        self.meter = divergenceMeterWidget(self)
        self.setCentralWidget(self.meter)

    def load_settings(self):
        """Load all settings"""
        qsettings = QSettings()

        self.move(qsettings.value('MainWindow/pos',
                self.frameGeometry().center()).toPoint())

    def save_settings(self):
        """Save all settings"""

        qsettings = QSettings()

        qsettings.setValue('MainWindow/pos', self.pos())

    def keyPressEvent(self, e):
        """This function catch key press events"""

        if (e.key() == Qt.Key_Enter) or (e.key() == Qt.Key_Return):
            if hasattr(self.meter, 'is_running_date'):
                self.meter.is_running_date = False
            elif hasattr(self.meter, 'is_running_time'):
                self.meter.is_running_time = False

            self.meter.generate_new_random_lines()
        elif e.key() == Qt.Key_D:
            if hasattr(self.meter, 'is_running_time'):
                self.meter.is_running_time = False

            self.meter.show_date()
        elif e.key() == Qt.Key_T:
            if hasattr(self.meter, 'is_running_date'):
                self.meter.is_running_date = False

            self.meter.show_time()
        elif e.key() == Qt.Key_Escape:
            self.about = aboutWidget(self)
            self.about.show()

    def mouseDoubleClickEvent(self, e):
        """This function catch mouse double click"""

        if e.button() == Qt.LeftButton:
            if self.isFullScreen():
                self.setWindowState(Qt.WindowNoState)
            else:
                self.setWindowState(Qt.WindowFullScreen)

    def closeEvent(self, e):
        """Catch close event"""

        if hasattr(self.meter, 'is_running_date'):
            self.meter.is_running_date = False
        elif hasattr(self.meter, 'is_running_time'):
            self.meter.is_running_time = False

        self.save_settings()


def run():
    #Change process name only GNU/Linux
    change_pro_name()

    #Set global var
    global app
    app = QApplication(sys.argv)

    #Set application parameters
    QCoreApplication.setOrganizationName(__prj__)
    QCoreApplication.setApplicationName(__prj__)
    QCoreApplication.setApplicationVersion(__version__)

    #Add style sheet
    with open(style_file, 'r') as f:
        style = f.read()
        app.setStyleSheet(style)

    app.setWindowIcon(QIcon(main_icon))

    window = divergenceMeterWindow()
    window.show()

    sys.exit(app.exec_())
