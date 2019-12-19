# This python script translates phrases passed to /t command

__module_name__ = "translate"
__module_version__ = "1.0"
__module_description__ = "This python script translates phrases passed to /t command"

# CONFIGURATION

DEST_LANG = "it"

# CONFIGURATION END

import hexchat
import googletrans

print(f"Loaded {__module_name__} version {__module_version__}")
print(f"{__module_description__}")

def translate(phrase, dest_lang=DEST_LANG):
    translator = googletrans.Translator()
    return translator.translate(phrase, dest=dest_lang).text

def t_command_hook(word, word_eol, userdata):
    phrase = " ".join(word[1:])
    print("Translation: {}".format(translate(phrase)))
    return hexchat.EAT_ALL

def tt_command_hook(word, word_eol, userdata):
    dest_lang = word[1]
    phrase = " ".join(word[2:])
    print("Translation: {}".format(translate(phrase, dest_lang=dest_lang)))
    return hexchat.EAT_ALL

hexchat.hook_command("t", t_command_hook, help=f"/t <phrase> translates frase to {DEST_LANG} using Google Translate APIs")
hexchat.hook_command("tt", tt_command_hook, help="/tt <dest_lang> <phrase> translates to <dest_lang> using Google Translate APIs")
