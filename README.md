# android-locale-hack
--------------------- 
These are my notes on hacking around the problem of getting the default locale
in a Python application running on Android, including a simple example on the
best method I've found so far.

Android's builtin version of libc, called bionic, doesn't have any concept of
locale. Usually, when (cross-)compiling Python for
[Android](https://github.com/kivy/pyjnius), a
[patch](https://github.com/kivy/pyjnius) for removing any parts of the Python
source which mention LC_* is used before (cross-)compiling.

Another method for working around the locale problem on Android is in Google's
alpha version of
[python3-for-android](https://code.google.com/p/python-for-android/source/browse/python3-alpha/?r=70d4f7c707c4e937ee7198aa8f01aaec3f12d708),
which ships
[an alternate ```locale``` module](https://code.google.com/p/python-for-android/source/browse/python3-alpha/python3-src/Lib/locale.py?r=70d4f7c707c4e937ee7198aa8f01aaec3f12d708)
that tries to import ```_locale``` from the standard library, and if that
fails, it falls back to emulating a normal libc's C-Types for LC_* in a series
of Python functions.

## fuck android
---------------
I don't want to fix a crappily designed operating system. I just want the
Python apps that I write for normal systems that use a normal libc to just
fucking work. Therefore, I'm resorting to cheap hacks.

One way to hack around this is to use
[pyjnius](https://github.com/kivy/pyjnius) to wrap the
[```java.util.Locale```](https://developer.android.com/reference/java/util/Locale.html)
class in a Python class, and use the Python wrapper to ask AOS's JVM for the
default locale. See ```locale-hack.py``` for a working version of this, which I
ran on [QPython](https://github.com/rumca-js/Qpython) (and
[here](https://play.google.com/store/apps/details?id=com.hipipal.qpyplus) is
QPython on the Google Play store) simply because it provides easy download of
pyjnius.
