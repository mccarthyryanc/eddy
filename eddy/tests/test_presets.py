"""
Some simple tests
"""
import time
import eddy
from eddy import config as edconf


def test_presets():
    """
    Display each present
    """
    print('')
    for preset in edconf.presets:
        eddy.start(msg=f'preset: {preset}',iterable=preset, delay=0.05)
        time.sleep(1)
        eddy.stop()