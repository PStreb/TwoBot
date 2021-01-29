import discord
from discord import Game
from discord.ext import commands
import json
import os
from asyncio import sleep

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
   



@client.event
async def on_ready():

 @client.event
 async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-running'):
        await message.channel.send('https://cdn.discordapp.com/attachments/804326215925497879/804633362672910347/111111111.gif')

    if message.author == client.user:
        return

    if message.content.startswith('-food'):
        await message.channel.send('https://stihi.ru/pics/2018/11/04/8335.jpg')

    if message.content.startswith('-win'): await message.channel.send('https://cdn.discordapp.com/attachments/797427662527791134/804060991956058112/Untitled_Project_33.mp4')

    if message.content.startswith('Всем привет'): await message.channel.send('Привет!')

    if message.content.startswith('Как дела?'): await message.channel.send('У меня хорошо а у тебя как?')

    if message.content.startswith('у меня норм'): await message.channel.send('ого!')

    if message.content.startswith('-help'): embed = discord.Embed(
        title = 'Команды Бота 2Bot',
        description = """**-хелп: это сообщение
        -running: неизвестная команда
        -food: выдаст фотку еды
        -win: Ура! Мы Победили
        -сырой_хелп - прототип команды -хелп
        -links - ссылки
        -горин - мем
        -двор - мем
        -бомж - тоже мем
        -сосед - мем
        -школа - мем
        F - неизвестно
        -моргенштерн - мем
        -забанили - мем
        -тиктокеры - Тикток Хаус мем
        -корея - свежие кадры из КНДР
        -валим - мем
        -казахстан - неизвестно
        -дед - мем
        -мерин - мем
        -магия - мем
        -анадырь - свежие кадры из Анадыря**""",
        colour = discord.Colour.from_rgb(0, 255, 246)
    )
    if message.content.startswith('-горин'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779216532930600/7ca1e75dfb02e9c6.mp4')

    if message.content.startswith('-двор'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779225138987084/aff024ed0f41518d.mp4')

    if message.content.startswith('-бомж'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779229035495464/26d31fb3a9aefb96.mp4')

    if message.content.startswith('-сосед'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779243199528990/dcf8194e19326a47.mp4')

    if message.content.startswith('-школа'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779246936653854/2685e7636cbd9b87.mp4')

    if message.content.startswith('F'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779247620456468/2020_.mp4')

    if message.content.startswith('-моргенштерн'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779249579720794/8b1f3055e06841dc.mp4')

    if message.content.startswith('-забанили'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779251042615378/dd3ce78c3f38eff4.mp4')

    if message.content.startswith('-тиктокеры'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779251404242986/178efc7853e7ac93.mp4')

    if message.content.startswith('-корея'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779261654335548/adidas_super_hit_2010.mp4')

    if message.content.startswith('-валим'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779262292525086/389e10b9e0d8d4d7.mp4')

    if message.content.startswith('-казахстан'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779263873646662/ee4a1d9f3aadee51.mp4')

    if message.content.startswith('-дед'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779265098645544/ec693392ef48f93a.mp4')

    if message.content.startswith('-мерин'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779266607808543/0fd536b130ed750a.mp4')

    if message.content.startswith('-магия'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779268151836682/991e81a6c5a83963.mp4')

    if message.content.startswith('-анадырь'): await message.channel.send('https://cdn.discordapp.com/attachments/789565423845769249/804779271166885898/6de520d399a3ea40.mp4')
  
    


    if message.content.startswith('-links'): embed = discord.Embed(
        title = 'Ссылки Бота 2Bot',
        description = """[**Пригласить Бота**](https://discord.com/oauth2/authorize?client_id=804394465568489523&scope=bot&permissions=8)
        [**Ютуб Канал**](https://www.youtube.com/channel/UCmETveqjHp-__xhtrq1mMfg)
        [**Дискорд Сервер**](https://discord.gg/fvRsntPmgP)""",
        colour = discord.Colour.from_rgb(0, 255, 246)
    )
    await message.channel.send(embed=embed)

    if message.content.startswith('-сырой_хелп'): await message.channel.send('Это временный хелп: команды бота: -hello, -пельмень, -победа, Всем привет, Как дела?, у меня норм, -хелп (скоро будет работать(общение это реальный команды а не просто так)) -сырой_хелп')




client.run('ODA0Mzk0NDY1NTY4NDg5NTIz.YBLsuQ.c43McVdnDWaDBwLA8IOU0B31jb8')