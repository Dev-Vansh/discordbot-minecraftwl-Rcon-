import discord
import requests
from discord.ext import commands
from mcrcon import MCRcon
from dotenv import load_dotenv
import os

# Must Change Env Files 
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
RCON_HOST = os.getenv("RCON_HOST")
RCON_PORT = int(os.getenv("RCON_PORT"))
RCON_PASSWORD = os.getenv("RCON_PASSWORD")
MONITOR_CHANNEL_ID = int(os.getenv("MONITOR_CHANNEL_ID"))
LIMITED_ROLE_ID = int(os.getenv("LIMITED_ROLE_ID"))
UNLIMITED_ROLE_ID = int(os.getenv("UNLIMITED_ROLE_ID"))
AUTO_ROLE_ID = int(os.getenv("AUTO_ROLE_ID"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

whitelist_used = {}

# -------- BOT SETUP --------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="U Till U Whitelist Yourself • Made By Vansh"
    ))
    print(f'✅ Bot is online as {bot.user}')
    print("💡 Made by Vansh")
    print("💡 Join Our Discord For More Updates")
    print("💡 discord.gg/heavymc")
    print("███████╗██╗ ██████╗ ███╗   ███╗ █████╗     ███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗ ")
    print("██╔════╝██║██╔════╝ ████╗ ████║██╔══██╗    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗ ")
    print("███████╗██║██║  ███╗██╔████╔██║███████║    ███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║  ")
    print("╚════██║██║██║   ██║██║╚██╔╝██║██╔══██║    ╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║  ")
    print("███████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║    ███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝  ")
    print("╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝   ")
                                                                                         


@bot.event
async def on_message(message):
    if message.author.bot or message.channel.id != MONITOR_CHANNEL_ID:
        return

    roles = [role.id for role in message.author.roles]
    user_id = message.author.id
    content = message.content.strip()

    if content.startswith('!') and not content.startswith('!uwl') and not content.startswith('!auto'):
        username = content[1:].strip()

        if UNLIMITED_ROLE_ID in roles:
            await whitelist_user(username, message)

        elif LIMITED_ROLE_ID in roles:
            if whitelist_used.get(user_id, 0) >= 1:
                await message.channel.send('🚫 You can only whitelist **1 username.**')
            else:
                await whitelist_user(username, message)
                whitelist_used[user_id] = whitelist_used.get(user_id, 0) + 1

        else:
            await message.channel.send('🚫 You do not have permission to whitelist players.')

    elif content.startswith('!uwl '):
        if UNLIMITED_ROLE_ID in roles:
            username = content[5:].strip()
            await unwhitelist_user(username, message)
        else:
            await message.channel.send('🚫 You do not have permission to unwhitelist players.')

    elif content.startswith('!auto '):
        if AUTO_ROLE_ID in roles:
            cmd = content[6:].strip()
            await run_auto_command(cmd, message)
        else:
            await message.channel.send('🚫 You do not have permission to use auto commands.')

    await bot.process_commands(message)

async def whitelist_user(username, message):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            mcr.command(f'whitelist add {username}')

        embed_success = discord.Embed(
            title="✅ Whitelist Successful!",
            description=f"Player **{username}** has been successfully whitelisted!",
            color=0x00ff00
        )
        embed_success.add_field(name="Whitelisted By", value=message.author.mention, inline=False)
        embed_success.set_footer(text="Thank you for supporting our server! ❤️")
        await message.channel.send(embed=embed_success)

        webhook_message = {
            "embeds": [{
                "title": "✅ Whitelist Success",
                "description": f"**IGN:** `{username}`\n**By:** {message.author.mention}",
                "color": 3066993
            }]
        }
        requests.post(WEBHOOK_URL, json=webhook_message)

        try:
            embed_dm = discord.Embed(
                title="🎉 Whitelist Successful!",
                description=f"Thank you for supporting our server!\nYou have successfully whitelisted **{username}**.\n\nWe appreciate you being part of our community! 💖",
                color=0x00ff00
            )
            embed_dm.set_footer(text="Enjoy your time on the server!")
            await message.author.send(embed=embed_dm)
        except Exception as e:
            print(f"❌ Could not send DM: {e}")

    except Exception as e:
        print(f'❌ Error: {e}')
        await message.channel.send('❌ An error occurred while whitelisting.')

async def unwhitelist_user(username, message):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            mcr.command(f'whitelist remove {username}')

        embed_success = discord.Embed(
            title="🗑️ Unwhitelist Successful!",
            description=f"Player **{username}** has been successfully removed from the whitelist!",
            color=0xff0000
        )
        embed_success.add_field(name="Unwhitelisted By", value=message.author.mention, inline=False)
        embed_success.set_footer(text="Whitelist update complete.")
        await message.channel.send(embed=embed_success)

        webhook_message = {
            "embeds": [{
                "title": "🗑️ Unwhitelist Success",
                "description": f"**IGN:** `{username}`\n**By:** {message.author.mention}",
                "color": 15158332
            }]
        }
        requests.post(WEBHOOK_URL, json=webhook_message)

    except Exception as e:
        print(f'❌ Error: {e}')
        await message.channel.send('❌ An error occurred while unwhitelisting.')

async def run_auto_command(cmd, message):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            mcr.command(cmd)

        embed_success = discord.Embed(
            title="⚙️ Auto Command Executed",
            description=f"Command: `{cmd}`\n\nExecuted successfully.",
            color=0x3498db
        )
        embed_success.add_field(name="Executed By", value=message.author.mention, inline=False)
        embed_success.set_footer(text="Command sent to server via RCON.")
        await message.channel.send(embed=embed_success)

        webhook_message = {
            "embeds": [{
                "title": "⚙️ Auto Command Executed",
                "description": f"**Command:** `{cmd}`\n**By:** {message.author.mention}",
                "color": 3447003
            }]
        }
        requests.post(WEBHOOK_URL, json=webhook_message)

    except Exception as e:
        print(f'❌ Error: {e}')
        await message.channel.send('❌ An error occurred while executing the command.')

bot.run(DISCORD_TOKEN)
