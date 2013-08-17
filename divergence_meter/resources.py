"""
This module contain all resources.
"""

#os imports
from os import path

#sys imports
import sys


###############################################################################
# PATHS
###############################################################################

#Path of project
project_path = path.abspath(path.dirname(__file__))

#Only for py2exe
frozen = getattr(sys, 'frozen', '')
if frozen in ('dll', 'console_exe', 'windows_exe'):
    # py2exe:
    project_path = path.abspath(path.dirname(sys.executable))

#Path of style file
style_file = path.join(project_path, 'resources', 'style.qss')


###############################################################################
# IMAGES
###############################################################################

#Main window icon
main_icon = path.join(project_path, 'images', 'DM-icon.png')

#Images for tubes
IMAGES = [path.join(project_path, 'images', 'point.png'),
          path.join(project_path, 'images', '0.png'),
          path.join(project_path, 'images', '1.png'),
          path.join(project_path, 'images', '2.png'),
          path.join(project_path, 'images', '3.png'),
          path.join(project_path, 'images', '4.png'),
          path.join(project_path, 'images', '5.png'),
          path.join(project_path, 'images', '6.png'),
          path.join(project_path, 'images', '7.png'),
          path.join(project_path, 'images', '8.png'),
          path.join(project_path, 'images', '9.png')]
