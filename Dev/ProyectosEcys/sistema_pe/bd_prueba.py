'''solo sirve para llenar la bd con datos de prueba'''
from sistema_pe.models import Usuario, Clase, Proyecto
from sistema_pe.models import Semestre, Repositorio, Asignacion
import hashlib

c = hashlib.sha512('prueba').hexdigest()
def llenar():
    usuario1 = Usuario(carnet=200811111, nombre='prueba1', clave=c, tipo_usuario=True, correo='orfrant@gmail.com')
    usuario2 = Usuario(carnet=200822222, nombre='prueba2', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')
    usuario3 = Usuario(carnet=200833333, nombre='prueba3', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')
    usuario4 = Usuario(carnet=200844444, nombre='prueba4', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')
    usuario5 = Usuario(carnet=200855555, nombre='prueba5', clave=c, tipo_usuario=True, correo='orfrant@gmail.com')
    usuario6 = Usuario(carnet=200866666, nombre='prueba6', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')
    usuario7 = Usuario(carnet=200877777, nombre='prueba7', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')
    usuario8 = Usuario(carnet=200888888, nombre='prueba8', clave=c, tipo_usuario=False, correo='orfrant@gmail.com')

    usuario1.save()
    usuario2.save()
    usuario3.save()
    usuario4.save()
    usuario5.save()
    usuario6.save()
    usuario7.save()
    usuario8.save()

    s1 = Semestre(year=2014, etapa=0)
    s7 = Semestre(year=2013, etapa=2)

    s1.save()
    s7.save()

    ayd = Clase(nombre='ayd', seccion='A', semestre=s1, tutor=usuario1)
    ayd2 = Clase(nombre='ayd', seccion='B', semestre=s1, tutor=usuario5)
    bases = Clase(nombre='bases', seccion='A', semestre=s1, tutor=usuario5)

    ayd.save()
    ayd2.save()
    bases.save()

    pAydA = Proyecto(clase=ayd, creador=usuario1, fecha_entrega='2014-03-03'
            , fecha_creacion='2014-02-02', contenido="<h1>proyecto 1</h1>" )
    pAydB = Proyecto(clase=ayd2, creador=usuario5, fecha_entrega='2014-03-03'
            , fecha_creacion='2014-02-02', contenido="<h1>proyecto 1</h1>" )
    p1bases = Proyecto(clase=bases, creador=usuario5, fecha_entrega='2014-03-03'
            , fecha_creacion='2014-02-02', contenido="<h1>proyecto 1</h1>" )
    p2bases = Proyecto(clase=bases, creador=usuario5, fecha_entrega='2014-04-04'
            , fecha_creacion='2014-03-03', contenido="<h1>proyecto 2</h1>" )

    pAydA.save()
    pAydB.save()
    p1bases.save()
    p2bases.save()

#########asignaciones

    Asignacion(id_carnet=usuario2, id_Clase=ayd).save()
    Asignacion(id_carnet=usuario3, id_Clase=ayd).save()
    Asignacion(id_carnet=usuario4, id_Clase=ayd).save()

    Asignacion(id_carnet=usuario6, id_Clase=ayd2).save()
    Asignacion(id_carnet=usuario7, id_Clase=ayd2).save()
    Asignacion(id_carnet=usuario8, id_Clase=ayd2).save()

    Asignacion(id_carnet=usuario1, id_Clase=bases).save()
    Asignacion(id_carnet=usuario2, id_Clase=bases).save()
    Asignacion(id_carnet=usuario3, id_Clase=bases).save()
    Asignacion(id_carnet=usuario4, id_Clase=bases).save()
    Asignacion(id_carnet=usuario6, id_Clase=bases).save()
    Asignacion(id_carnet=usuario7, id_Clase=bases).save()
    Asignacion(id_carnet=usuario8, id_Clase=bases).save()

##########repositorios

    Repositorio(proyecto=pAydA, usuario=usuario2,
            direccion='/p_'+str(usuario2.carnet)).save()
    Repositorio(proyecto=pAydA, usuario=usuario3,
            direccion='/p_'+str(usuario3.carnet)).save()
    Repositorio(proyecto=pAydA, usuario=usuario4,
            direccion='/p_'+str(usuario4.carnet)).save()
    Repositorio(proyecto=pAydB, usuario=usuario6,
            direccion='/p_'+str(usuario6.carnet)).save()
    Repositorio(proyecto=pAydB, usuario=usuario7,
            direccion='/p_'+str(usuario7.carnet)).save()
    Repositorio(proyecto=pAydB, usuario=usuario8,
            direccion='/p_'+str(usuario8.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario1,
            direccion='/p_'+str(usuario1.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario2,
            direccion='/p_'+str(usuario2.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario3,
            direccion='/p_'+str(usuario3.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario4,
            direccion='/p_'+str(usuario4.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario6,
            direccion='/p_'+str(usuario6.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario7,
            direccion='/p_'+str(usuario7.carnet)).save()
    Repositorio(proyecto=p1bases, usuario=usuario8,
            direccion='/p_'+str(usuario8.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario1,
            direccion='/p_'+str(usuario1.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario2,
            direccion='/p_'+str(usuario2.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario3,
            direccion='/p_'+str(usuario3.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario4,
            direccion='/p_'+str(usuario4.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario6,
            direccion='/p_'+str(usuario6.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario7,
            direccion='/p_'+str(usuario7.carnet)).save()
    Repositorio(proyecto=p2bases, usuario=usuario8,
            direccion='/p_'+str(usuario8.carnet)).save()



