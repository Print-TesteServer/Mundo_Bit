import time

class Timer():
    def __init__(self):
        self.lastTime = time.time()
        self.isPaused = False
        self.goPause = False
        self.timePaused = 0.0

    def getTimer(self):
        returnTime = None
        if self.isPaused:
            if not self.goPause:
                self.goPause = True
                self.timePaused = time.time() - self.lastTime
                returnTime = self.timePaused
            else:
                returnTime = self.timePaused
        else:
            returnTime = time.time() - self.lastTime

        return returnTime

    def pauseTimer(self):
        self.isPaused = True

    def resumeTimer(self):
        if self.isPaused:
            self.lastTime += (time.time() - self.lastTime) - self.timePaused
            self.isPaused = False

    def resetTimer(self):
        self.lastTime = time.time()