import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("로그인중")
    print("준비됨")
    game = discord.Game("명령어 준비됨")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=".help입력ㄱㄱ". format(len(client.guilds), len(client.users))))
    




@client.event
async def on_message(message):
    if message.content.startswith("서준아"):
        await message.channel.send("뭐")
        await message.channel.send("왓")
        await message.channel.send("?")
    if message.content.startswith(".심심해"):
        await message.channel.send("배그하던가 아무게임하던가.노래들으러가던가.공부하러가.밥먹으러가든가")
    if message.content.startswith("/몇살이니?"):
        await message.channel.send("관셈을보살")
    if message.content.startswith(".잘함?"):
        await message.channel.send("너보다는 잘할듯 ^^")
    if message.content.startswith(".help"):
        await message.channel.send("명령어들 입니다")
        await message.channel.send("#.서준아")
        await message.channel.send("#.심심해")
        await message.channel.send("#.몇살이니?")
        await message.channel.send("#.욕잘함?")
        await message.channel.send("#.ㅇ)
        await message.channel.send("#.ㅂ")
        await message.channel.send("#.어디살아")
        await message.channel.send("#.브금추천좀")                            
    if message.content.startswith(".ㅎㅇ"):
        await message.channel.send("안녕 나는 장애서준이노예야")
    if message.content.startswith(".어디살아"):
        await message.channel.send("니마음속에")
    if message.content.startswith(".ㅂㅂ"):
        await message.channel.send("잘가 다음에보장!!")
        await message.channel.send("그래 다음에보장!!!")
    if message.content.startswith(".브금추천좀"):
        await message.channel.send("요즘시대는https://www.youtube.com/watch?v=QNIokOJW8CM&t=2s")
    if message.content.startswith(".배그할래?"):
            await message.channel.send("나 일하러가봐야되;;우리형한테문의해!") 
          
          




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
