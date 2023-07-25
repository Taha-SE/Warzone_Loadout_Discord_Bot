import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import os


url = "https://warzoneloadout.games/de/"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
def getTopWeapons():
  results_dict = {}
  weapons = soup.find("div", class_="wz2_weapontables")
  for w in weapons:
    weapon_atts = {}
    weapon_group = w.find("div", class_="weapon_group").text
    weapon_name = w.find("div", class_="wz2_weaponname").text
    weapon_name_voll = f"{weapon_name} - {weapon_group}"
    attachments = w.find_all("div", class_="accordion__attachment")
    for att in attachments:
      att_type = att.find("div", class_="accordion__attachment__type").text
      att_name = att.find("strong", class_="accordion__attachment__name").text
      if (att.find("div", class_="loadouts__attachment_tuning1")
          is not None) and (att.find(
            "div", class_="loadouts__attachment_tuning2") is not None):
        att_tuning_v = att.find("div",
                                class_="loadouts__attachment_tuning1").text
        att_tuning_h = att.find("div",
                                class_="loadouts__attachment_tuning2").text
        att_tuning = f"vertical: {att_tuning_v}, horizontal: {att_tuning_h}"
        weapon_atts[att_type] = (att_name, att_tuning)
      else:
        weapon_atts[att_type] = att_name

    results_dict[weapon_name_voll] = weapon_atts
  results = ""
  for weapon_name, weapon_dict in results_dict.items():
    results += f"{weapon_name}:\n"

    for attribute_name, attribute_value in weapon_dict.items():
      if isinstance(attribute_value, list):
        attribute_value = f"{attribute_value[0]} ({attribute_value[1]})"
      results += f"  {attribute_name}: {attribute_value}\n"
    results += "\n"
  return results


def getLoadoutByName(name):
    tables = soup.find_all("div",class_="wz2_weapontables")
    results=""
    results_dict = {}
    for table in tables:
        for w in table:
            weapon_atts = {}
            weapon_group = w.find("div", class_="weapon_group").text
            weapon_name = w.find("div", class_="wz2_weaponname").text
            weapon_name_voll= f"{weapon_name} - {weapon_group}"
            if weapon_name.lower() == name.lower():
                attachments = w.find_all("div",class_="accordion__attachment")
                for att in attachments:
                    att_type= att.find("div",class_="accordion__attachment__type").text
                    att_name= att.find("strong", class_="accordion__attachment__name").text
                    if(att.find("div", class_="loadouts__attachment_tuning1") is not None) and (att.find("div", class_="loadouts__attachment_tuning2") is not None):
                        att_tuning_v = att.find("div", class_="loadouts__attachment_tuning1").text
                        att_tuning_h = att.find("div", class_="loadouts__attachment_tuning2").text
                        att_tuning = f"vertical: {att_tuning_v}, horizontal: {att_tuning_h}"
                        weapon_atts[att_type] = (att_name,att_tuning)
                    else: 
                        weapon_atts[att_type] = att_name
                results_dict[weapon_name_voll] = weapon_atts 
    if len(results_dict) ==0:
        results = "Waffe nicht gefunden. Check den Namen, oder probiere es mit einer anderen Waffe!"
    for weapon_name, weapon_dict in results_dict.items():
        results += f"{weapon_name}:\n"
        for attribute_name, attribute_value in weapon_dict.items():
            if isinstance(attribute_value, list):
                attribute_value = f"{attribute_value[0]} ({attribute_value[1]})"
            results += f"  {attribute_name}: {attribute_value}\n"
        results += "\n"
    return results     


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def meta(ctx):
    await ctx.send(getTopWeapons())
  
@bot.command()
async def loadout(ctx, arg):
  await ctx.send(getLoadoutByName(arg))
bot.run('DISCORD_API_KEY')
