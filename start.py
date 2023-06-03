import random
import asyncio
import blivedm

class MyHandler(blivedm.BaseHandler):

    async def _on_danmaku(self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage):
        with open("data.txt", "a+") as f:
            f.write(f'[{client.room_id}] {message.uname}：{message.msg}\n')

    async def _on_super_chat(self, client: blivedm.BLiveClient, message: blivedm.SuperChatMessage):
        with open("data.txt", "a+") as f:
            f.write(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}\n')

TEST_ROOM_IDS = [27529444, ]

async def main():
    await run_client()

async def run_client():
    room_id = random.choice(TEST_ROOM_IDS)
    client = blivedm.BLiveClient(room_id, ssl=True)
    handler = MyHandler()
    client.add_handler(handler)
    client.start()
    await client.join()

if __name__ == '__main__':
    asyncio.run(main())
