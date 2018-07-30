cd "C:\Users\Holodnuk.LOCAL\YandexDisk\blogs\mcold\"
pelican content
cd output
del .html
vivaldi.exe http://localhost:8000
python -m SimpleHTTPServer