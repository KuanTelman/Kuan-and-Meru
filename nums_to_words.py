from num2words import num2words
from tkinter import *
import tkinter.messagebox
import pyperclip

print("It can take any number",
      "lang: The language in which to convert the number. Supported values are:",
      "en (English, default)",
      "kz (Kazakh)",
      "fr (French)",
      "ru (Russian)",
      "see full info at https://github.com/savoirfairelinux/num2words",
      sep = '\n')

print('Input your number')
num = input()
print('Input language needed')
print('Your result will be saved to clipboard so use Ctrl+V ti insert text to your doc')
lang = str(input())

pyperclip.copy(num2words(num, lang = lang))
