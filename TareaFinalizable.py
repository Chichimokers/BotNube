import threading
import ctypes

class StoppableThread(threading.Thread):
    
    def __init__(self,  *args, **kwargs):

        super(StoppableThread, self).__init__(*args, **kwargs)

        self._stop_event = threading.Event()

    def stop(self):
        self.terminate_thread(self)

    def stopped(self):

        return self._stop_event.is_set()
