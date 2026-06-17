from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):

        self.connections = {}

    async def connect(
        self,
        run_id,
        websocket
    ):

        await websocket.accept()

        self.connections[
            run_id
        ] = websocket

    def disconnect(
        self,
        run_id
    ):

        if run_id in self.connections:

            del self.connections[
                run_id
            ]

    async def send_log(
        self,
        run_id,
        message
    ):

        ws = self.connections.get(
            run_id
        )

        if ws:

            await ws.send_json(
                {
                    "message":
                        message
                }
            )