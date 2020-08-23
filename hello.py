#export PATH="$PATH:/usr/local/bin/python-gi3"
import sys
print(sys.path)

import gi as Gtk
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
