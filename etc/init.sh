ln -sf $PWD/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
#ln -sf $PWD/gunicorn.conf /etc/gunicorn.d/test
#/etc/init.d/gunicorn restart

#gunicorn -b :8000 --pythonpath /home/box/web/ask/ask wsgi:application&
