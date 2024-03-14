
import tensorflow as tf
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Load your trained chatbot model
model = tf.keras.models.load_model('/content/chatbot_model.h5')

def generate_response(text):
    # Implement logic to process user input and generate a response using your model
    # This will depend on how your model is designed and what input format it expects
    # Replace this placeholder logic with your actual model inference code
    response = "Your response here."
    return response

def start(update, context):
    update.message.reply_text("Hello! I'm your STEM chatbot. Ask me anything!")

def handle_messages(update, context):
    user_input = update.message.text
    # Generate a response using your chatbot model
    response = generate_response(user_input)
    update.message.reply_text(response)

def main():
    updater = Updater("6614625526:AAHyWOocwVEvee_PiViwVnAfY1f-7C8lF0U", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
