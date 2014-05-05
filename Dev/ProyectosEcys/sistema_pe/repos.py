'''
comandos importantes:
git log --pretty=format:"%h - %an, %ar : %s" --stat
'''
import os

REPO_DIR = '/Repos/'
USER = 'ojr'
THRUSTED_KEY = '/home/'+USER+'/.ssh/authorized_key'


def configurar(usuario, direccion):
    REPO_DIR = direccion
    USER = usuario


def crear_repositorio(identificador):
    ''' crea una carpeta con el repo en /home/git'''
    absolute_dir = REPO_DIR + identificador +'.git'
    os.system('mkdir '+absolute_dir)
    os.system('git --bare init')
    return True


def agregar_llave_ssh(llave):
    try:
        cadenas = str.split(llave)
        for linea in cadenas:
            os.system('echo ' + linea + ' >> ' + THRUSTED_KEY)

        return True
    except:
        return False




def obtener_branchs(repo):
    absolute_dir = REPO_DIR + repo +'.git'
    cd = 'cd ' + absolute_dir
    command_git = 'git branch'
    command = cd + ' && ' +command_git
    result = os.popen(command)
    branchs = []

    for r in result:
        a = r.replace('*',' ')
        branchs.append(a.strip())

    result.close()
    return branchs

def obtener_commits(repo, branch):
    absolute_dir = REPO_DIR + repo +'.git'
    cd = 'cd ' + absolute_dir
    gitlog = 'git log --pretty=format:"%h:%an:%ar:%s" '
    command_git = gitlog + branch
    command = cd + ' && ' + command_git
    result = os.popen(command)
    todo = []
    for r in result:
        fila = r.split(":")
        info = {"hexa":fila[0],"nombre":fila[1],
                "tiempo":fila[2],"comentario":fila[3]}
        todo.append(info)

    result.close()
    return todo




