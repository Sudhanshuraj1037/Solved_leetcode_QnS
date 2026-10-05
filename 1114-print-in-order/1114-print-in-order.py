from threading import Semaphore

class Foo:

    def __init__(self):
        self.second_sem = Semaphore(0)
        self.third_sem = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.second_sem.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_sem.acquire()
        printSecond()
        self.third_sem.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_sem.acquire()
        printThird()