import time
import threading

class TimeoutException(Exception):
    pass

def timeout(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [TimeoutException('Time out')]
            
            def function_with_args():
                result[0] = func(*args, **kwargs)
            
            thread = threading.Thread(target=function_with_args)
            thread.start()
            thread.join(seconds)
            if thread.is_alive():
                try:
                    thread._stop()  # Принудительно завершаем поток
                except Exception as e:
                    del e
                    raise TimeoutException('Time out')
            return result[0]
        return wrapper
    return decorator

@timeout(2)
def some():
    time.sleep(2.1)
    return "Hello"

print(some())