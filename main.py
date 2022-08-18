import nextcord
from nextcord.ext import commands

import news_getting_cog
from settings import BOT_PREFIX, BOT_DESC, BOT_NAME, WATCH_MESSAGE, TOKEN

bot = commands.Bot(command_prefix=BOT_PREFIX, description=BOT_DESC)


# on ready do some set up
@bot.event
async def on_ready():
    print(f"{BOT_NAME} is now ready")
    print("---------------------------------------------------")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=WATCH_MESSAGE))


bot.add_cog(news_getting_cog.News(bot))

print("starting up")
bot.run(TOKEN)
