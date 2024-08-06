import os

from dotenv import load_dotenv

from day_52_insta_follower_bot.insta_follower_bot import InstaFollower

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


bot = InstaFollower(USERNAME, PASSWORD)

bot.login()
bot.find_followers()
bot.follow()