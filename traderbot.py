import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Trader is ready!")
    await client.change_presence(game=discord.Game(name="Lorax Kart"))
    
@client.event
async def on_message(message):
    userID = message.author.id
    
    # Nomes
    if message.content.upper() == "ALE":
        await client.send_message(message.channel, "esse é niilista")
    if message.content =="catito":
        await client.send_message(message.channel, "ah n")
    if message.content =="trader":
        await client.send_message(message.channel, "fala")
    if message.content =="davis":
        await client.send_message(message.channel, "meu criador")
    if message.content =="gru":
        await client.send_message(message.channel, "gru dudu e seu cu")
    if message.content =="vini":
        await client.send_message(message.channel, "outro niilista")
    if message.content =="skil9":
        await client.send_message(message.channel, "it is what it is")
    if message.content =="tetinhas":
        await client.send_message(message.channel, "esse é o amigo bundudo do ale ne")
    if message.content =="esquilo":
        await client.send_message(message.channel, "esse menino é aquela lenda urbana de guarulhos ne filhao?")
    if message.content =="andre":
        await client.send_message(message.channel, "esse que gosta de smosh dublado ne ale")
    if message.content =="luan":
        await client.send_message(message.channel, "adoro a série desse menino")
    if message.content =="flavio":
        await client.send_message(message.channel, "pernambucano do inferno") 
    if message.content =="guincho":
        await client.send_message(message.channel, "esse devia ta fznd LR mas fica o dia inteiro coçando o saco")
    if message.content =="ricardo":
        await client.send_message(message.channel, "faz uma webnamorada no python p mim pfvr")
    if message.content =="maranhão":
        await client.send_message(message.channel, "o cara zoa tf2 mas gosta de fantasia de cachorro")
    if message.content =="maranhao":
        await client.send_message(message.channel, "o cara zoa tf2 mas gosta de fantasia de cachorro")
    if message.content =="meg":
        await client.send_message(message.channel, "ó o Bongo ae")
    if message.content =="dri":
        await client.send_message(message.channel, "DRI DRI DRI DRI DRI DRI")
    if message.content =="toba":
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=kQU-3o1O5fM")

    # Ale é...
    if message.content.upper() =="ALE É MÓ...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale e mo...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale é mo...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh mó...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh moh...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh mo...":
        await client.send_message(message.channel, "...niilista")

    # Jogos e séries do Creme    
    if message.content =="qual o melhor jogo do mundo":
        await client.send_message(message.channel, "flappy catito")
    if message.content.upper() =="CADE LR?":
        await client.send_message(message.channel, "pergunta pra porra do guincho")
    if message.content =="sente sdds do catito?":
        await client.send_message(message.channel, "o do arqui ou o flappy?")
    if message.content =="flappy":
        await client.send_message(message.channel, "esse sim, jogo do ano")
    if message.content =="lorax kart":
        await client.send_message(message.channel, "duvido alguem bater o record do Rick: https://lorax-kart.netlify.app/")

    # Meme
    if message.content =="que":
        await client.send_message(message.channel, "jo")
    if message.content =="porra":
        await client.send_message(message.channel, "tudo isso")
    if message.content =="porr":
        await client.send_message(message.channel, "tudo isso")
    if message.content =="ronaldo":
        await client.send_message(message.channel, "brilha muito no curintia")
    if message.content =="mungus" || message.content=="sus" || message.content=="among us" || message.content=="monguinho":
        await client.send_message(message.channel, "vsf guincho")

    # Expressões
    if message.content.upper() =="MDS":
        await client.send_message(message.channel, "<@%s> chamou?" % (userID))
    if message.content.upper() =="VLW":
        await client.send_message(message.channel, "rlx qqlr coisa to aqui")
    if message.content.upper() =="Q":
        await client.send_message(message.channel, "q oq caralho")
    if message.content.upper() =="KK":
        await client.send_message(message.channel, "obrigado por rir")
    if message.content.upper() =="CUCK":
        await client.send_message(message.channel, "ó o ale ai")
    if message.content.upper() =="KCT":
        await client.send_message(message.channel, "no seu cu arrombado")
    if message.content.upper() =="AHN":
        await client.send_message(message.channel, "para c essa bosta de 'ahn'")
    if message.content.upper() =="GRR":
        await client.send_message(message.channel, "miau")
    if message.content.upper() =="PERAE":
        await client.send_message(message.channel, "to perando kk")
    if message.content.upper() =="EAE":
        await client.send_message(message.channel, "<@%s> eae bro" % (userID))
    if message.content.upper() =="UE":
        await client.send_message(message.channel, "ue oq?")
    if message.content.upper() =="KD":
        await client.send_message(message.channel, "n sei to procurando")
    if message.content.upper() =="PO":
        await client.send_message(message.channel, "rra")
    if message.content.upper() =="PQP":
        await client.send_message(message.channel, "Language.")
    if message.content.upper() =="RIP":
        await client.send_message(message.channel, "=f pipi") 
    if message.content.upper() =="VSF":
        await client.send_message(message.channel, "<@%s> vai vc" % (userID))
    if message.content.upper() =="MAS LITTLE." and message.author.id!="431999631120138240":
        await client.send_message(message.channel, "mas <@%s>." % (userID))

    # Piadas internas
    if message.content =="equador":
        await client.send_message(message.channel, "nem foi tao bom assim")
    if message.content =="o creme e de la quem?":
        await client.send_message(message.channel, "du ale")
    if message.content =="miguelvin ou melguel?":
        await client.send_message(message.channel, "<@%s> precisa de alguém rápido ou forte?" % (userID))
    if message.content =="forte":
        await client.send_message(message.channel, "melguel")
    if message.content =="rápido":
        await client.send_message(message.channel, "miguelvin")
    if message.content =="rapido":
        await client.send_message(message.channel, "miguelvin")
    if message.content =="boa sorte":
        await client.send_message(message.channel, "Mickey?")
    if message.content =="bolinho tetinhas":
        await client.send_message(message.channel, "esse foi feito na unha")

    # Jogos
    if message.content =="dominions 4":
        await client.send_message(message.channel, "meu filho n para de falar dessa bosta")
    if message.content =="fortnite":
        await client.send_message(message.channel, "ainda bem que o ale n joga isso")
    if message.content.upper() =="SCP":
        await client.send_message(message.channel, "jogao")

    # Literalmente Bullying (Catito)
    if message.content.upper()=="BAN":
        if message.author.id =="143607024087859200":
          await client.send_message(message.channel, "calaboca catito quem ter q ser banido é vc")
        else:
          await client.send_message(message.channel, "ban catito")
    if message.author.id =="143607024087859200":
        number=random.randint(0,19)
        lista=[1,2,3]
        lista2=[4,5,6]
        if number in lista:
           await client.send_message(message.channel, "kkkk o cara joga fortnite no switch")
        if number in lista2:
           await client.send_message(message.channel, "ah veio parae to cansado")
        if number==7:
            await client.send_message(message.channel, "olha n queria fala nada mas dessa vez o catito ta certo")

    # Tetinhas
        if message.author.id =="307282841501171712":
        number=random.randint(0,9)
        lista=[2,3]
        if number in lista :
           await client.send_message(message.channel, "mas little.")
        
    # Maranhão
        if message.author.id =="201575755124047879":
        number=random.randint(0,9)
        lista=[2,3,4,5]
        if number in lista :
           await client.send_message(message.channel, "kkkk o cara é furry")

    # Flavio
        if message.author.id =="216660094048403457":
        number=random.randint(0,20)
        lista=[1,2]
        if number==8:
        # Que porra de piada era essa? :
        #    await client.send_message(message.channel, "se continuar falando merda vou baixar o mod da sua namorada pelada")
        await client.send_message(message.channel, "ó o treloso ai faz umas graça")
        if number in lista:
           await client.send_message(message.channel, "chapéu de alumínio") 

    # Luan
        if message.author.id =="294968198535577600":
        number=random.randint(0,9)
        lista=[1,2]
        if number in lista:
           await client.send_message(message.channel, 
           "Caneta azul, azul caneta
            Caneta azul tá marcada com minha letra
            Caneta azul, azul caneta
            Caneta azul tá marcada com minha letra")

    # Esquilo
        if message.author.id =="132989284067180544":
        number=random.randint(0,11)
        lista=[5,6]
        if number in lista:
           await client.send_message(message.channel, "kkkk o cara mora em gru")

    # Ale
        if message.author.id =="325407029382348801":
        number=random.randint(0,99)
        if number ==24:
           await client.send_message(message.channel, "Cascudo.")
        elif number < 10 :
           await client.send_message(message.channel, "nada importa msm")
        elif number > 90 :
           await client.send_message(message.channel, "mó...")

    # Pergunte ao Trader
    if message.content =="sdds da morena?":
        await client.send_message(message.channel, "demais")
    if message.content =="cade seu filho?":
        await client.send_message(message.channel, "ta batendo punheta la em cima")
    if message.content =="e o arqui?":
        await client.send_message(message.channel, "sdds")
    if message.content.upper().startswith('QUAL O FRENE?'):
        memes = message.content.split(" ")
        if 'Catito' in memes or 'catito' in memes or 'CATITO' in memes:
            await client.send_message(message.channel, "Catito")
        else:
            size=len(memes)
            frene1=random.randint(3,size)
            await client.send_message(message.channel, "%s" % ("".join(memes[frene1])))
    if message.content.upper().startswith('QUAL O CORNO?'):
        memes = message.content.split(" ")
        if 'Ale' in memes or 'ale' in memes or 'Nagy' in memes or 'nagy' in memes or ':Nagy:' in memes:
            await client.send_message(message.channel, "óbvio que é o ale né")
        else:
            size=len(memes)
            frene1=random.randint(3,size)
            await client.send_message(message.channel, "%s" % ("bom já que o ale n tá aí acho que é o " +(memes[frene1])))

    # Discord bots e comandos
    if message.content =="@everyone":
        await client.send_message(message.channel, "chega mais rapaziada")
    if message.content =="/play":
        await client.send_message(message.channel, "solta o som <@%s>" % (userID))
    if message.content =="/play toto africa":
        await client.send_message(message.channel, "nossa toto africa mto bom")
    if message.content =="/play susto grito":
        await client.send_message(message.channel, "D:")
    if message.content =="/skip":
        number=random.randint(0,9)
        lista=[1,2,3]
        if number in lista:
           await client.send_message(message.channel, "nao porra mo foda a musica")
        if message.content.upper().startswith('!TRADER SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[2:])))
    if message.content.startswith('/play') :
        args= message.content.split(" ")
        number=random.randint(0,15)
        lista1=[1,2,3]
        lista2=[12,13]
        if number in lista1:
            await client.send_message(message.channel, "%s" % ('ae porra adoro ' + ' '.join(args[2:])))
        if number in lista2:
            await client.send_message(message.channel, "%s" % ('porra que merda ' + ' '.join(args[2:])))

    # Em caso de erros
    if message.content.upper() =="TRADER BUGO":
        await client.send_message(message.channel, "chama o creme de la dev")
    if message.content.upper() =="TRADER MORREU":
        await client.send_message(message.channel, "chama o creme de la dev")
   
    # Sessão Raffa Moreira (por algum motivo tem muita coisa disso)
    if message.content.upper() =="EU SOQUEI UM HATER NO SHOPPING":
        await client.send_message(message.channel, "QUE FALOU BOSTA") 
    if message.content.upper() =="ÓCULOS DO KURT COBAIN":
        await client.send_message(message.channel, "Double cup, Sprite, Codein")
    if message.content.upper() =="RAFFA MOREIRA":
        number=random.randint(0,9)
        lista=[0,1,2]
        lista2=[3,4,5]
        lista3=[6,7]
        lista4=[8,9]
        if number in lista:
            await client.send_message(message.channel, "MIXTAPE MANO")
        if number in lista2:
            await client.send_message(message.channel, "BRO FAZ SOL")
        if number in lista3:
            await client.send_message(message.channel, "gang gang")
        if number in lista4:
            await client.send_message(message.channel, "vc e branco bro")

client.run("NDMxOTk5NjMxMTIwMTM4MjQw.DasiAw.0hlUP5MbyeuWE_WuF6dVY0xjHa4")
client.login(process.env.BOT_TOKEN)
