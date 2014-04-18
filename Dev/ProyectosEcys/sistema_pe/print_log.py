

def app_mensaje(mensaje):
    log = open("logs/app.log",'a')
    log.write(mensaje+'\n')
