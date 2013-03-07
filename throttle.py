import collections
import time

class Throttler:
    def __init__(self, frame, limit):
        self.frame, self.limit = frame, limit
        self.log = collections.deque()

    def _clean(self):
        while len(self.log) and time.time() > self.log[0] + self.frame:
            self.log.popleft()

    def ttl(self):
        if len(self.log) == 0:
            return 0
        return max(int(self.log[0] + self.frame - time.time()), 0)

    def ready(self):
        return len(self.log) < self.limit

    def wait(self):
        while not self.ready():
            time.sleep(self.ttl())
            self._clean()

    def register(self):
        self.wait()
        time.sleep(self.frame / self.limit)
        self.log.append(time.time())
        return
