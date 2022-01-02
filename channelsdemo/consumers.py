import json
import random
from asyncio import sleep

from channels.generic.websocket import AsyncWebsocketConsumer


class NumberGenerator(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        while True:
            data = {
                'number': random.randint(1, 1000)
            }

            await self.send(json.dumps(data))

            await sleep(1)

    def disconnect(self, code):
        print("Socket disconnected with code", code)
