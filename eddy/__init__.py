"""
Python module for a simple, threaded progress spinner.
"""
from . import spinner

_spin = None

def start(msg='waiting', name='classic'):
    """
    Start function for spinner.
    """
    global _spin
    
    _spin = spinner.Spinner(msg,name)
    _spin.start()

def stop():
    """
    Stop function for spinner
    """
    global _spin

    if _spin is not None:
        _spin.stop()
