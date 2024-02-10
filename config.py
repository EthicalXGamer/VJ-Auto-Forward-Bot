from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "ec241c37a122cda302d68cb1415d2bff")
      API_ID = int(getenv("API_ID", "22368708"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6613760701:AAGdUwTIeZzQ_avAB5F-UlxGDNxntS0d_2c")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002007585466:-1002067804488").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
