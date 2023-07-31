import os
import vk_api
from dotenv import load_dotenv

load_dotenv()


session = vk_api.VkApi(token=os.getenv("TOKEN"))
vk = session.get_api()


def get_user_status(user_id):
    friends = session.method("friends.get", {"user_id": user_id})

    for friend in friends["items"]:
        user = session.method("users.get", {"user_ids": friend})
        status = session.method("status.get", {"user_id": friend})

        if status["text"] == "":
            continue
        else:
            print(f"{user[0]['first_name']} {user[0]['last_name']} | {status['text']}")


def set_user_status():
    vk.status.set(text="New text for my status")


get_user_status(1)
set_user_status()
