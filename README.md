# django_stripe

http://194.36.178.183/

/item/1 - получение товаров

Кнопка "Buy" добавляет в корзину товар.

Кнопка "Заказать" получает session.id и редиректит на checkout.

После нажатия на кнопку "Заказать" корзина очищается.

Чтобы у заказа выставить discount или tax, нужно сделать это в админке.

admin panel: /admin

login: admin password: admin1

Работает на nginx + gunicorn

Запуск:
  
virtualenv env

. env/bin/activate

python3 -m pip install -r requirements.txt

Добавить в /config/.env переменные для подключения к postgresql
и переменные с ключами от stripe

./manage.py migrate

./manage.py runserver, либо же настроить веб-сервер

Пояснения к коду есть в самом коде в виде комментариев
