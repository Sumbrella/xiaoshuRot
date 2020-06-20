
import reuqests
from nonebot import on_command, commandSession
from urllib.parse import quote
import json


class Poster:
    def __init__(self, question):
        data = "topic[0]=" + quote(question)
        self.data = data.replace("%28%29", "()")
        self.length = len(data)
        self.headers = {
            "Host": "cx.icodef.com",
            "Connection": "keep-alive",
            "Content-Length": "{}".format(self.length),
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://cx.icodef.com",
            "Referer": "http://cx.icodef.com/query.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        self.response = None
        self.answer = {}

    def post(self):
        self.response = requests.post(url=url, data=self.data, headers=self.headers)
        sleep(0.5)
        self.response = json.loads(self.response.content)
        result = self.response[0]['result']
        option = result[0]['correct'][0]['option']
        content = result[0]['correct'][0]['content']
        self.answer = {
            'option': f'{option}',
            'content': f'{content}',
        }


@on_command("find",aliases=("查题"))
async def findAnswer(session: commandSession):
	args = session.current_args.split()
	poster = Poster(args)
	poster.post()
	await session.send(poster.answer)
