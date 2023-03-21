# GreenHighPlace | Phuket Telegram bot shop for GreenHighPlace

## Check Telegram Bot - https://t.me/GreenHighPlaceBot

## Description: 
2-roles telegram shop bot for online orders.
roles: User, Admin

User Functionality:
* Language change
* Change of address + comment to the address (+ automatic sending of geo-location via the telegram widget
* My orders (list of orders + all order information)
* Shopping cart + Order
* Write to the administrator on the current order via the bot

Admin Functionality:
* Orders (Active\Cancelled\Completed) + Change of order statuses (Transferred to the courier/Cancel the order)
* Receiving notification of new orders
* Write to the user on the current order
* Post promotion (send a post to all bot users)
* Product catalog (creating a new product + editing old ones)
* Language change
* Log out of the admin panel

### 1. [Miro design](https://miro.com/welcomeonboard/MHZNUUZ4T0pGUGJLbm5RZ2xVZE5MSGw3T0NGZThYUExRcUdIcnlBeUh0N2lVaXdxM3pvZGhEWlZOZHVwRHRiZXwzMDc0NDU3MzU0NzgyMTA3MTY5fDI=?share_link_id=2729402969)

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
