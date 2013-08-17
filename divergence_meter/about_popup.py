"""
This module contain aboutWidget()
"""

#divergence_meter imports
from . import __prj__
from . import __source__
from . import __license__
from . import __version__
from . import __author__

#PyQt4.QtGui imports
from PyQt4.QtGui import QDesktopWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QWidget

#PyQt4.QtCore imports
from PyQt4.QtCore import QPoint
from PyQt4.QtCore import Qt


class aboutWidget(QWidget):

    def __init__(self, parent):
        super(aboutWidget, self).__init__()
        #Set popup
        self.setWindowFlags(Qt.Popup)
        self.resize(parent.meter.width(), 307)
        self.setWindowOpacity(0.5)

        #Move aboutWidget
        if parent.isFullScreen():
            resolution = QDesktopWidget().screenGeometry()
            self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                    (resolution.height() / 2) - (self.frameSize().height() / 2))
        else:
            point = parent.meter.rect().topRight()
            global_point = parent.meter.mapToGlobal(point)
            self.move(global_point - QPoint(self.width(), 0))

        #Create vertical layout
        vbox = QVBoxLayout(self)

        #Set align and margins
        if parent.isFullScreen():
            vbox.setAlignment(Qt.AlignLeft)
            vbox.setContentsMargins(150, 0, 0, 0)
        else:
            vbox.setAlignment(Qt.AlignHCenter)
            vbox.setContentsMargins(0, 0, 0, 0)

        vbox.setSpacing(0)

        #LABELS
        #name and version
        label_name = QLabel('%s (%s)' % (__prj__, __version__))
        label_name.setObjectName('name')

        #label_url
        label_url = QLabel('Source: %s' % (__source__))

        #label_license
        label_license = QLabel('License: %s' % (__license__))

        #label_author
        label_author = QLabel(__author__)
        label_author.setObjectName('author')

        #Add widget to vbox
        vbox.addWidget(label_name)
        vbox.addWidget(label_license)
        vbox.addWidget(label_url)
        vbox.addWidget(label_author)

        self.setLayout(vbox)
