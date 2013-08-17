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


#sys imports
import sys


def change_pro_name():

    #Change the process name only for GNU/Linux
    #Since kernel version 2.6.9
    if sys.platform != 'win32' and sys.platform != 'darwin':
        try:
            from ctypes import CDLL
            libc = CDLL('libc.so.6')  # Loading C library
            procname = 'LoLServerStatus'
            #Change process name
            #15 value is PR_SET_NAME see "/usr/include/linux/prctl.h"
            libc.prctl(15, '%s\0' % procname, 0, 0, 0)
        except:
            pass


def get_digit(digit):
    """This function return index value of IMAGES list"""

    digit = int(digit)

    if digit == 0:
        return 1
    elif digit == 1:
        return 2
    elif digit == 2:
        return 3
    elif digit == 3:
        return 4
    elif digit == 4:
        return 5
    elif digit == 5:
        return 6
    elif digit == 6:
        return 7
    elif digit == 7:
        return 8
    elif digit == 8:
        return 9
    elif digit == 9:
        return 10
