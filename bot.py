import telebot
import requests
import os

TOKEN = os.environ.get("8787106530:AAGsSIQb2ta3pYPbX-aeWYuyREgaz4mId_8")
OPENROUTER_KEY = os.environ.get("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")

bot = telebot.TeleBot(8787106530:AAGsSIQb2ta3pYPbX-aeWYuyREgaz4mId_8)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ИИ-бот. Напиши мне что-нибудь 🤖")

@bot.message_handler(func=lambda m: True)
def ai_reply(message):
    bot.send_message(message.chat.id, "Думаю... ⏳")
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3.1-8b-instruct:free",
            "messages": [{"role": "user", "content": message.text}]
        }
    )
    
    reply = response.json()["choices"][0]["message"]["content"]
    bot.send_message(message.chat.id, reply)

bot.polling()