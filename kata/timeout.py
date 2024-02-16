import signal

class TimeoutError(Exception):
    def __init__(self, value = "Timed Out"):
        self.value = value
    def __str__(self):
        return repr(self.value)

def timeout(seconds_before_timeout):
    def decorate(f):
        def handler(signum, frame):
            raise TimeoutError()
        def new_f(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds_before_timeout)
            try:
                result = f(*args, **kwargs)
            finally:
                # reinstall the old signal handler
                signal.signal(signal.SIGALRM, old)
                # cancel the alarm
                # this line should be inside the "finally" block (per Sam Kortchmar)
                signal.alarm(0)
            return result
        return new_f
    return decorate

if __name__ == "__main__":
    @timeout(2)
    def f():
        import time
        time.sleep(3)
        return 42

    try:
        print(f())
    except TimeoutError as e:
        print(e)  # Function 'f' timed out after 2 seconds
    except Exception as e:
        print(e)
    else:
        print("No exception")  # No exception