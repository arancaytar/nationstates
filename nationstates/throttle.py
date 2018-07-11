import collections
import time

class Throttler:
    '''A class for automatically throttling events. 
    This class should support multiple threads provided it is only instanced once.'''
    def __init__(self, frame, limit):
        '''Initialize a throttler that restricts events to happen <limit> number of 
        times in the last <frame> seconds.'''
        self.frame, self.limit = frame, limit
        self.log = collections.deque()

    def _clean(self):
        while len(self.log) and time.time() > self.log[0] + self.frame:
            self.log.popleft()

    def ttl(self):
        '''How much time will pass before the event is allowed to happen again.'''
        if len(self.log) == 0:
            return 0
        return max(int(self.log[0] + self.frame - time.time()), 0)

    def ready(self):
        '''Whether or not the event may now happen.'''
        return len(self.log) < self.limit

    def wait(self):
        '''Block the current thread until the event may happen again.'''
        while not self.ready():
            time.sleep(self.ttl())
            self._clean()

    def register(self):
        '''Register the event, blocking the thread if necessary.'''
        self.wait()
        time.sleep(self.frame / self.limit)
        self.log.append(time.time())
        return
