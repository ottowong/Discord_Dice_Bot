# discordDiceBot
It's a Discord bot that you can use to roll dice

## Running

You will need:
- [A Discord bot](https://discordapp.com/developers/applications)
- [Python](http://python.org/downloads)
- Python's discord module<br>
  `pip install discord`

Paste your Discord bot's token to into the dicebot.py file and run it.

## How to use
format your messages in the format:
 !r[number of dice]d[number of sides]

for example:<br>
 `!r1d20`

you can also add a modifier or roll multiple dice by adding:<br>
 `+[number]`

or<br>
 `+[number of dice]d[number of sides]`

to the end of your message. e.g.<br>
 `!r1d20+2d6+5`

do not roll more than 10 dice with more than 1000 sides with a modifier greater than 1000 or more than 10 different dice.
