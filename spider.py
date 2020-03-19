#!/usr/bin/python3

import vk_api
import os

G = {}

MAX_GRAPH_SIZE = 1000

def go(user_id):
    if user_id in G and len(G[user_id]) > 0:
        return

    print("current user_id:", user_id, "G size:", len(G))

    G[user_id] = []
    try:
        for friend in vk.friends.get(user_id=int(user_id))['items']:
            G[user_id].append(friend)
            if not friend in G:
                G[friend] = []

        if len(G) < MAX_GRAPH_SIZE:
            for friend in G[user_id]:
                go(friend)
    except Exception:
        print("Exception:", Exception)

vk_session = vk_api.VkApi(os.environ["VK_KEY"], os.environ["VK_VALUE"])
vk_session.auth()

vk = vk_session.get_api()

user_id = vk.users.get()[0]['id']
print("user_id:", user_id)

go(user_id)

print("ready graph size:", len(G))
