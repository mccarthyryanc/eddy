"""
Python module for a simple, threaded progress spinner.
"""
from . import spinner

_spin = None

def start(msg='waiting', iterable='pulse-plus', delay=None):
    """
    Start function for spinner.
    """
    global _spin

    _spin = spinner.Spinner(msg=msg, iterable=iterable, delay=delay)
    _spin.start()

def stop():
    """
    Stop function for spinner
    """
    global _spin

    if _spin is not None:
        _spin.stop()
