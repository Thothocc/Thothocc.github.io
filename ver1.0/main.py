from cgitb import reset
from msilib.schema import Class
import string
from fastapi import FastAPI
import pandas as pd
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from search_exchange import SearchObj

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

@app.get("/")
async def index():
    return "SJTU-IGEM"

@app.get("/mode")
async def choic_mode(flag: str):
    if flag == "GECKO":
        
        return 0
    else:

        return 1


@app.get("/objsearch")
async def objsearch(name:str):
    res = SearchObj(name)
    return {"res":res}

'''
@app.get("/search_2")
async def search_maxn(act: string, carb: string):
    # 此处有一个相关操作函数
    return res

@app.get("/search_3"):
async def search_key(): # 此处未完成
    # 此处有一个相关操作函数
    return res 

# 跳转链接无需后端接口

@app.get("/search_4")
async def search_keysub(): # 此处未完成
    #此处有一个相关操作函数
    return res 

@app.get("/upload")
async def upload_seq(): # 我还没想好怎么写
    

@app.get("/update")
async def update_kcat(): # 我还没想好怎么写
     
'''