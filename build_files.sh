python3.9 -m pip install -r requirements.txt
sudo apt install libsqlite3-dev
./configure --enable-loadable-sqlite-extensions && make && sudo make install
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic