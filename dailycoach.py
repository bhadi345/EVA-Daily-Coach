import random
import requests

WEBHOOK="https://discord.com/api/webhooks/1515062659308064989/IjygD32R5dUZRva1tiKmovIIjswYXc_84dOVMbz2CDGMzLvVj6WZ_bhErIHnDnOGD5Ni"

with open("tips.txt","r",encoding="utf-8") as f:
    tips=f.readlines()

tip=random.choice(tips).strip()

msg=f"""🎯 EVA Daily Coach

{tip}

💙 EVA Coaching"""

requests.post(
WEBHOOK,
json={"content":msg}
)

print("Gesendet")
