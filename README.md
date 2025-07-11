# discordbot-minecraftwl-Rcon-
A Bot That Will Allow  Person to be  Whitelist in a Minecraft Server  From Discord 

A powerful and secure Discord bot that allows specific users to whitelist, unwhitelist, and send raw RCON commands to your Minecraft server — all with beautiful embed messages, permission controls, and webhook logging.

----->>> Features
- Per-user whitelist limit for users with a limited role.
- Unlimited whitelist/unwhitelist for users with a higher role.
- Auto RCON command execution for users with a third specific role.
- Webhook integration for logs and notifications.
- Private DM confirmation for successful whitelistings.
- Clean, embedded Discord messages instead of plain text.



## 🔧 Setup
### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Edit Config in `bot.py`
Update:
- `DISCORD_TOKEN`
- `RCON_HOST`, `RCON_PORT`, `RCON_PASSWORD`
- `MONITOR_CHANNEL_ID`
- `LIMITED_ROLE_ID`, `UNLIMITED_ROLE_ID`, `AUTO_ROLE_ID`
- `WEBHOOK_URL`

### 3. Enable RCON in `server.properties`
```
enable-rcon=true
rcon.password=YOUR_RCON_PASSWORD
rcon.port=25575
```

### 4. Run the bot
```bash
python bot.py
```

## Cmd 
```!<username>	 --------------->  Whitelist a Minecraft IGN	Limited / Unlimited Role     ```                                 

```!uwl <username> ------------>	Unwhitelist a Minecraft IGN	Unlimited Role```

``` !auto <cmd>	-------------> Run any Minecraft server command via RCON	Auto Role ( Its Like Console ) ```


## 🧾 License
MIT License





If U Have Any Problem U Can  Contact me on Discord - discord.gg/heavymc or u Can Send Dm on Vansh_1901
If U Are Intrested In Our Custom Plugin By Sigma Studio U Can Also Check Out Us 

