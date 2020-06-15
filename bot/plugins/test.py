# """
#
# """
#
# from aiocqhttp.event import Event
# from nonebot import get_bot
#
# from ..qqids import *
#
#
# bot = get_bot()
#
#
# @bot.on_message('private')
# async def _(ctx: Event):
#     message = ctx['raw_message']
#     print(message)
#     await bot.send_group_msg(group_id=big_group, message=message)
