from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 2095537199
bot_user = "BDTGXBOT"
api_id = 18026880
api_hash = "d8d5482bf8fc23b9a47f8d0931124911"
session = "1BJWap1wBu0yH9SFXVPZ1qjCQ02uhyOYWfFEfXlewr3nA4tvssBlq4UQhSSCkKiA35C9Aa-TaMFRkpO8HvGkZOW5mF9vwYxgKG_hNaytA5xFbpf98AuLbyzdLEkEf3PUcfo0Kig7aZl5Mfn3T0FZfYaiJU2buL7uayqsCXAOjgPm46RctrMi4rizstBHWFXmCjOtmYJ-G0hnwYGFh5Z59L9BrjEBAm5YuTysGqxNBHHuMDWyaXtKRSdRdwjgX-dcQNLB0dDY5Qkd_yodV4s9wFozleb9T_v-2YOrwy_pQUH4X8SOZ_IyPMjtSqOwsZu10al1jMHtAx882RPu8EJfmBRYwB-77ygA="
token = "2123292337:AAElITfux1Wmj70hViVWEtTIQVZ991PepDU"
pm = "-1001356928994"
mention = "-1001356928994"
plugins = dict(root="plugins")
app = Client("user:bot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("bot_id",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))