from fastapi import FastAPI, WebSocket, WebSocketDisconnect

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[WebSocket] = {}
        self.room_connection: dict[str] = {}
        
    def join_room(self, room_name: str, websocket: WebSocket):
        try:
            room_obj = self.room_connection[room_name]
            room_obj.append(websocket)
            return
        except Exception as e:
            self.room_connection[room_name] = [websocket]
    
    def create_room(self, room_name, websockt: WebSocket):
        if room_name in self.room_connection:
            return False
        else:
            self.room_connection[room_name] = [websockt]
            return True

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        del self.active_connections[WebSocket]
        for room in self.room_connection:
            room.

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)        
            
            
manager = ConnectionManager()
