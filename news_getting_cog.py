import asyncio
import random
import datetime

import nextcord
from nextcord.ext import commands, tasks

import functions
import settings


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Chimp News Cog \n Manages the sending of chimp and other primate related news"

    @tasks.loop(hours=24)
    async def post_news(self):
        """every day send chimp news"""
        print('sending Chimp news')
        # news_channel = self.bot.get_channel(1002299603183489035)
        news_channel = self.bot.get_channel(settings.real_news_ID)


        news_story_list = functions.get_chimp_news('monkey')

        news_date = datetime.date.today()

        url = random.choice(settings.monkey_gifs)

        embedmsg = nextcord.Embed(title=f"Chimp News {news_date}",
                                  description='Here is the latest monkey business',
                                  color=0xccff00)
        embedmsg.set_image(url=url)
        for story in news_story_list:
            embedmsg.add_field(name=f"{story['publisher']} : {story['title']}", value=f"{story['url']}", inline=False)

        await news_channel.send(embed=embedmsg)
        print(f'{news_date} : message sent')

    @commands.Cog.listener()
    async def on_ready(self):
        print("news cog ready")
        self.post_news.start()


    @post_news.before_loop
    async def before_post_news(self):
        await self.bot.wait_until_ready()
        now = datetime.datetime.now()
        await asyncio.sleep(functions.time_until_next_reset(now, 7))
