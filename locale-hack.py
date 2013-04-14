#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# locale-hack.py
# --------------
# Get an Android device's default locale in Python.
#
# This script is intended to run in an installation of Python *on* an Android
# device. It was created using QPython, but should work on any
# python-for-android installation, or any Arm cross-compilation of Python which
# includes the modules androidhelper[1] and pyjynius[2].
#
# [1] https://python-for-android.googlecode.com/files/androidhelper.py
# [2] https://github.com/kivy/pyjnius
#
# :author: Isis Agora Lovecruft
# :license: AGPLv3
# :copyright: (c) 2013 Isis Agora Lovecruft
# :version: 0.0.1 

from jnius import autoclass
import androidhelper


current = None
droid = androidhelper.Android()

try:
    droid.makeToast(str("Importing locale module..."))
    import locale
except (ImportError, NameError) as exc:
    droid.makeToast(str(exc.message))
else:
    try:
        droid.makeToast(str("Attempting to get default locale from Python..."))
        current = locale.getdefaultlocale()
    except Exception as exc2:
        droid.makeToast(str(exc2.message))

if current and isinstance(current, tuple):
    if current == (None, None,):
        droid.makeToast(str("Unable to get locale from Python..."))
    else:
        try:
            droid.makeToast(str("Attempting to set local from Python..."))
            locale.setlocale('en_GB.ISO8859-1', 'UTF-8')
        except Exception as goddamnit:
            droid.makeToast(str(goddamnit.message))
            droid.makeToast(str("Available locales:"))
            droid.makeToast(str(locale.locale_alias))
        else:
            droid.makeToast(str("Success! Our locale is:"))
            current = locale.getlocale()
            droid.makeToast(str(current))

try:
    droid.makeToast(str("Attempting to get default locale from Java..."))
    JavaUtilLocale = autoclass('java.util.Locale')
    jlocale = JavaUtilLocale
    ourlocale = jlocale.getDefault()
except Exception as exc3:
    droid.makeToast(str("Unable to get locale from Java..."))
    droid.makeToast(str(exc3.message))
else:
    droid.makeToast(str("Success! Our locale is:"))
    droid.makeToast(str(ourlocale))
