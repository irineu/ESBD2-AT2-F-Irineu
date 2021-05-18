# ESBD2-AT2-F-Irineu
Atividade 2 do segundo módulo do MBA de Machine Learning da UFSCar

`
source ESBD2-AT2/bin/activate
pip install django
pip install selenium

python3 manage.py migrate
python3 manage.py runserver

python3 manage.py dumpdata lists > testdb.json
python manage.py loaddata testdb.json

brew install cask
brew install chromedriver

#SET PATH /usr/local/bin/chromedriver

python manage.py testserver testdb.json
`
