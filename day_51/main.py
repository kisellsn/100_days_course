import os
import time
from dotenv import load_dotenv
from day_50_tinder_swipe.internet_speed_twitter_bot import InternetSpeedTwitterBot

load_dotenv()
GUARANTEED_DOWNLOAD_SPEED = 150
GUARANTEED_UPLOAD_SPEED = 10
CHROME_DRIVER_PATH = '/Users/kisellsn/Development/chromedriver'

bot = InternetSpeedTwitterBot(GUARANTEED_DOWNLOAD_SPEED, GUARANTEED_UPLOAD_SPEED)


# down, up = bot.get_internet_speed()
bot.tweet_at_provider(50, 9)





