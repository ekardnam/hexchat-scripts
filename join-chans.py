# This python scripts joins automatically all the channels.
# Can be used if some channels are required to be joined after NickServ auth has happened

__module_name__ = "join-chans"
__module_version__ = "1.0"
__module_description__ = "This python scripts joins automatically all the channels. Can be used if some channels are required to be joined after NickServ auth has happened"

# CONFIGURATION

# Channels to be joined
CHANS = ["#archlinux-projects", "#archlinux-aur", "#archlinux-security"]

# CONFIGURATION END

import hexchat

print(f"Loaded {__module_name__} version {__module_version__}")
print(f"{__module_description__}")

def jc_command_hook(word, word_eol, userdata):
    for chan in CHANS:
        hexchat.command(f"j {chan}")
    return hexchat.EAT_ALL

hexchat.hook_command("jc", jc_command_hook, help="/jc joins {}".format(" ".join(CHANS)))
