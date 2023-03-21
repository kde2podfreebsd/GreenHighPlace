# GreenHighPlace | Phuket Telegram bot shop for GreenHighPlace

## Check Telegram Bot - https://t.me/GreenHighPlaceBot

### 1. Struct of project | [Miro design](https://miro.com/welcomeonboard/MHZNUUZ4T0pGUGJLbm5RZ2xVZE5MSGw3T0NGZThYUExRcUdIcnlBeUh0N2lVaXdxM3pvZGhEWlZOZHVwRHRiZXwzMDc0NDU3MzU0NzgyMTA3MTY5fDI=?share_link_id=2729402969)
```
.
├── app
│   ├── attachments
│   │   └── saverEmptyDirectory
│   ├── bot
│   │   ├── bot.py
│   │   ├── __init__.py
│   │   ├── markups.py
│   │   └── tools.py
│   ├── config
│   │   ├── config.py
│   │   └── __init__.py
│   ├── files
│   │   └── saverEmptyDirectory
│   ├── __init__.py
│   ├── migrations
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 7de62e106479_.py
│   ├── models
│   │   ├── ActiveOrderModel.py
│   │   ├── AdminModel.py
│   │   ├── CartModel.py
│   │   ├── CompleteOrderModel.py
│   │   ├── CustomerModel.py
│   │   ├── __init__.py
│   │   ├── NewProductModel.py
│   │   ├── postModel.py
│   │   ├── ProductModel.py
│   │   └── RefusalOrderModel.py
│   ├── utils
│   │   ├── databaseResponseModel.py
│   │   └── __init__.py
│   └── wsgi.py
├── config.ini
├── docker-compose-devdb.yaml
├── README.md
└── requirements.txt
```

### 2. Prepair and Start project
#### 2.1 .env file
```
TelegramBotToken = '<your_telegram_bot_token>'
YandexGeoToken = '<your_yandex_geocoder_api_token>'
```
#### 2.2 Start postgresql in docker-compose 
```.sh
docker-compose -f docker-compose-devdb.yaml up
```

#### 2.3 Change database ip in config.ini
```.sh
### Grep Ip
docker inspect pgdb | grep IPAddress
```

```.ini
[POSTGRESQL_DATABASE]
host = <IPAddress>
port = 5432
database = greenhighplace
user = root
password = root
```

#### 2.4 Make migrations
```.sh
cd app/

flask db init
flask db migrate 
flask db upgrade 
```

2.5 Export PythonPath
```.sh
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

#### 2.6 For upgrade database
```.sh
flask db migrate 
flask db upgrade 
```

#### 2.6 Start Bot
```.sh
python app/bot/bot.py
```
