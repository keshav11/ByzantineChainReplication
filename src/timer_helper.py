from threading import Timer


class TimerHelper:

    def __init__(self):
        self.timer = None

    def start_timer(self, time_seconds, callback):
        print('Timer started')
        self.timer = Timer(time_seconds, callback)
        self.timer.start()

    def stop_timer(self):
        if self.timer.isAlive():
            self.timer.cancel()
        else:
            print('timer not alive')

if __name__ == "__main__":
    th = TimerHelper()
    f = lambda a : print(a)
    th.start_timer(1, f('1'))