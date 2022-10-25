def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./aocuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(aoc):
	for i in a:
		await aoc.edit(' '+str(i))
		sleep({slep})
Help = CmdHelp("aocuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @SakirBey2 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def a_(fayl_adi, name, siyahi, slep):
	f = open(f"./aocuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(aoc):
	text= " "
	for i in a:
		text+=i+"\\n"
		await aoc.edit(text)
		sleep({slep})
Help = CmdHelp("aocuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @sakirbey2 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def r_(fayl_adi, name, siyahi):
	f = open(f"./aocuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from random import choice
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(aoc):
	random_ = choice(a)
	await aoc.client.send_file(aoc.chat_id, random_)
	await aoc.delete()
Help = CmdHelp("aocuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @SakirBey2 tarafından hazırlanmıştır.")
Help.add()
		""")

def m_(fayl_adi, name, siyahi):
	f = open(f"./aocuserbot{fayl_adi}.py", "x")
	f.write("""from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import random
import os
IFACI = [{siyahi}]
@register(outgoing=True, pattern="^.{name}$")
async def aocmusic(aoc):
    
    
    await aoc.edit("`Sizin için  "+IFACI+"müziğini aktarıyorum`")
    try:
        results = await aoc.client.inline_query('deezermusicbot', '+IFACI+')
    except:
            await aoc.edit("`Bottan cevap alamadım`")
            return
    netice = False
    while netice is False:
            rast = random.choice(results)
            if rast.description == IFACI:
                await aoc.edit("`Müzik Yükleniyor!")
                yukle = await rast.download_media()
                await aoc.edit("`Yükleme tamamlandı!`")
                await aoc.client.send_file(aoc.chat_id, yukle, caption="@SakirBey2 sizin için `"+rast.description+" - "+rast.title+"` müziğini seçti iyi dinlemeler. :)")
                await event.delete()
                os.remove(yukle)
                netice = True
Help = CmdHelp("aocuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @SakirBey2 Taradındən Hazırlanmışdır..")
Help.add()
		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))
