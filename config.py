# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 8560623))
    API_HASH = os.environ.get("API_HASH", "d1f72390990c765e4816e77a1e5a5cfd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1536292101").split())
    DOWNLOAD_LOCATION = "./megafiles/"
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "False")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", -489))
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "likeracademy@gmail.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "r72450162")

# Text Prints
B_START_TEXT = """
   __  ___                                     ___       __ 
  /  |/  /__ ___ ____ _      ___  ___   ____  / _ )___  / /_
 / /|_/ / -_) _ `/ _ `/ _   / _ \/_ /  /___/ / _  / _ \/ __/
/_/  /_/\__/\_, /\_,_/ (_) /_//_//__/       /____/\___/\__/ 
           /___/

Process: {}
"""

PROCESS_TEXT = """
Process: {}
"""

LOGGED_AS_USER = """
Successfully Logged Into Mega.nz User Account
"""

LOGIN_ERROR_TEXT = """
Can't Get Mega Email and Password Login as an Anonymouse User
"""

ERROR_TEXT = """
 _____                     
| ____|_ __ _ __ ___  _ __ 
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |   
|_____|_|  |_|  \___/|_|  

Log: {}

Save the Log file and Send it to @Nexa_bots for Help :)
"""

START_TEXT="""
    _   __                   ____        __      
   / | / /__  _  ______ _   / __ )____  / /______
  /  |/ / _ \| |/_/ __ `/  / __  / __ \/ __/ ___/
 / /|  /  __/>  </ /_/ /  / /_/ / /_/ / /_(__  ) 
/_/ |_/\___/_/|_|\__,_/  /_____/\____/\__/____/ 


Bot is Running Now! Join @NexaBotsUpdates
"""
