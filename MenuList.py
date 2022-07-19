from telebot import types
from Messages_v2 import *

def start_menu():
    callback1 = types.InlineKeyboardButton(
        text = "Search Module Info", callback_data = "module_info"
    )

    callback2 = types.InlineKeyboardButton(
        text = "Find Module Group", callback_data = "module_group"
    )

    callback3 = types.InlineKeyboardButton(
        text = "Find Module Mate", callback_data = "module_mate"
    )

    callback4 = types.InlineKeyboardButton(
        text = "Find Study Buddy", callback_data = "study_buddy"
    )

    menu = types.InlineKeyboardMarkup()
    menu.add(callback1)
    menu.add(callback2)
    menu.add(callback3)
    menu.add(callback4)

    return menu

def faculty_menu():

    menu = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    menu.add("Alice Lee Centre for Nursing Studies")
    menu.add("Business School")
    menu.add("College of Design and Engineering")
    menu.add("College of Humanities and Sciences - FASS")
    menu.add("College of Humanities and Sciences - FoS")
    menu.add("Faculty of Dentistry")
    menu.add("Faculty of Law")
    menu.add("NUS College")
    menu.add("School of Computing")
    menu.add("Yong Loo Lin School of Medicine")
    menu.add("Yong Siew Toh Conservatory of Music")

    return menu

def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(like_str)
    markup.add(dislike_str)
    return markup
