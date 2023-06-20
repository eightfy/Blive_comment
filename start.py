import os
import random
import asyncio
import blivedm
import tkinter as tk
import threading
from message import MyHandler
import datetime

TEST_ROOM_IDS = [
    22603245, # 永雏塔菲
    #22637920, #monaka
    #23490978,
    #1438243, 
    ]


async def main():
    await run_client()

async def run_client():
    room_id = random.choice(TEST_ROOM_IDS)
    client = blivedm.BLiveClient(room_id, ssl=True)
    handler = MyHandler()
    client.add_handler(handler)
    client.start()
    await client.join()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.delete_file_button = tk.Button(
            self.master, text='删除data.txt并自动退出', command=self.delete_file)
        self.delete_file_button.pack(side="top")

    def delete_file(self):
        os.remove("data.txt")
        os._exit(0)

def win():
    app = Application()
    app.mainloop()
def dan():
    asyncio.run(main())

if __name__ == '__main__':
    with open("data.txt", "w") as f:
        pass
    with open("data.txt", "a+") as f:
        f.write(f'========== {datetime.datetime.now().strftime(" %Y-%m-%d ")}：：{datetime.datetime.now().strftime(" %H:%M:%S ")}==========\n')
    t1 = threading.Thread(target=win)
    t2 = threading.Thread(target=dan)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
