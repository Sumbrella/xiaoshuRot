"""

"""

from nonebot import get_bot
from nonebot import permission as perm
from nonebot import on_command
from nonebot import CommandSession


@on_command('点赞', permission=perm.SUPERUSER)
async def _(session: CommandSession):
    bot = get_bot()
    friend_list = await bot.get_friend_list()
    for friend in friend_list:
        await bot.send_like(user_id=friend['user_id'], times=10)
