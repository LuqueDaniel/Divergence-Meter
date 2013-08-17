# -*- coding: utf-8 -*-
#
# This file is part of Divergence Meter
#
# LoL Server Status is free software: you can redistribute it and/or modify
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
# Source: <>


#LoL Server status imports
from divergence_meter import resources
import divergence_meter

#setuptools imports
from setuptools import find_packages

#distutils.core imports
from distutils.core import setup

#py2exe
import py2exe


packages = find_packages()


information = {'script': 'divergence_meter.py',
              'Version': divergence_meter.__version__,
              'copyright': divergence_meter.__license__,
              'name': divergence_meter.__prj__,
              'dest_base': divergence_meter.__prj__,
              'icon_resources': [(1, 'windows_icon.ico')]}


#Add resources files
resources_files = [('images', []), ('resources', [])]

#Add images
for img in resources.IMAGES:
    resources_files[0][1].append(img)

#Add icon
resources_files[0][1].append(resources.main_icon)

#Add styles
resources_files[1][1].append(resources.style_file)


parameters = {
                'name': divergence_meter.__prj__,
                'version': divergence_meter.__version__,
                'description': divergence_meter.__docu__,
                'author': divergence_meter.__author__,
                'author_email': divergence_meter.__mail__,
                'license': divergence_meter.__license__,

                'windows': [information],

                'data_files': resources_files,
                'zipfile': None,
                'options': {
                    'py2exe': {
                        'dll_excludes': ['MSVCP90.dll'],
                        'compressed': 1,
                        'optimize': 2,
                        'includes': ['sip'],
                        'excludes': ['bsddb', 'curses', 'email',
                            'pywin.debugger', 'pywin.debugger.dbgcon',
                            'pywin.dialogs'],
                        'packages': packages,
                        'bundle_files': 1,
                        'dist_dir': 'dist',
                        'xref': False,
                        'skip_archive': False,
                        'ascii': False}
                    }
                }


setup(**parameters)
