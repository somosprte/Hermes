# NOT READY
FROM : python:onbuild

apt install sqlite3

pip install -r requirements.txt

COPY . .

