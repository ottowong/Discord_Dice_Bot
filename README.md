# discordDiceBot
It's a Discord bot that you can use to roll dice

## Running

You will need:
- [A Discord bot](https://discordapp.com/developers/applications)
- [Python](http://python.org/downloads) (I used 3.7.2 but other versions might work idk)
- Python's discord module<br>
  `pip install discord`

Paste your Discord bot's token to into the dicebot.py file and run it.

## How to use
Format your messages in the format:
 !r[number of dice]d[number of sides]

For example:<br>
 `!r1d20`

You can also add a modifier or roll multiple dice by adding:<br>
 `+[number]`

Or<br>
 `+[number of dice]d[number of sides]`

To the end of your message. e.g.<br>
 `!r1d20+2d6+5`
 
 You can subtract a number by adding:<br>
 `+-[number]`

As shorthand to roll 1d20 you can also do:<br>
`!r`

## Known Issues
* If you do e.g. 1d20 +- 1d10 it will try to roll -1d10 rather than 1d10 and subtract the result
* The +- syntax is annoying and I don't know how/can't be bothered to fix it
