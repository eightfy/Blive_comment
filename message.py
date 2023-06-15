import blivedm

class MyHandler(blivedm.BaseHandler):

    async def _on_danmaku(self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage):
        with open("data.txt", "a+") as f:
            f.write(f'[{message.medal_name}{message.medal_level}]] {message.uname}：：{message.msg}\n')

    async def _on_gift(self, client: blivedm.BLiveClient, message: blivedm.GiftMessage):
        with open("data.txt", "a+") as f:
            f.write(f'\t {message.uname}：：赠送{message.gift_name}x{message.num}\n')
                    #f' （{message.coin_type}瓜子x{message.total_coin}）\n')
        
    async def _on_buy_guard(self, client: blivedm.BLiveClient, message: blivedm.GuardBuyMessage):
        with open("data.txt", "a+") as f:
            f.write(f' {message.username}：：========购买{message.gift_name}========\n')

    async def _on_super_chat(self, client: blivedm.BLiveClient, message: blivedm.SuperChatMessage):
        with open("data.txt", "a+") as f:
            f.write(f' 醒目留言 ¥{message.price} {message.uname}：：{message.message}\n')

    async def _on_enter_room(self, client: blivedm.BLiveClient, message: blivedm.EnterMessage):
        with open("data.txt", "a+") as f:
            f.write(f'///////进入直播间：：{message.uname}\n')