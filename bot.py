import csv
import logging
import os
import sqlite3

import config
import discord
import keep_alive
import requests
from discord import utils
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

result = []
k = 0
con = sqlite3.connect('C:/Users/natas/Downloads/sqlitestudio-3.3.3 (1)/SQLiteStudio/all_programmers')
cur = con.cursor()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
intents = discord.Intents.default()
intents.members = True

Base = declarative_base()


def translate_text(target, text):
    import six
    # from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


# этот api не получилось хорошо подключить, по итогу не использовался

class User(Base):
    __tablename__ = 'person'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String)
    role = Column('role', String)


engine = create_engine(f'sqlite:///users.db', encoding="utf8", echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
session = Session()


# создание orm моделей

class YLBotClient(discord.Client):
    global k
    roles = []

    async def on_ready(self):  # отправляет в консоль сообщение, что подключился
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def member_join(self, member):  # отправляет приветствие в личку при подключении нового пользователя в личку
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):  # реакция на сообщение
        print(message.content.lower()[0])

        if message.author == self.user:
            return
        if "c++" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'c++' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")

            await message.channel.send('http://1obuchenie.com/wp-content/uploads/2020/05/maxresdefault.jpg')
        elif "python" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'python' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://russiakids.ru/storage/ug/ugOwbJ2N.l.jpg')
        elif "java" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'java' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://fuzeservers.ru/wp-content/uploads/6/8/c/68c002704dca9c8f6316be783e593de6.jpeg')
        elif "pascal" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'pascal' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://cloud.prezentacii.org/18/09/66230/images/screen8.jpg')
        elif "scratch" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'scratch' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://androidt.ru/uploads/posts/2021-06/1623614554_kisspng-scratchjr-'
                'computer-programming-thymio-discovery-pr-scratch-5b10f832b4f0f4.42990'
                '55915278387707412.jpg')
        elif "d" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'd' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://upload.wikimedia.org/wikipedia/commons/'
                'thumb/2/24/D_Programming_Language_logo.svg/1200px-'
                'D_Programming_Language_logo.svg.png')
        elif "r" in message.content.lower():
            print(message.author)
            for elem in result:
                if elem['role'] == 'r' and elem['name'] != str(message.author).split("#")[0]:
                    await message.author.send(f"{elem['name']} can help you")
            await message.channel.send(
                'https://avatars.mds.yandex.net/'
                'i?id=5c674c8f240e1f710feff1a652c86974-'
                '5516191-images-thumbs&n=13')
        # при введении названия языка выводит эмблему и кто может помочь в случае проблем с задачей
        elif "кот" in message.content.lower() or "кошк" in message.content.lower():
            server = 'https://api.thecatapi.com/v1/images/search'
            response = requests.get(server)
            await message.channel.send(response.json()[0]['url'])
        # выводит фото кошек
        elif "собак" in message.content.lower() or "щенок" in message.content.lower():
            server1 = "https://dog.ceo/api/breeds/image/random"
            response1 = requests.get(server1)
            await message.channel.send(response1.json()['message'])
        # выводит фото собак
        elif "привет" in message.content.lower() or "здравствуйте" in message.content.lower():

            await message.channel.send('Добро пожаловать!')
        elif message.content.lower()[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            print(translate_text('ru', message))
        # приветствие

    async def on_raw_reaction_add(self, payload):  # взаимодействие с постановкой реакции

        if payload.message_id == config.post_id:

            channel = self.get_channel(payload.channel_id)  # получаем объект канала
            message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
            member = utils.get(message.guild.members,
                               id=payload.user_id)  # получаем объект пользователя который поставил реакцию

            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.roles[emoji])  # объект выбранной роли (если есть)

            if (len([i for i in member.roles]) <= config.max_roles_for_user):
                global k
                k += 1
                print(config.roles[emoji])
                print(config.language[config.roles[emoji]])
                print(type(str(member).split('#')[0]))
                c = User(
                    id=k,
                    username=str(member).split('#')[0],
                    role=config.language[config.roles[emoji]]

                )
                session.add(c)
                session.commit()
                session.close()
                result.append({"name": str(member).split('#')[0], "role": config.language[config.roles[emoji]]})
                await member.add_roles(role)
                with open('users.csv', 'w', newline='', encoding="utf8") as f:
                    writer = csv.DictWriter(f, fieldnames=list(result[0].keys()), delimiter='-')
                    writer.writeheader()
                    for line in result:
                        writer.writerow(line)

    async def on_raw_reaction_remove(self, payload):  # взаимодействие с удалением реакции
        global k
        channel = self.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members,
                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        k -= 1
        emoji = str(payload.emoji)  # эмоджик который выбрал юзер
        role = utils.get(message.guild.roles, id=config.roles[emoji])
        print(str(member).split('#')[0])  # объект выбранной роли (если есть)
        i = session.query(User).filter(User.username == str(member).split('#')[0]).one()

        session.delete(i)
        session.commit()
        session.close()
        await member.remove_roles(role)
        for elem in result:
            print(str(member).split('#')[0])
            if elem['name'] == str(member).split('#')[0]:
                result.remove(elem)
                print('ok')
        if not result:
            result.append({"name": '', "role": ''})

        with open('users.csv', 'w', newline='', encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=list(result[0].keys()), delimiter='-')
            writer.writeheader()
            for line in result:
                writer.writerow(line)
            if not result:
                writer.writerow('')
        print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
keep_alive.keep_alive()
client.run(os.enviran.get('TOKEN'), bot=True, reconnect=True)
