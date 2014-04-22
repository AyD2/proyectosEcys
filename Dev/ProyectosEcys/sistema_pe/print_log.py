

def app_mensaje(mensaje):
    log = open("log/app.log",'a')
    log.write(mensaje+'\n')
