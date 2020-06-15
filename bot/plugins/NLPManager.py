"""

"""

from nonebot import on_natural_language
from nonebot import NLPSession


@on_natural_language(keywords='提问',)
async def questionHandler(session: NLPSession):
    return
