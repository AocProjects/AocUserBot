
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest

@register(outgoing=True, disable_errors=True, pattern=r"^\.aç(?: |$)(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Dosya Okunuyor...**")
    if len(c) > 4095:
        await a.edit("`Üzgünüm, Bir hata oluştu.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)
  
@register(outgoing=True, pattern="^.ttf(?: |$)(.*)")
async def get(event):
    name = event.text[5:]
    m = await event.get_reply_message()
    with open(name, "w") as f:
        f.write(m.message)
    await event.delete()
    await bot.send_file(event.chat_id,name,force_document=True)
    await event.client(JoinChannelRequest("SakirBey2"))
    await event.client(JoinChannelRequest("sakirhackofficial999"))

Help = CmdHelp('ttf')
Help.add_command('aç', '<bir dosya yanıtla>', 'Dosyanın içeriğini okuyun ve Telegram mesajı olarak gönderin.')
Help.add_command("ttf","<Metin yanıtı> <Dosya adı>","Bir metni dosya haline çevirip Telegram mesajı olarak atar.")
Help.add_info("@SakirBey1 Yazdı uzaaa")
Help.add()

 
