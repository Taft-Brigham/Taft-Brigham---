from bot import telegram_bot
import openai

mybot = telegram_bot("config.txt")

update_id = None

def make_reply(msg):
    if msg is not None:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=msg,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    
while True:
    print("...")
    updates = mybot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            mybot.send_message(reply, from_)