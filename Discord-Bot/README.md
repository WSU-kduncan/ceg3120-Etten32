- Documentation for Project1BobTheBot
  - Setup
    - To obtain a Discord API token, go to the Discord Developer website (found at the following link: https://discord.com/developers/applications) and select the application. Navigate to the 'Bot' tab, and click 'Copy' underneath were it says 'TOKEN'.
    - Next create a file called '.env' in the same directory as the bot.py code is stored
    - Within the file write '# .env', followed by newline, followed by 'DISCORD_TOKEN=', followed by the contents of the Token that has been copied to the clipboard. 
    - In order for the bot to work, the following must be installed:
      - Python3    (sudo apt install Python3)
      - pip3       (sudo apt install pip3)
      - discord.py (pip3 install discord.py)
      - dotenv     (pip3 install -U python-dotenv)
  - Usage
    - In order to use the bot once it has been activated on a server, type the command "mmm" in a message.
    - Upon the command "mmm", the bot will randomly select and post one from six qoutes taken from three stories relating to the names: Molly, Megan, and Milo.
  - Research
    - you may have realized that it is lame that it only runs when you run the program.
    In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.
    Research some possible solutions that would solve this, and discuss why you think it would work. !!!!!
