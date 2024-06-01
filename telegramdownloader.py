from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant
from colorama import Fore, Style
from tqdm import tqdm

from colorama import init
init()

r = Fore.RED
ye = Fore.YELLOW
re="\033[1;31m"
gr="\033[1;32m"
wi="\033[1;35m"

api_id = 'api id' #-- enter your api id.
api_hash = 'api hash' #-- enter your api hash.
phone_number = 'phone number' #-- enter your tg phone number.

app = Client(
    'my_user',
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone_number,
)
app.start()

link_or_dialog = input(f"{Fore.CYAN}{Style.BRIGHT}Do you want to use a link or a dialog? (Type 'link' or 'dialog'): {re}")

if link_or_dialog.lower() == 'link':
    group_link = input(f"{Fore.CYAN}{Style.BRIGHT}If PRIVATE enter link if PUBLIC enter username: {re}")
    try:
        app.join_chat(group_link)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
    try:
        raj = app.get_chat(group_link)
    except Exception as e:
        print(e)
    selected_ids_str = input(f"{Fore.GREEN}{Style.BRIGHT}Enter the message IDs you want to download (separated by spaces): {Style.RESET_ALL}")
    selected_ids = map(int, selected_ids_str.split())

    for selected_id in selected_ids:
        selected_message = app.get_messages(raj.id, selected_id)

        try:
            def progress_bar(current, total):
                with tqdm(total=total, desc="Downloading...", bar_format="{l_bar}{bar}{r_bar}") as pbar:
                    pbar.update(current)
            app.download_media(selected_message, progress=progress_bar)
            print(f"{Fore.MAGENTA + Style.BRIGHT}Media downloaded successfully for Message ID {selected_id}!{Style.RESET_ALL}")
        except Exception as e:
            print(f"Error downloading for Message ID {selected_id}: {e}")



elif link_or_dialog.lower() == 'dialog':
    print(f"{Fore.CYAN}{Style.BRIGHT}Choose a channel: {re}")
    try:
        dialogs = list(app.get_dialogs())
        for index, dialog in enumerate(dialogs):
            print(f"{re}{index + 1}. {gr}{dialog.chat.first_name or dialog.chat.title}")
    except Exception as e:
        print(e)

    selected_channel_index = int(input(f"{Fore.CYAN}{Style.BRIGHT}Enter the number of the channel you want to explore: {re}")) - 1

    selected_channel = dialogs[selected_channel_index].chat

    print(f"{Fore.CYAN}{Style.BRIGHT}Do you want to get messages from the entire channel/dialog or by a specific message ID?")
    preference = input(f"{Fore.GREEN}{Style.BRIGHT}Type 'channel' for entire channel, 'message' for a specific message ID: {re}")

    if preference.lower() == 'channel':
        limitenter = int(input(f"{Fore.YELLOW + Style.BRIGHT}Enter Limit of messages or use 0 all messages: {re}"))
        try:
            messages = app.get_chat_history(selected_channel.id, limitenter)
            print(Fore.RED + Style.BRIGHT + "All media in the channel:" + Style.RESET_ALL)
            for message in messages:
                if message.caption:
                    print(Fore.MAGENTA + Style.BRIGHT + f"{message.id}. {ye + Style.BRIGHT}Caption: {re}{message.caption} {wi}Media Type: {gr}{message.media}" + Style.RESET_ALL)
                else:
                    print(Fore.BLUE + Style.BRIGHT + f"{message.id}. {ye + Style.BRIGHT}Caption: {re}No Caption | {wi}Media Type: {gr}{message.media}" + Style.RESET_ALL)
        except Exception as e:
            print(e)
        selected_ids_str = input(f"{Fore.GREEN}{Style.BRIGHT}Enter the message IDs you want to download (separated by spaces): {Style.RESET_ALL}")
        selected_ids = map(int, selected_ids_str.split())

        for selected_id in selected_ids:
            selected_message = app.get_messages(selected_channel.id, selected_id)

            try:
                def progress_bar(current, total):
                    with tqdm(total=total, desc="Downloading...", bar_format="{l_bar}{bar}{r_bar}") as pbar:
                        pbar.update(current)
                app.download_media(selected_message, progress=progress_bar)
                print(f"{Fore.MAGENTA + Style.BRIGHT}Media downloaded successfully for Message ID {selected_id}!{Style.RESET_ALL}")
            except Exception as e:
                print(f"Error downloading for Message ID {selected_id}: {e}")

    elif preference.lower() == 'message':
        selected_ids_str = input(f"{Fore.GREEN}{Style.BRIGHT}Enter the message IDs you want to download (separated by spaces): {Style.RESET_ALL}")
        selected_ids = map(int, selected_ids_str.split())

        for selected_id in selected_ids:
            selected_message = app.get_messages(selected_channel.id, selected_id)

            try:
                def progress_bar(current, total):
                    with tqdm(total=total, desc="Downloading...", bar_format="{l_bar}{bar}{r_bar}") as pbar:
                        pbar.update(current)
                app.download_media(selected_message, progress=progress_bar)
                print(f"{Fore.MAGENTA + Style.BRIGHT}Media downloaded successfully for Message ID {selected_id}!{Style.RESET_ALL}")
            except Exception as e:
                print(f"Error downloading for Message ID {selected_id}: {e}")

    else:
        print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please type 'channel' or 'message'.{Style.RESET_ALL}")

else:
    print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please type 'link' or 'dialog'.{Style.RESET_ALL}")
    
#fogpiercer
#roothanedan