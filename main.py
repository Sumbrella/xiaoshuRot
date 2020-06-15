"""
"""
import os

import nonebot

from xiaoshuRot import config


def main():
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'bot', 'plugins'),
        'bot.plugins'
    )
    nonebot.run()


if __name__ == '__main__':
    main()

