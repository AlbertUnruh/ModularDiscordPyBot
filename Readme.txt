In `Configs.json` you must set the Token and Prefix.
You also can define some other variables in there.
(the own class `AttrDict` (*1) allows you, to get a value by calling it as an attribute und also as an item)

Utils.py is for the class `Help` that is used for the `help`-command

The module `Modules` is for the commands, each `.py`-file has the same name as the command and must have the following structure:
/--------------------------------------
| test.py:
|
| HELP = Utils.Help()  # you can leave the brackets empty, it will also work
| Branch = Utils.Branch.on_ready  # is to let the bot know, where the bot has to run the command
|
| async def __main__(client, message):  # client is a discord.Client and message is a discord.Message
|     pass  # here you can run your command
\--------------------------------------

`Bot.py` is the file, that is going to run the Bot.


---------------------------------------
*1:
    url: https://github.com/AlbertUnruh/NewClass/blob/main/AttrDict.py
    you must download the files and then import it in your command-files, if you want, but you need the file `AttrDict` OR the module `NewClass` for `Bot.py`
