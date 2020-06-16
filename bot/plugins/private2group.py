"""

"""
import time

from nonebot import get_bot
from nonebot import on_command
from nonebot import on_natural_language
from nonebot import CommandSession
from nonebot import NLPSession
from nonebot import IntentCommand

from ..data.qqids import *
from ..tools.makeMessage import makeMessageTitle

__plugin_name__ = '提问'
__plugin_usage__ = """\
用法示例：
提问 鸟笼多少斤？\
"""

bot = get_bot()


@on_command('question', aliases={'问题', '提问'}, shell_like=True)
async def private2group(session: CommandSession):

    question = session.get('question', prompt='请发送你的问题~')
    print(question)
    question = question[0]
    print(question)
    title = makeMessageTitle(ctx=session.ctx)
    # print(title)

    await bot.send_msg(group_id=test_group, message=title+question)
    await session.send('问题已经收到啦，请等待')


@private2group.args_parser
async def _(session: CommandSession):
    # 去掉首尾的空白
    stripped_arg = session.current_arg.split()

    if session.is_first_run:
        if stripped_arg:
            session.state['question'] = stripped_arg
        return

    if not stripped_arg:
        session.pause("未收到问题，请重新输入 （提问 xxxx）")
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords='提问')
async def handler(session: NLPSession):
    return IntentCommand(80, 'question')
