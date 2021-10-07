# weather

# For local deploy
docker-compose -f docker-compose.local.yml up -d;


#Then local run
docker-compose -f docker-compose.local.yml exec weather-django python manage.py migrate

#API CALLS:
```weather/?city=&lat=&lon&units=&lang= ``` <p>
```city - название города``` <p>
```lat & lon -  координаты``` <p>
```Можно использовать поиск по городу, либо по координатам, в приоритете город```<p>
```units - системы счисления:  "standard","metric","imperial"```<p>
```lang - язык "ru","en"```