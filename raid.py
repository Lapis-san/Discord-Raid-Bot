import discord
 
class Bot(discord.Client):
 
    def __init__(self):
        super().__init__()
 
 
    async def on_ready(self):
            print("Logged in as")
            print(self.user.name)
            print(self.user.id)
            print("------")
            print("created by bex#9999 | github.com/Enterrados ")
            members = 0
            for guild in self.guilds:
                members += guild.member_count
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f'{len(self.guilds)} servers and {members} members.'))
 
    async def on_message(self, message):
 
        if (message.author == self.user):
            return
 
        if (message.content.startswith(".on")):
            run = True
            while run is True:
                await message.channel.send('YOUR RAID MESSAGE')
                await message.guild.create_text_channel('YOUR RAID CHANNEL NAME')
 
 
if __name__ == "__main__":
    bot = Bot()
    bot.run("YOUR BOT TOKEN")
