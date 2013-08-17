# This file is part of Divergence Meter
#
# Divergence Meter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Divergence Meter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LoL Server Status. If not, see <http://www.gnu.org/licenses/>.
#
# Source: <https://github.com/LuqueDaniel/Divergence-Meter.git>


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
