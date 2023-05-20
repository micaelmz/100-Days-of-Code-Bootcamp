from instafollower import InstaFollower
from time import sleep

LOGIN = ""
PASSWORD = ""
TARGET_ACCOUNT = "instagram"
TARGET_FOLLOWERS = 100

insta_bot = InstaFollower()
i = 0

insta_bot.login(LOGIN, PASSWORD)
sleep(2)
insta_bot.load_followers_page(TARGET_ACCOUNT)
sleep(3)

while i < TARGET_FOLLOWERS:
    followers = insta_bot.find_followers()
    for follower in followers[i:]:
        insta_bot.follow(follower)
        sleep(1)
        i += 1
    if i >= TARGET_FOLLOWERS:
        break

input("Press enter to exit")
