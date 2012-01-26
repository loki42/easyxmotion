#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
##
## Copyright 2012
## Author: Loki Davison <loki.davison@gravityfour.com>
## gravityfour.com and musicfilmcomedy.com
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of 
## the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""
A Easy motion style window switcher.

inspired by the vim plugin:
https://github.com/Lokaltog/vim-easymotion

"""
import time, string
import wnck
import pyosd
from Xlib.display import Display
from Xlib import X, XK
import sys
import operator

# Config values
font = "-monotype-arial-bold-r-normal--75-0-0-0-p-0-iso8859-15"
colour = 'red'
outline_colour = 'black'
#

timestamp = int(time.time())

def display_osd():
    s = wnck.screen_get_default()
    s.force_update()
    windows = s.get_windows()
    osds = []
    ws = s.get_active_workspace()

    windows = sorted(windows, key=operator.methodcaller("get_pid"))
    windows = [window for window in windows if window.is_visible_on_workspace(ws)]

    for i, window in enumerate(windows):
        if window.is_visible_on_workspace(ws):
            osd = pyosd.osd(font)
            osd.set_timeout(-1)
            osd.set_colour(colour)
            osd.set_outline_offset(1)
            osd.set_outline_colour(outline_colour)
            osd.set_shadow_offset(2)
            x, y  = window.get_geometry()[:2]
            osd.set_horizontal_offset(x)
            osd.set_vertical_offset(y)
            # XXX explodes if more than 26 windows are visable.
            osd.display(string.lowercase[i])
            osds.append(osd)
    return osds, windows

def main():
    # current display
    osds, windows = display_osd()
    disp = Display()
    root = disp.screen().root

    # grab all lowercase key presses. No mechanism to change your mind and not jump.
    root.change_attributes(event_mask = X.KeyPressMask)
    for keycode in [disp.keysym_to_keycode(XK.string_to_keysym(a)) for a in string.lowercase]:
        root.grab_key(keycode, 0, 1, X.GrabModeAsync, X.GrabModeAsync)

    while True:
        event = root.display.next_event()
        keycode = event.detail
        if event.type == X.KeyPress:
            key = XK.keysym_to_string(disp.keycode_to_keysym(keycode, 0))
            windows[string.lowercase.index(key)].activate(timestamp)
            sys.exit()

if __name__ == '__main__':
    main()
