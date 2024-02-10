import random
import ujson

user_pass = ujson.load(open("config.json"))["proxy_username_password"]

proxy = random.choice(open("proxies.csv").read().splitlines()).split(",")

print("https://" + user_pass + "@" + proxy[1] + ":" + proxy[2])
