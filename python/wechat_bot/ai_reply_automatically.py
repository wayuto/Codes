import json
from wxauto import WeChat
import requests


conversationHistory: str = ""
def getReplyingContent(newMsg: str, who: str) -> None:
    global conversationHistory
    prompt: str = f"""你叫万宇桐，你正在与{who}对话，
    这是你们的历史对话(WAN代表你, 非{who}的对话不必理会): [ \n \"{conversationHistory}\" \n], 
    直接回复{who}发来的新内容: \"{newMsg}\"不要带有WAN字样
    """

    headers: dict = {
        "Authorization": "Bearer sk-W0rpStc95T7JVYVwDYc29IyirjtpPPby6SozFMQr17m8KWeo",
        "Content-Type": "application/json"
    }

    data: dict = {
        "model": "free:QwQ-32B",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    }

    result: requests.Response = requests.post(url="https://api.suanli.cn/v1/chat/completions", headers=headers, data=json.dumps(data))
    if result.status_code == 200:
        replyingContent: str = result.json()["choices"][0]["message"]["content"]
        processedContent: str = replyingContent.split("</think>")[1].strip()
        conversationHistory += f"{who}: \"{newMsg}\" \n WAN: \"{processedContent}\""
        return processedContent
    else:
        return result

def main() -> None:
    wx = WeChat()

    listeningList: list = ["Object", "海风"]
    for listeningObject in listeningList:
        wx.AddListenChat(listeningObject)

    while True:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            who: str = chat.who
            one_msgs: list = msgs.get(chat)
            for msg in one_msgs:
                msgType: str = msg.type
                content: str = msg.content
                if msgType == 'friend':
                    print(f"{who}: {content}")
                    replyingContent: str = getReplyingContent(content, who)
                    wx.SendMsg(replyingContent, who)
                    print(f"4e07: {replyingContent}")

if __name__ == '__main__':
    main()