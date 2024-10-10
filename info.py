import os
# Bot information
API_ID = os.getenv('API_ID', "18029060")
API_HASH = os.getenv('API_HASH', "c7e952440251e33bb5cce566b29f7254")
BOT_TOKEN = os.getenv('BOT_TOKEN', "7082078294:AAGWIeE1zSxBHVncVM10shxP8grw3_327rA")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = os.getenv("BIN_CHANNEL", "-1002376421685") #Log Channel
URL = os.getenv("URL", "https://vocational-darsie-jsfillerv2-5407b1b3.koyeb.app") #App URL not MongoDB URL
