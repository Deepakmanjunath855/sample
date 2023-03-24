import threading



data={'prodct20':886363,'product21':8783838,'product22':78787979,"product23":87728723}
cache={}
def update_cache():
    lock=threading.Lock()
    with lock:
        for item in data:
            cache[item]=data[item]
            print(cache)

