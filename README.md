# Warzone Loadout Discord Bot
 
This is a Discord bot that provides information about the top weapons and their attachments in Call of Duty: Warzone. The bot scrapes data from a website and responds to user commands with relevant loadout details.

## Setup
To run this bot, you need to have Python and the following libraries installed:
- discord.py
- beautifulsoup4
- requests

You can install these dependencies using pip: 
`pip install discord.py beautifulsoup4 requests`

## Usage
### 1. Clone the Repository
`git clone https://github.com/Taha-SE/Warzone_Loadout_Discord_Bot.git`
### 2. Configure Discord API Token
Before running the bot, you need to set up a Discord bot and get its API token.
- Go to the Discord Developer Portal (https://discord.com/developers/applications) and create a new application.
- Under the "Bot" tab, click on "Add Bot" to create a new bot.
- Copy the token and replace 'DISCORD_API_KEY' with your bot's token in the last line of the code.

### 3. Run Bot
`python main.py`

## Commands
- $meta: This command displays information about the top weapons and their attachments in Call of Duty: Warzone.
- $loadout "weapon_name": Use this command to get details of a specific weapon and its attachments. Replace \<weapon_name\> with the name of the weapon you want to look up.

## Examples
`$meta`
This command will display information about the top weapons and their attachments in Warzone.

`$loadout "Grau 5.56"`
This command will provide loadout details for the weapon "Grau 5.56" and its attachments.

## Note
This bot relies on web scraping to gather data, and the website's structure might change over time. If the bot stops working correctly, consider checking if the website structure has been updated and adjust the scraping code accordingly.

