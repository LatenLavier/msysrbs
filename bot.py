import logging
import requests
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import pymysql
con = pymysql.connect(host = "mysql-33521-0.cloudclusters.net", port = 33536, user="admin", passwd="K8AshjJN",db="sistema")
cursor = con.cursor()
grupo = -1001202002760
def sumar(update, context):
    numero1 = int(context.args[0])
    cursor.execute ("SELECT * FROM employees WHERE telefono =%s",numero1)
    hasil =  cursor.fetchall ()
    if cursor.rowcount > 0:
        for row in hasil:
            output = "๐ฑ Telefono: " + row[2] + "\n๐ค Nombre: " + row[1] + "\n๐ Domicilio: " + row[5] + "\n๐  Colonia: " + row[6] +  "\n๐ Postal: " + row[7] + "\n โ Marca: " + row[3]
        context.bot.send_message(grupo, output )
def ine(update, context):
    numero2 = context.args[0]
    cursor.execute ("SELECT * FROM usuarios WHERE curp =%s",numero2)
    hasil =  cursor.fetchall ()
    if cursor.rowcount > 0:
        for row in hasil:
            output = " ๐คNombre: " + row[2]+ "\n๐ Fecha Nac: " + str(row[5]) + "\n ๐Calle : " +  str(row[8]) + "\n ๐Num de casa: " + str(row[10]) + "\n ๐ Postal: "+ str(row[7])
        context.bot.send_message(grupo, output )
   

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
