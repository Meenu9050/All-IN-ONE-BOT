import asyncio
import pyrogram

from AloneX import pbot
from AloneXMusic import config, logger


class Bot:
    def __new__(cls):
        pbot.owner = config.OWNER_ID
        pbot.logger = config.LOGGER_ID
        pbot.bl_users = pyrogram.filters.user()
        pbot.sudoers = pyrogram.filters.user(config.OWNER_ID)

        async def boot():
            for _ in range(30):
                if getattr(pbot, "me", None):
                    break
                await asyncio.sleep(1)

            pbot.id = pbot.me.id
            pbot.name = pbot.me.first_name
            pbot.username = pbot.me.username
            pbot.mention = pbot.me.mention

            try:
                await pbot.send_message(config.LOGGER_ID, "Music Bot Started")
                get = await pbot.get_chat_member(config.LOGGER_ID, pbot.id)
            except Exception as ex:
                raise SystemExit(
                    f"Bot has failed to access the log group: {config.LOGGER_ID}\nReason: {ex}"
                )

            if get.status != pyrogram.enums.ChatMemberStatus.ADMINISTRATOR:
                raise SystemExit("Please promote the bot as an admin in logger group.")

            logger.info(f"Music handlers attached to @{pbot.username}")

        async def exit():
            logger.info("Music bot bridge stopped.")

        pbot.boot = boot
        pbot.exit = exit
        return pbot
