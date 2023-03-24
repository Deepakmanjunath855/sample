from fastapi import FastAPI
from fastapi import Request
app = FastAPI()
import json
from pydantic import BaseModel
import threading
from thread_test import update_cache

class product(BaseModel):
    product_name:str
    id:int

cache={'product1':11}

@app.post("/get")
async def root(request:product):
    name =request.product_name
    print(f" {cache}")

    t1=threading.Thread(target=update_cache)
    t1.start()
    
    if name not in cache:
        cache[name]=request.id
        print("added to cache")
    else:
        print("already in cache")

    return {"cache":cache}