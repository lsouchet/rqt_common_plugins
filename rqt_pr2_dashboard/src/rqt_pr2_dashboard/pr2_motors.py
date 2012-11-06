# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
from python_qt_binding.QtCore import QSize

from rqt_robot_dashboard.widgets import MenuDashWidget

class PR2Motors(MenuDashWidget):
    def __init__(self, context, reset_callback, halt_callback):
        super(PR2Motors, self).__init__(context, 'Motors')
        
        self.add_action('Reset', reset_callback)
        self.add_action('Halt', halt_callback)
        self.setToolTip('Motors')

        self._ok_icon = self.build_icon(['bg-green.svg', 'ic-motors.svg'])
        self._warn_icon = self.build_icon(['bg-yellow.svg', 'ic-motors.svg', 'ol-warn-badge.svg'])
        self._err_icon = self.build_icon(['bg-red.svg', 'ic-motors.svg', 'ol-err-badge.svg'])
        self._stale_icon = self.build_icon(['bg-grey.svg', 'ic-motors.svg', 'ol-stale-badge.svg'])

        self._ok_click = self.build_icon(['bg-green.svg', 'ic-motors.svg', 'ol-click.svg'])
        self._warn_click = self.build_icon(['bg-yellow.svg', 'ic-motors.svg', 'ol-warn-badge.svg', 'ol-click.svg'])
        self._err_click = self.build_icon(['bg-red.svg', 'ic-motors.svg', 'ol-err-badge.svg', 'ol-click.svg'])
        self._stale_click = self.build_icon(['bg-grey.svg', 'ic-motors.svg', 'ol-stale-badge.svg', 'ol-click.svg'])

        self._icons = [self._ok_icon, self._warn_icon, self._err_icon, self._stale_icon]
        self._clicked_icons = [self._ok_click, self._warn_click, self._err_click, self._stale_click]
        self.update_state(3)

        self.setFixedSize(self._icons[0].actualSize(QSize(50,30)))

    def set_ok(self):
        self.update_state(0)

    def set_warn(self):
        self.update_state(1)

    def set_error(self):
        self.update_state(2)

    def set_stale(self):
        self.update_state(3)
