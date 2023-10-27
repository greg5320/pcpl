import telebot
from telebot import types
import random
API_TOKEN = '6667880476:AAFfK2B4a03kYVY2b4zk4L0UmMKAyd68Q1U'
bot = telebot.TeleBot(API_TOKEN)

heroes = [
    "Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe",
    "Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster",
    "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen",
    "Clinkz", "Clockwerk", "Crystal Maiden", "Dark Seer", "Dazzle", "Death Prophet",
    "Disruptor", "Doom", "Dragon Knight", "Dawnbreaker", "Drow Ranger", "Earth Spirit", "Earthshaker",
    "Elder Titan", "Ember Spirit", "Enchantress", "Enigma", "Faceless Void", "Grimstroke",
    "Gyrocopter", "Huskar", "Hoodwink", "Invoker", "Io", "Jakiro", "Juggernaut", "Keeper of the Light",
    "Kunkka", "Legion Commander", "Leshrac", "Lich", "Lifestealer", "Lina", "Lion",
    "Lone Druid", "Luna", "Lycan", "Magnus", "Marci", "Mars", "Medusa", "Meepo", "Mirana",
    "Monkey King", "Morphling", "Muerta", "Naga Siren", "Nature's Prophet", "Necrophos",
    "Night Stalker", "Nyx Assassin", "Ogre Magi", "Omniknight", "Oracle", "Outworld Devourer",
    "Pangolier", "Primal Beast", "Phantom Assassin", "Phantom Lancer", "Phoenix", "Puck", "Pudge",
    "Pugna", "Queen of Pain", "Razor", "Riki", "Rubick", "Sand King", "Shadow Demon",
    "Shadow Fiend", "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark",
    "Snapfire", "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit", "Sven", "Techies",
    "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker", "Tiny",
    "Treant Protector", "Troll Warlord", "Tusk", "Underlord", "Undying", "Ursa",
    "Vengeful Spirit", "Venomancer", "Viper", "Visage", "Void Spirit", "Warlock", "Weaver",
    "Windranger", "Winter Wyvern", "Witch Doctor", "Wraith King", "Zeus"
]

@bot.message_handler(commands=['start'])
def send_random_word(message):
    random_hero = random.choice(heroes)
    markup = get_inline_keyboard()
    bot.send_message(message.chat.id, f"Случайный герой: {random_hero}", reply_markup=markup)


def get_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Новый герой", callback_data="new_hero")
    markup.add(button)
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "new_hero")
def button_click(call):
    random_hero = random.choice(heroes)
    markup = get_inline_keyboard()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Случайный герой: {random_hero}", reply_markup=markup)

if __name__ == '__main__':
    bot.polling()