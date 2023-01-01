# -*- coding: utf-8 -*-

def classFactory(iface):
    from .mms_foto_viewer import mms_foto_viewer
    return mms_foto_viewer(iface)
