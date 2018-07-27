import sys
import time
import threading
import logging
# local config
from . import config

logger = logging.getLogger(__name__)

class Spinner(object):
    """
    Spinner class for rotating or animating things while you wait.
    """

    @staticmethod
    def spinning_cursor(msg,charset):
        while 1: 
            for cursor in charset: yield msg+': '+cursor+' '

    def __init__(self, msg='waiting', preset='classic', delay=None):
        super(Spinner, self).__init__()

        self.msg = msg
        self.busy = False

        if preset not in config.presets:
            logger.warn(f'Unknown preset, {preset}, using "classic".')
            preset = 'classic'
        
        self.iterable = config.presets[preset][1]
        self.delay = config.presets[preset][0]
        
        if delay is not None: 
            self.delay = delay

        # determine number of delete chars from first item in iterable and
        # msg length
        self.delchar = 3 + len(msg) + len(self.iterable[0])

        # Define generator that advances through iterable
        self.spin_gen = self.spinning_cursor(self.msg, self.iterable)

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spin_gen))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b'*self.delchar)
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task, daemon=True).start()  

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
        sys.stdout.write('\n')
        sys.stdout.flush()