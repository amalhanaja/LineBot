from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, LocationSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('lG9rEIP8vrQnDUZfWcbx7ny1r3rnwKYTNUeVt1Tt7rFMaUY64Qxl2+T3rnofyEZyOZPrtdEiUA6fgsV1b0zImcryHy1FWqqWIgePWQBuHbVgClcByE9orTAaEYPN418nYrh1UL32QhWaXVgVbfhwmAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c8389cd4cb889807cf529273a7872092')

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
    lokasiDict = ("lokasi", "cabang", "gerai", "kantor")
    cabangDict = ("sidoarjo", "surabaya", "bangkalan", "jombang", "yogyakarta")
    print (event.message.text)
    for pesan in event.message.text.lower().split():
        if pesan in lokasiDict:
            text_message = TextSendMessage(text="Mau cari tahu "+ pesan + " di Kabupaten/Kota mana BossKu ?")
            line_bot_api.reply_message(event.reply_token, text_message)
        if pesan in cabangDict:
            if(pesan == cabangDict[0]):
                send_location = LocationSendMessage(
                    title="Kantor Pusat",
                    address="Jl Diponegoro Ruko Graha Mutiara Delta C9, Sidoarjo, Jawa Timur",
                    latitude=-7.452799,
                    longitude=112.714243,
                )
                line_bot_api.reply_message(event.reply_token, send_location)
                ###TODO: ADD MORE ACTION
            else:
                text_message = TextSendMessage(text="Maaf Sekali Bossku kita belum buka cabang disana")
                line_bot_api.reply_message(event.reply_token, text_message.messages)
    #
    # line_bot_api.reply_message(
	# 	event.reply_token,
	# 	TextSendMessage(text='Hello!')
	# )
    # if event.message.text.lower == "hai":
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text='Hai Juga')
    # )
    # if event.message.text.lower == "lokasi":
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         LocationSendMessage(
    #             title="Kantor Pusat",
    #             address="Jl Diponegoro Ruko Graha Mutiara Delta C9, Sidoarjo, Jawa Timur",
    #             latitude=-7.452799,
    #             longitude=112.714243,
    #         )
    #     )
if __name__ == "__main__":
    app.run()
    #arg_parser = ArgumentParser(
    #    usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    #)
    #arg_parser.add_argument('-p', '--port', default=8000, help='port')
    #arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    #options = arg_parser.parse_args()
    #app.run(debug=options.debug, port=options.port)
# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )

# app = Flask(__name__)

# line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('YOUR_CHANNEL_SECRET')


# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


# if __name__ == "__main__":
#     app.run()
