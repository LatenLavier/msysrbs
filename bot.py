import logging
import requests
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import pymysql
con = pymysql.connect(host = "mysql-33521-0.cloudclusters.net", port = 33536, user="admin", passwd="K8AshjJN",db="sistema")
cursor = con.cursor()
def sumar(update, context):
    numero1 = int(context.args[0])
    cursor.execute ("SELECT * FROM employees WHERE telefono =%s",numero1)
    hasil =  cursor.fetchall ()
    if cursor.rowcount > 0:
        for row in hasil:
            output = "📱 Telefono: " + row[2] + "\n👤 Nombre: " + row[1] + "\n🌐 Domicilio: " + row[5] + "\n🏠 Colonia: " + row[6] +  "\n📍 Postal: " + row[7] + "\n ✅ Marca: " + row[3]
        context.bot.send_message(update.message.chat.id, output )

def ine(update, context):
    numero2 = str(context.args[0])
    cursor.execute ("SELECT * FROM usuarios WHERE nombre =%s",numero2)
    hasil =  cursor.fetchall ()
    if cursor.rowcount > 0:
        for row in hasil:
            output = " 👤NOMBRE: " + row[2] + "\n📅 NACIMIENTO: " + row[5] + "\n🌐 UBICACION: " + row[8] + "\n🏠 COLONIA: " + row[9] +  "\n📍 POSTAL: " + row[7] + "\n 📄 CURP: " + row[7]
        context.bot.send_message(update.message.chat.id, output )
   

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def perro(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater("1997242106:AAGk6QGCaVtXRr5G0zVpAZJ9SertyKT_iv0", use_context=True)
    # el token lo guardamos en un a variable llamada botm3
    botm3 = updater.dispatcher

    botm3.add_handler(CommandHandler("telcel", sumar))
    botm3.add_handler(CommandHandler("ine", ine))

    updater.start_polling()

    #Aqui decimos que es un bulce y que no pare hasta que le demos a ctrl+c 
    updater.idle()

if __name__ == '__main__':
    main()
