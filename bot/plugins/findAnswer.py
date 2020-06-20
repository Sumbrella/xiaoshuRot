
import requests
from nonebot import on_command, CommandSession
from time import sleep
from urllib.parse import quote
import json

url = 'http://cx.icodef.com/v2/answer'


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
        self.topic = None
        self.answer = None

    def post(self):
        self.response = requests.post(url=url, data=self.data, headers=self.headers)
        sleep(0.5)
        self.response = json.loads(self.response.content)
        result = self.response[0]['result']
        answer = result[0]['correct']
        topic = result[0]['topic']
        self.topic = topic
        self.answer = answer


@on_command("find", aliases=("查题"))
async def findAnswer(session: CommandSession):
    args = session.current_arg_text.split()
    poster = Poster(args[0])
    poster.post()
    await session.send(str(poster.topic) + "\n" + str(poster.answer))
