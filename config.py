# Copyrighted by Aresona & Sentric Nova 2024-2025
# Please do not modify any file if you don't sure what you doing.
# --------------------------------------Credits---------------------------------#
# Sentric Nova -> For his best ideas and making it shorts.
# Aresona -> For coding and making it short as much possible.
# Support channel --> social_bots.t.me
# Support Group --> Join social_bots's comment box
# Please gives credits if you fork or anything. also join our support channels too.


# Configuration variables
CONFIG_VARS = {
    "API_ID": ,
    "API_HASH": "",
    "BOT_TOKEN": "",
    "LOGGER_GROUP": int(""),
    "PHONE_NUMBER": "",
    "OWNER_ID": []
}

# SUDO_ID is derived from OWNER_ID
SUDO_ID = [None]

# Check for missing configuration variables
missing_vars = [var for var, value in CONFIG_VARS.items() if not value]

if missing_vars:
    print("The following variables are missing:")
    for var in missing_vars:
        print(f"  - {var}")
    print("Please fill in the above variables for the userbot to work properly.")
    import sys
    sys.exit("User bot exited due to missing configuration variables.")
else:
    print("All configuration variables are set!")

# Accessing variables
API_ID = CONFIG_VARS["API_ID"]
API_HASH = CONFIG_VARS["API_HASH"]
BOT_TOKEN = CONFIG_VARS["BOT_TOKEN"]
LOGGER_GROUP = CONFIG_VARS["LOGGER_GROUP"]
PHONE_NUMBER = CONFIG_VARS["PHONE_NUMBER"]
OWNER_ID = CONFIG_VARS["OWNER_ID"]
SUDO_USERS = CONFIG_VARS["OWNER_ID"][:] + SUDO_ID
