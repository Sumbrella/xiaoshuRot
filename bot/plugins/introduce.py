"""

"""

from nonebot import on_command
from nonebot import CommandSession

__plugin_name__ = '介绍'
__plugin_usage__ = """
使用示例
介绍\
"""

INTRODUCEMESSAGE = """\
{nickname},你好,我是长安大学数学竞赛小数助手！\
我主要能帮助小数完成各项工作，\
现在的工作主要是帮助小数完成答疑工作\
因为小数不是一直都有小姐姐登陆的哦(划去),\
你可以将问题发给我，我会联系小数来解答哦！
    eg:
        提问 小数(助手)我想知道鸟笼多少斤呀？\
"""


@on_command('introduce', aliases=('介绍', '自我介绍', '你是谁'))
async def introduce(session: CommandSession):
    sender = session.ctx.get('sender')
    nickname = sender['nickname']
    await session.send(INTRODUCEMESSAGE.format(
       nickname=nickname
    ))
