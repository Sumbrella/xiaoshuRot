"""
"""
NOINPUT = 0

from nonebot import on_command, CommandSession
from nonebot import  premission as perm

@on_command('send_group_message' ,permission=perm.SUPERUSER, aliases=('发送群消息'))
async def _send_group_message(session: CommandSession):
	if session.state['group_id'] == NOINPUT:
		await session.send('指令错误!')
		return
	else:
		group_id = int(session.state['group_id'])
		message = session.state['target_message']

		await session.bot.send(group_id=group_id, message=message)
		await session.send('消息已发送')

@_send_group_message.args_parser
async def _(session: CommandSession):
	arg = session.current_arg_text
	args = arg.split('/')
	try:
		group_id = args[0]
		message = args[1]
	except Exception as e:
		session.state['group_id'] = NOINPUT
		session.state['target_message'] = ""


