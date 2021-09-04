import html

from AigerAkabaneRobot import bot
from AigerAkabaneRobot.config import get_int_key
from AigerAkabaneRobot.utils.logger import log


async def channel_log(msg, info_log=True):
    chat_id = get_int_key("LOGS_CHANNEL_ID")
    if info_log:
        log.info(msg)

    await bot.send_message(chat_id, html.escape(msg, quote=False))
