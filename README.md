These are my notes on hacking around the problem of getting the default locale
in a Python application running on Android, including a simple example on
the best method I've found so far.

Android's builtin version of libc, called bionic, doesn't have any concept of
locale. Usually, when (cross-)compiling Python for
[Android](https://github.com/kivy/pyjnius), a
[patch](https://github.com/kivy/pyjnius) for removing any parts of the Python
source which mention LC_* is used before (cross-)compiling.

One way to hack around this is to use
[pyjnius](https://github.com/kivy/pyjnius) to wrap the
[```java.util.Locale```](https://developer.android.com/reference/java/util/Locale.html)
class in a Python class, and use the Python wrapper to ask AOS's JVM for the
default locale.
