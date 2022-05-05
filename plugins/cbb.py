# (©)Codexbotz
# Recode by @mrismanaziz
# Recode by @RYUUSHINNI

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • 𝘽𝘼𝘾𝘼 𝙆𝙊𝙈𝙄𝙆 𝙃𝙀𝙉𝙏𝙄 >: @Doujindesukomik\n • 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝙍𝘼𝙍𝙀 𝙆𝙊𝙇𝙀𝙆𝙎𝙄 >: @RareCollectionID\n • 𝙆𝙊𝙇𝙀𝙆𝙎𝙄 𝙇𝙊𝙆𝘼𝙇 >: @LokalPrideid\n • 𝙑𝙄𝘿𝙀𝙊 𝙑𝙄𝙍𝘼𝙇 >: <a href='https://t.me/viralbelatungid'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
