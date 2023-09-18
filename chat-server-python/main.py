from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

class loginReq(BaseModel):
    name: str
    passwd: str

app = FastAPI()


@app.get("/")
def hearbeat():
    return True


@app.post("/login")
def read_item(item: loginReq):
    confirm = True
    if not item.name == "xheize":
        confirm = False
    if not item.passwd == "test1234":
        confirm = False
    if not confirm:
        return { "code": 2, "msg": "login fail"}
    return { "code": 1, "msg": "login success"}

@app.websocket("/chat")
async def websocket_endpoing(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")