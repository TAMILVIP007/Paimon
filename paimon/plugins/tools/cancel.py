# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# Edited by Alicia

from paimon import Message, paimon


@paimon.on_cmd("cancel", about={"header": "Reply this to message you want to cancel"})
async def cancel_(message: Message):
    if replied := message.reply_to_message:
        replied.cancel_the_process()
        await message.edit("`added your request to the cancel list`", del_in=5)
    else:
        await message.edit("`reply to the message you want to cancel`", del_in=5)
