"""
Python module for a simple, threaded progress spinner.
"""
from . import spinner

_spin = None

def start(msg='waiting', name='classic', custom=None):
    """
    Start function for spinner.
    """
    global _spin

    if custom is not None:
        delay, iterable = custom
        _spin = spinner.Spinner(msg=msg, iterable=iterable, delay=delay)
    else:
        _spin = spinner.Spinner(msg,name)

    _spin.start()

def stop():
    """
    Stop function for spinner
    """
    global _spin

    if _spin is not None:
        _spin.stop()
