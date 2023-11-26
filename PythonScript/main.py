from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes




TOKEN :Final = "6965325512:AAGzBV_KsElHRfEZ4Q4ph7kCq88mBgOpMpI"
BOT_USERNAME:Final = '@mengeashebnir1234bot'

# Commands 
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! thankes for chatting with me ! I am mengistu ")


async def help_command(upadate:Update,context:ContextTypes.DEFAULT_TYPE):
    await upadate.message.reply_text("I am mengistu typing something here so i can help you ")
    
 
async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" this is a custom command! ")
    
# Responses

def handle_response(text: str)->str:
    processed :str = text.lower()


    if "hello" in processed:
        return "hey there"
    if "how are you"in processed:
        return "I am good"
    if "i love python" in processed:
        return "Remember to subscribe!"
    
    return "I do not understand what you wrote ..."


async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text

    print(f"user ({update.message.chat.id}) in {message_type} :'{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text : str = text.replace(BOT_USERNAME,'').strip()
            response :str =handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)    

    print('Bot:',response)

    await update.message.reply_text(response)


async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__== '__main__':
    print("staring bot...")


    app = Application.builder().token(TOKEN).build()
    #  Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #  Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    # Errors
    app.add_error_handler(error)

    print("polling...")
    app.run_polling(poll_interval=3)



    








     




























# from aiogram import Dispatcher,Bot, types 
# from aiogram import executor   

# bot = Bot(token = "6965325512:AAGzBV_KsElHRfEZ4Q4ph7kCq88mBgOpMpI")
# dp = Dispatcher(bot=bot)

# @dp.message_handler()
# async def echo_bot(mes:types.Message)->None:
#     await mes.answer(mes.text)
    
# if __name__ == "__main__":
#     executor.start_polling(dispatcher=dp)




