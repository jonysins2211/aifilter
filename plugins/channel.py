from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

# Accept video, audio, and document messages from specified channels
media_filter = filters.chat(CHANNELS) & (filters.video | filters.audio | filters.document)

@Client.on_message(media_filter)
async def media_handler(bot, message):
    """Handles incoming media (video, audio, document) and saves it to the database"""
    file_type = None
    media = None

    if message.video:
        media = message.video
        file_type = "video"
    elif message.audio:
        media = message.audio
        file_type = "audio"
    elif message.document:
        media = message.document
        file_type = "document"

    if not media:
        return

    media.file_type = file_type
    media.caption = message.caption

    await save_file(media)
    print(f"⭕ Auto Indexed ✅ ({file_type})")
