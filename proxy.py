import random
user_pass = "0j86x5ku-mn35b8v:8z3gd752ub"

proxy = random.choice(open("proxies.csv").read().splitlines()).split(",")

print("https://" + user_pass + "@" + proxy[1] + ":" + proxy[2])