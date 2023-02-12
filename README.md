# django_stripe

http://194.36.178.183:8000/

/item/<id> - получение товаров

Кнопка "Buy" добавляет в корзину товар

Кнопка "Заказать" получает session.id и редиректит на checkout

После нажатия на кнопку "Заказать" корзина очищается

Работает на nginx + gunicorn

Запуск:

virtualenv env

. env/bin/activate

python3 -m pip install -r requirements.txt

Создать в директории config файл .env и добавить туда переменные для подключения к postgresql
и переменные с ключами от stripe

./manage.py runserver

Либо же настроить веб-сервер

Поясннения к коду есть в самом коде в виде комментариев