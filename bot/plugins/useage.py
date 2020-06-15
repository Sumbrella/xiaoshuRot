"""

"""
import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=('使用帮助', '用法', '帮助', '使用方法'))
async def usage(session:CommandSession):
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果没有参数 发送列表
        await session.send(
            '现在支持的功能有：\n' + '\n'.join(p.name for p in plugins) +
            '\n\n可以发送 “帮助 + 选项” 来查看使用示例哦~'
        )
        return

    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
