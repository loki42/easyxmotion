## Easyxmotion
A Easy motion style window switcher.

### How it works
To focus any visible window just launch easyxmotion usually with a shortcut (i use the menu key), then it displays letters on each window, type that letter to jump to the window. 

Should work with any window manager that supports [EWMH](http://en.wikipedia.org/wiki/Extended_Window_Manager_Hints). It probably only makes sense with tiling window managers. I've tested it only with XMonad. My dotfiles repo has the xmonad config.

inspired by the [easymotion vim plugin](https://github.com/Lokaltog/vim-easymotion).

This is the first open source project by [Gravity Four](http://www.gravityfour.com).

## Dependencies

Easyxmotion requires python, python xlib, pyosd and python wnck. To get these on ubuntu:
> sudo apt-get install python-xlib python-pyosd python-wnck

If you're using libxosd patched for truetype font support (XFT) you'll need to change the font in the code.

## Installing
just put it somewhere in your path.

Thanks to Noon for enthusiastic support. 
