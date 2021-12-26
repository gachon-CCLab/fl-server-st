from typing import Optional
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI

#버킷과 파일 이름은 여기서 결정된다. 다른 곳에서는 이 값을 받아와 사용
#
class ServerStatus(BaseModel):
    S3_bucket: str = 'ccl-fl-demo-model'
    S3_key: str = 'model.h5'  # 모델 가중치 파일 이름
    FLSeReady: bool = False


app = FastAPI()

FLSe = ServerStatus()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/FLSe/info")
def read_status():
    return {"Server_Status": FLSe}


@app.put("/FLSe/FLSeUpdate")
def update_item(Se: ServerStatus):
    global FLSe
    FLSe = Se
    return {"Server_Status": FLSe}

@app.put("/FLSe/FLSeReady")
def update_item(Se: bool):
    global FLSe
    FLSe.FLSeReady = Se
    return {"Server_Status": FLSe}



if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    print('asdf')
