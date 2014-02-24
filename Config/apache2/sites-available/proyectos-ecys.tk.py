<virtualhost *:80>
ServerName proyectos-ecys.tk
DocumentRoot /var/www/web
<Directory /var/www/web>
Order allow,deny
Allow from all
</Directory>
WSGIDaemonProcess web.djangoserver processes=2 threads=15 display-name=%{GROUP}
WSGIProcessGroup web.djangoserver
WSGIScriptAlias / /var/www/web/apache.conf/web.wsgi
Alias /media /var/www/web/media/
<Directory /var/www/web/media>
Order deny,allow
Allow from all
</Directory>
Alias /static/admin /usr/lib/pymodules/python2.7/django/contrib/admin/media/
<Directory /usr/lib/pymodules/python2.7/django/contrib/admin/media>
Order deny,allow
Allow from all
</Directory>
</virtualhost>

