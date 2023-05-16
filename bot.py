"""
import csv
from pathlib import Path
from llama_index.indices.vector_store import GPTSimpleVectorIndex
from llama_index import download_loader,LLMPredictor
from langchain.chat_models import ChatOpenAI
import os


os.environ["OPENAI_API_KEY"] = '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'

loaded_index = GPTSimpleVectorIndex.load_from_disk('index.json')

query = '一次方程式の解き方は？'
response = index.query(query)
print(response)"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得
"""YOUR_CHANNEL_ACCESS_TOKEN = os.environ["xOI/6oM31uxRQ2hX96Lu+ChY3qbYKLoJo6Ht0jytaCXxI7PHsOB96//B2FmX9XL+mAB47znM2rC0QTGmvWOjY7tylB8Or7te5Nd81LuI5/HiKeWjon6oarIP8FBZ7FCf/VAt9L4fRw2ZCHbXBptatgdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["a1925b289744404dfbe0603365bebdeb"]"""

line_bot_api = LineBotApi("xOI/6oM31uxRQ2hX96Lu+ChY3qbYKLoJo6Ht0jytaCXxI7PHsOB96//B2FmX9XL+mAB47znM2rC0QTGmvWOjY7tylB8Or7te5Nd81LuI5/HiKeWjon6oarIP8FBZ7FCf/VAt9L4fRw2ZCHbXBptatgdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("a1925b289744404dfbe0603365bebdeb")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)