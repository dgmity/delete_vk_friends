import asyncio
from vkbottle import API
from config import tokenac
api = API(token=tokenac)

async def handler():
    friends = await api.friends.get()

    for friend in friends.items:
        await api.friends.delete(friend)

asyncio.run(handler())