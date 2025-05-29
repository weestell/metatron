# METATRON VOICE Welcome Bot

Telegram bot for welcoming new members to the METATRON VOICE channel.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your bot token:
```
BOT_TOKEN=your_bot_token_here
```

5. Run the bot:
```bash
python bot.py
```

## Features
- Welcomes new members with personalized message
- Sends welcome media file
- Handles private message interactions 