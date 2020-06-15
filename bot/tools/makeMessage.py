"""

"""
import time

from aiocqhttp.event import Event


def makeMessageTitle(ctx: Event):
    items = ctx.items()

    _time = time.localtime(ctx.get('time'))
    _time = time.strftime("%Y-%m-%d %H:%M:%S", _time)

    # 获取发送者信息
    sender = ctx.get('sender')
    user_id = sender['user_id']
    nickname = sender['nickname']
    # 获取信息
    result_message = f"{_time}\nQQ名称:{nickname}\nQQ号:{user_id}\n"

    return result_message

