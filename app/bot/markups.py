from telebot import types
from telegram_bot_pagination import InlineKeyboardPaginator
from app.models import ProductModel as pm
from app.models import CustomerModel as db
from app.models import ActiveOrderModel as ao
hideMenu = types.ReplyKeyboardRemove()

# до меню профиль-купить

toBuyMarkupRU = "Купить 🛍"
toProfileMarkupRU = "Профиль 👤"
toBuyMarkupEN = "Buy 🛍"
toProfileMarkupEN = "Profile 👤"

start_msg = '''
Hi!
Choose language

Привет!
Выбери язык
    '''

switchLanguage = types.InlineKeyboardMarkup(row_width=1)
languageEN = types.InlineKeyboardButton("English 🇺🇸", callback_data="EN")
languageRU = types.InlineKeyboardButton("Русский 🇷🇺", callback_data="RU")
switchLanguage.add(languageEN, languageRU)


def welcomeText(language: str):
    if language == "RU":
        return '''Привет!
Ты в крутом магазине на крутом острове
Можешь сделать заказ и оформить доставку'''

    if language == "EN":
        return '''Hello!
You are in the cool boshkiShop on cool Island
You can make an order and do delivery'''


def askLocation(language: str):
    if language == "RU":
        return "Напишите свой адрес или отправьте свою геолокацию"

    if language == "EN":
        return "Write your address or send geolocation"


sendLocationRU = types.KeyboardButton("Отправить геолокацию 📍", request_location=True)
writeLocationRU = types.KeyboardButton("Написать адрес текстом 🏘")
passLocationRU = types.KeyboardButton("Пропустить сейчас ➡️")
sendLocationEN = types.KeyboardButton("Send location 📍", request_location=True)
writeLocationEN = types.KeyboardButton("Write the address in text 🏘")
passLocationEN = types.KeyboardButton("Pass now ➡")


def menuLocation(language: str):
    menuLocation = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    if language == "RU":

        return menuLocation.add(sendLocationRU, writeLocationRU, passLocationRU)

    elif language == "EN":

        return menuLocation.add(sendLocationEN, writeLocationEN, passLocationEN)


def menuBuyProfile(language: str):
    menuBuyProfile = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    if language == "RU":
        toBuyRU = types.KeyboardButton(toBuyMarkupRU)
        toProfileRU = types.KeyboardButton(toProfileMarkupRU)
        return menuBuyProfile.add(toBuyRU, toProfileRU)

    elif language == "EN":
        toBuyEN = types.KeyboardButton(toBuyMarkupEN)
        toProfileEN = types.KeyboardButton(toProfileMarkupEN)
        return menuBuyProfile.add(toBuyEN, toProfileEN)


passCommentRU = types.InlineKeyboardButton("Пропустить ➡️", callback_data="passCommentAdress")
passCommentEN = types.InlineKeyboardButton("Pass ➡️", callback_data="passCommentAdress")


# toBackEN = types.InlineKeyboardButton("To back", callback_data="toBackFromCommentAdress")

def toCommentAdress(language: str):
    toCommentAdress = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":

        return toCommentAdress.add(passCommentRU)

    elif language == "EN":

        return toCommentAdress.add(passCommentEN)


def addressInfo(language: str, address: str):
    if language == "RU":
        return f'Адрес: {address}\nЕсли он неверный, измените его в профиле'

    elif language == "EN":
        return f'Address: {address}\nIf it incorrect, change one in profile'


def toCommentAddress(language: str):
    if language == "RU":
        return 'Укажите комментарий к адресу:'
    elif language == "EN":
        return 'Write comment for adrress:'


def inviteToWriteAddress(language: str):
    if language == "RU":
        return 'Введите ваш полный адрес и отправьте:'
    elif language == "EN":
        return 'Write your complete address and send:'


def addressAddedSuccessfully(language: str):
    if language == "RU":
        return 'Адрес успешно добавлен!\nМожешь переходить к покупкам!'
    elif language == "EN":
        return 'Address has added successfully!\nYou can go to buy!'


toShopRU = types.InlineKeyboardButton("В магазин 🛍", callback_data="toShop")
toShopEN = types.InlineKeyboardButton("To shop 🛍", callback_data="toShop")
toProfileRU = types.InlineKeyboardButton("В профиль 👤", callback_data="backToProfile")
toProfileEN = types.InlineKeyboardButton("To profile 👤", callback_data="backToProfile")
def toShop(language: str):
    toShop = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        return toShop.add(toShopRU, toProfileRU)

    elif language == "EN":
        return toShop.add(toShopEN, toProfileEN)


def indexAddreessLater(language: str):
    if language == "RU":
        return "Если понадобится, ты можешь указать адрес в профиле"

    elif language == "EN":
        return "If it'll be need, you can point address at profile"


# профиль
profileMarkup = types.InlineKeyboardMarkup(row_width=1)
profileButtonRU1 = types.InlineKeyboardButton("Изменить адрес 🏘", callback_data="changeAddress")
profileButtonRU2 = types.InlineKeyboardButton("Мои заказы 💌", callback_data="myOrders")
profileButtonRU3 = types.InlineKeyboardButton("Корзина 🛒", callback_data="bin")
# profileButtonRU4 = types.InlineKeyboardButton("Реферальная система", callback_data="refSystem")
profileButtonRU6 = types.InlineKeyboardButton("Изменить язык 🇷🇺🇺🇸", callback_data="changeLanguage")

profileButtonEN1 = types.InlineKeyboardButton("Change address 🏘", callback_data="changeAddress")
profileButtonEN2 = types.InlineKeyboardButton("My orders 💌", callback_data="myOrders")
profileButtonEN3 = types.InlineKeyboardButton("Cart 🛒", callback_data="bin")
# profileButtonEN4 = types.InlineKeyboardButton("Ref system", callback_data="refSystem")
profileButtonEN6 = types.InlineKeyboardButton("Change language 🇷🇺🇺🇸", callback_data="changeLanguage")


def profileMenu(language: str):
    profileMarkup = types.InlineKeyboardMarkup(row_width=1)
    if language == "RU":
        return profileMarkup.add(profileButtonRU3, profileButtonRU2, profileButtonRU1,
                                 profileButtonRU6)

    elif language == "EN":
        return profileMarkup.add(profileButtonEN3, profileButtonEN2, profileButtonEN1,
                                 profileButtonEN6)


def getInfoProfile(language: str, address: str, comment: str):
    if language == "RU":
        return f'''*Профиль*
*Адрес:* {address if address is not None else "не указан"}
*Комментарий к адресу:* {comment if comment is not None else "не указан"}'''

    elif language == "EN":
        return f'''*Profile*
*Address:* {address if address is not None else "didn't point"}
*Comment for address:* {comment if comment is not None else "didn't point"}'''


def textOfChangingLanguage(language: str):
    if language == "RU":
        return 'Выберите язык'

    elif language == "EN":
        return 'Choose language'


switchLanguageProfile = types.InlineKeyboardMarkup(row_width=1)
languageProfileEN = types.InlineKeyboardButton("English 🇺🇸", callback_data="profileEN")
languageProfileRU = types.InlineKeyboardButton("Русский 🇷🇺", callback_data="profileRU")
switchLanguageProfile.add(languageProfileEN, languageProfileRU)


# шоп

class sliderShopPaginator(InlineKeyboardPaginator):
    first_page_label = '<<'
    previous_page_label = '<-'
    current_page_label = '·  {}  ·'
    next_page_label = '->'
    last_page_label = '>>'


def textShop(language, products):
    if len(products) != 0:
        if language == "RU":
            return "Список товаров\nВыберите нужный и нажмите"
        elif language == "EN":
            return "List of products\nChoose you needed and push"
    else:
        if language == "RU":
            return "Сейчас товаров нет в магазине 😔"
        if language == "EN":
            return "Now at shop there aren't products 😔"


def sliderShop(page, products, language):
    if len(products) != 0:

        nameOfProducts = list(i.name for i in products)
        idOrders = list(i.id for i in products)
        paginator = sliderShopPaginator(page_count=len(nameOfProducts),
                                        current_page=page,
                                        data_pattern='listProduct#{page}')

        lookProduct = types.InlineKeyboardButton('{}'.format(nameOfProducts[page - 1]),
                                                 callback_data='productName#{}'.format(idOrders[page - 1]))
        paginator.add_before(lookProduct)

        if language == "RU":

            toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='backToProfile')
            paginator.add_after(toBackButton)

        elif language == "EN":

            toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='backToProfile')
            paginator.add_after(toBackButton)

        return paginator.markup

    else:
        menuBack = types.InlineKeyboardMarkup(row_width=1)
        if language == "RU":
            toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
            return menuBack.add(toBack)
        if language == "EN":
            toBack = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
            return menuBack.add(toBack)


class sliderProductPaginator(InlineKeyboardPaginator):
    first_page_label = ''
    previous_page_label = ' - '
    next_page_label = ' + '
    last_page_label = ''


def textProduct(name, infoAbout, price, language):
    if language == "RU":
        return f'''{name}
        
{infoAbout.split("#")[0]}

Доставка по всему острову
1 грамм - {price} BATH'''

    elif language == "EN":
        return f'''{name}
        
{infoAbout.split('#')[1]}

Delivery on the whole Island
1 gram - {price} BATH'''


def sliderProduct(page, name, price, language):
    paginator = sliderProductPaginator(
        page_count=500,
        current_page=page,
        data_pattern='coast#' + name + '#{page}'
    )
    paginator.current_page_label = '{}' + ' | {} BATH'.format(int(page) * price)

    if language == "RU":

        # toChooseNumberOf = types.InlineKeyboardButton('Указать количество', callback_data='toChooseNumberOf')
        # toOrderDelivery = types.InlineKeyboardButton('Заказать доставку', callback_data='toOrderDelivery')
        toCart = types.InlineKeyboardButton('В корзину 🛒', callback_data='toCart#{}#{}'.format(name, int(page)))
        toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='toShopFromVideo')
        paginator.add_before(toCart)
        paginator.add_after(toBackButton)

    elif language == "EN":

        # toChooseNumberOf = types.InlineKeyboardButton('Indicate quantity', callback_data='toChooseNumberOf')
        # toOrderDelivery = types.InlineKeyboardButton('Order delivery', callback_data='toOrderDelivery')
        toCart = types.InlineKeyboardButton('Add to cart 🛒', callback_data='toCart#{}#{}'.format(name, int(page)))
        toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='toShopFromVideo')

        paginator.add_before(toCart)
        paginator.add_after(toBackButton)

    return paginator.markup


def infoCart(num: int, language: str):
    if language == "RU":
        return "Товаров в корзине: {}\nОформи заказ через профиль".format(num)

    elif language == "EN":
        return "Items in the cart: {}\nPlace an order through your profile".format(num)


def textTrash(products, language):
    if len(products) != 0:

        if language == "RU":
            head = "*Товаров в корзине:* {}\n\nНажми на товар чтобы удалить или изменить".format(len(products))

            return head

        if language == "EN":
            head = "*Items in the cart:* {}\n\nTouch on product for delete or change".format(len(products))

            return head

    else:
        if language == "RU":
            return "Твоя корзина пуста 🤷‍♀️"
        if language == "EN":
            return "Your cart is empty 🤷‍♀️"


# def trashMenu(products, language):
#
#     trashMenu = types.InlineKeyboardMarkup(row_width=1)
#
#     if len(products) != 0:
#
#         totalsum = 0
#         for product in products:
#             product = str(product)
#
#             if pm.getPrice(product.split('#')[0]) != 0:
#
#                 name = product.split('#')[0]
#
#                 price = pm.getPrice(name)
#                 num = int(product.split('#')[1])
#                 sum = num * price
#                 totalsum += sum
#
#         if language == "RU":
#             toDeliver = types.InlineKeyboardButton("Заказать | {} BATH".format(totalsum), callback_data="toDeliver#{}".format(totalsum))
#             toClearBin = types.InlineKeyboardButton("Очистить корзину", callback_data="toClearBinWarning")
#             toBack = types.InlineKeyboardButton("Назад", callback_data="backToProfile")
#             trashMenu.add(toDeliver, toClearBin, toBack)
#
#         if language == "EN":
#             toDeliver = types.InlineKeyboardButton("Order | {} BATH".format(totalsum), callback_data="toDeliver#{}".format(totalsum))
#             toClearBin = types.InlineKeyboardButton("Empty trash", callback_data="toClearBinWarning")
#             toBack = types.InlineKeyboardButton("To back", callback_data="backToProfile")
#             trashMenu.add(toDeliver, toClearBin, toBack)
#     else:
#         if language == "RU":
#             toBack = types.InlineKeyboardButton("Назад", callback_data="backToProfile")
#             trashMenu.add(toBack)
#
#         if language == "EN":
#             toBack = types.InlineKeyboardButton("To back", callback_data="backToProfile")
#             trashMenu.add(toBack)
#
#     return trashMenu

def trashMenu(products, language):
    trashMenu = types.InlineKeyboardMarkup(row_width=1)

    if len(products) != 0:

        totalsum = 0
        i = 0
        for product in products:

            if pm.getPrice(product.idFromProduct) is not False:

                name = product.nameOfProduct

                price = pm.getPrice(product.idFromProduct)
                num = product.numOfProducts
                sum = num * price
                totalsum += sum

                if language == "RU":
                    button = types.InlineKeyboardButton(f"🌿 {name} | {str(num)} грамм | {price * num} BATH",
                                                        callback_data=f"toEdit#{product.id}")
                    trashMenu.add(button)
                if language == "EN":
                    button = types.InlineKeyboardButton(f"🌿 {name} | {str(num)} gramm | {price * num} BATH",
                                                        callback_data=f"toEdit#{product.id}")
                    trashMenu.add(button)

            i += 1

        if language == "RU":
            toDeliver = types.InlineKeyboardButton("🚚 Заказать | {} BATH".format(totalsum),
                                                   callback_data="toDeliver#{}".format(totalsum))
            toClearBin = types.InlineKeyboardButton("🧹 Очистить корзину", callback_data="toClearBinWarning")
            toBack = types.InlineKeyboardButton("⬅ Назад️", callback_data="backToProfile")
            trashMenu.add(toDeliver, toClearBin, toBack)

        if language == "EN":
            toDeliver = types.InlineKeyboardButton("🚚 Order | {} BATH".format(totalsum),
                                                   callback_data="toDeliver#{}".format(totalsum))
            toClearBin = types.InlineKeyboardButton("🧹 Empty trash", callback_data="toClearBinWarning")
            toBack = types.InlineKeyboardButton("⬅ Back️", callback_data="backToProfile")
            trashMenu.add(toDeliver, toClearBin, toBack)



    else:
        if language == "RU":
            toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
            trashMenu.add(toBack)

        if language == "EN":
            toBack = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
            trashMenu.add(toBack)

    return trashMenu


def areYouSureText(language):
    if language == "RU":
        return "Ты уверен?"

    if language == "EN":
        return "Are you sure?"


def areYouSureMenu(language):
    areYouSure = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        yes = types.InlineKeyboardButton("Очистить 🧹", callback_data="toClearBin")
        no = types.InlineKeyboardButton("Назад ⬅️", callback_data="bin")
        return areYouSure.add(yes, no)

    if language == "EN":
        yes = types.InlineKeyboardButton("To empty 🧹", callback_data="toClearBin")
        no = types.InlineKeyboardButton("Back ⬅️", callback_data="bin")
        return areYouSure.add(yes, no)


def beforeOrderText(address: str, comment: str, language: str):
    if address is not None:
        if language == "RU":
            return f'''*Адрес:* {address}
*Комментарий к адресу:* {comment if comment is not None else "не указан"}'''

        elif language == "EN":
            return f'''*Address:* {address}
*Comment for address:* {comment if comment is not None else "didn't point"}'''

    else:
        if language == "RU":
            return "Вы не указали адрес, укажите его для заказа"
        if language == "EN":
            return "You didn't point address. Point it for order"


def beforeOrderMenu(address: str, language: str, fullprice: int):
    confirmMenu = types.InlineKeyboardMarkup(row_width=1)

    if address is not None:

        if language == "RU":
            confirm = types.InlineKeyboardButton("Подтвердить ✅", callback_data="toConfirm#{}".format(fullprice))
            badAddress = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
            return confirmMenu.add(confirm, badAddress)
        if language == "EN":
            confirm = types.InlineKeyboardButton("Confirm ✅", callback_data="toConfirm#{}".format(fullprice))
            badAddress = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
            return confirmMenu.add(confirm, badAddress)

    else:
        if language == "RU":
            badAddress = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
            return confirmMenu.add(badAddress)
        if language == "EN":
            badAddress = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
            return confirmMenu.add(badAddress)


def chooseMethodPayText(language: str):
    if language == "RU":
        return "Выбери способ оплаты"

    if language == "EN":
        return "Choose method of pay"


def chooseMethodPayMenu(fullsum: int, language: str):
    methodsPay = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        forCash = types.InlineKeyboardButton("Наличные 💰", callback_data="forCash#{}".format(fullsum))
        # forCard = types.InlineKeyboardButton("Криптовалюта", callback_data="forCryptocurrency#{}".format(fullsum))
        toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
        return methodsPay.add(forCash, toBack)

    if language == "EN":
        forCash = types.InlineKeyboardButton("Cash payment 💰", callback_data="forCash#{}".format(fullsum))
        # forCard = types.InlineKeyboardButton("Сryptocurrency", callback_data="forCryptocurrency#{}".format(fullsum))
        toBack = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
        return methodsPay.add(forCash, toBack)


def infoOrderText(products: list, fullsum: int, address: str, comment: str, payment: str, language: str):
    if len(products) != 0:

        if language == "RU":

            head = "*Товаров:* {}\n\n*Товары:*  \n".format(len(products))

            for product in products:

                if pm.getPrice(product.idFromProduct) != 0:

                    name = product.nameOfProduct

                    price = pm.getPrice(product.idFromProduct)
                    num = product.numOfProducts
                    summ = num * price

                    head += "_{} - {} грамм - {} BATH_\n".format(name, num, summ)

                else:
                    name = product.split('#')[0]
                    head += 'Товар "{}" удален из магазина\n'.format(name)

            head += "\n*Итого:* {} BATH".format(fullsum)
            head += "\n\n*Адрес:* {}" \
                    "\n\n*Комментарий к адресу:* {}\n\n".format(address, comment if comment is not None else "не указан")

            if payment == "forCash":
                head += "*Метод оплаты:* наличные"

            return head

        if language == "EN":

            head = "*Items:* {}\n\n*Items:*\n".format(len(products))

            for product in products:

                if pm.getPrice(product.idFromProduct) != 0:

                    name = product.nameOfProduct

                    price = pm.getPrice(product.idFromProduct)
                    num = product.numOfProducts
                    summ = num * price

                    head += "_{} - {} gramm - {} BATH_\n".format(name, num, summ)

                else:
                    name = product.split('#')[0]
                    head += 'Item "{}" was delete from shop\n'.format(name)

            head += "\n*Total:* {} BATH".format(fullsum)
            head += "\n\n*Address:* {}" \
                    "\n\n*Comment for address:* {}\n\n".format(address,
                                                             comment if comment is not None else "didn't point")

            if payment == "forCash":
                head += "*Payment:* cash"

            return head

    else:
        pass


def infoOrderMenu(fullprice: int, payment: str, language):
    orderMenu = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        orderConfirm = types.InlineKeyboardButton("Подтвердить ✅",
                                                  callback_data="orderConfirm#{}#{}".format(fullprice, payment))
        orderRefuse = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
        return orderMenu.add(orderConfirm, orderRefuse)

    if language == "EN":
        orderConfirm = types.InlineKeyboardButton("Confirm ✅",
                                                  callback_data="orderConfirm#{}#{}".format(fullprice, payment))
        orderRefuse = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
        return orderMenu.add(orderConfirm, orderRefuse)


def confirmedOrderText(numberOfOrder: int, language: str):
    if language == "RU":
        return f'''*Номер заказа:* №{numberOfOrder}
*Заказ успешно создан*
Мы оповестим тебя, курьер примет заказ'''

    if language == "EN":
        return f'''*Number of order:* №{numberOfOrder}
*Order created succesfully*
We'll say you, when courier accepted the order'''


def confirmedOrderMenu(numberOfOrder: int, language: str):
    confirmedOrderMenu = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        toCurrentOrder = types.InlineKeyboardButton("К заказу 🛍", callback_data="toCurrentOrder#{}".format(numberOfOrder))
        toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
        return confirmedOrderMenu.add(toCurrentOrder, toBack)

    if language == "EN":
        toCurrentOrder = types.InlineKeyboardButton("To order 🛍", callback_data="toCurrentOrder#{}".format(numberOfOrder))
        toBack = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
        return confirmedOrderMenu.add(toCurrentOrder, toBack)


class sliderOrderPaginator(InlineKeyboardPaginator):
    first_page_label = ''
    previous_page_label = ' < '
    next_page_label = ' > '
    last_page_label = ''


def textOrder(active, refusal, complete, language):
    if len(active + refusal + complete) != 0:
        if language == "RU":
            return '*Все ваши заказы:*\n\n🟡 - заказ в процессе\n🔴 - заказ отменён\n🟢 - заказ завершён'

        if language == "EN":
            return '*All your orders:*\n\n🟡 - active order\n🔴 - refused order\n🟢 - completed order'
    else:
        if language == "RU":
            return 'У тебя еще нет заказов 🤷‍♀️'

        if language == "EN":
            return "You haven't orders yet 🤷‍♀️"


def sliderOrder(page, active, refusal, complete, language):
    # print("---", refusal)
    active.reverse()
    refusal.reverse()
    complete.reverse()
    # print("---", refusal)

    orders = active + refusal + complete

    if len(orders) != 0:
        a = len(active)
        r = len(refusal)
        total = len(orders)

        paginator = sliderOrderPaginator(
            page_count=total,
            current_page=page,
            data_pattern='order#{page}'
        )

        paginator.current_page_label = '· {} ·'
        print(orders[page - 1])
        if orders[page - 1] in active:
            lookOrder = types.InlineKeyboardButton("№{} | {} BATH 🟡".format(str(orders[page - 1]).split('-#-#-')[0],
                                                                            str(orders[page - 1]).split('-#-#-')[3]),
                                                   callback_data="lookActive#{}".format(page - 1))
            paginator.add_before(lookOrder)

        elif orders[page - 1] in refusal:
            lookOrder = types.InlineKeyboardButton("№{} | {} BATH 🔴".format(str(orders[page - 1]).split('-#-#-')[9],
                                                                            str(orders[page - 1]).split('-#-#-')[3]),
                                                   callback_data="lookRefusal#{}".format(page - 1 - a))
            paginator.add_before(lookOrder)

        elif orders[page - 1] in complete:

            lookOrder = types.InlineKeyboardButton("№{} | {} BATH 🟢".format(str(orders[page - 1]).split('-#-#-')[9],
                                                                            str(orders[page - 1]).split('-#-#-')[3]),
                                                   callback_data="lookComplete#{}".format(page - 1 - a - r))
            paginator.add_before(lookOrder)

        if language == "RU":

            toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='backToProfile')
            paginator.add_after(toBackButton)

        elif language == "EN":

            toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='backToProfile')
            paginator.add_after(toBackButton)

        return paginator.markup

    else:
        backingMenu = types.InlineKeyboardMarkup(row_width=1)

        if language == "RU":
            backingButton = types.InlineKeyboardButton("Назад ⬅️", callback_data="backToProfile")
            return backingMenu.add(backingButton)
        if language == "EN":
            backingButton = types.InlineKeyboardButton("Back ⬅️", callback_data="backToProfile")
            return backingMenu.add(backingButton)


def showActiveOrderText(activeOrders: list, choosedOrder: int, language: str):
    print(activeOrders)
    activeOrders.reverse()
    order = activeOrders[choosedOrder]
    order = str(order)

    if language == "RU":
        head = f"*Заказ №{order.split('-#-#-')[0]}*\n\n*Товары:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} грамм - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Итого:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Дата и время заказа:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Способ оплаты:* {order.split('-#-#-')[5]}"
        head += f"\n\n*Адрес для заказа:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Комментарий к адресу:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'не указан'}"
        if order.split('-#-#-')[6].split("#")[0] == "Передано на доставку":
            head += f"\n\n*Статус заказа:* {order.split('-#-#-')[6].split('#')[0]}"
            if order.split('-#-#-')[6].split('#')[1] != "":
                head += f"\n*Ориентировочное время доставки:*\n{order.split('-#-#-')[6].split('#')[1]}"
        else:
            head += f"\n\n*Статус заказа:* {order.split('-#-#-')[6]}"
        return head

    if language == "EN":
        head = f"*Order №{order.split('-#-#-')[0]}*\n\n*Items:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} gramm - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Total:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Date and time order:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Payment:* {'cash' if order.split('-#-#-')[5] == 'наличные' else '-'}"
        head += f"\n\n*Address for order:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Comment for address:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'did not point'}"
        if order.split('-#-#-')[6].split("#")[0] == "Передано на доставку":
            head += f"\n\n*Status order:* sent for delivery"
            if order.split('-#-#-')[6].split('#')[1] != "":
                head += f"\n*Estimated delivery time:*\n{order.split('-#-#-')[6].split('#')[1]}"
        else:
            head += f"\n\n*Status order:* waiting for courier"
        # head += f"\n\n*Status order:* {'waiting for courier' if order.split('-#-#-')[6] == 'ожидает курьера' else 'sent for delivety'}"
        return head


def showActiveOrderMenu(activeOrders: list, choosedOrder: int, language: str):
    showActiveOrderMenu = types.InlineKeyboardMarkup(row_width=1)


    activeOrders.reverse()
    idActive = activeOrders[choosedOrder].id


    if language == "RU":
        # добавить id ордера в колбэк дату
        toWriteCourier = types.InlineKeyboardButton("Написать курьеру ✏️", callback_data=f"toWriteCourier#{idActive}")
        toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data='myOrders')
        return showActiveOrderMenu.add(toWriteCourier, toBack)

    if language == "EN":
        toWriteCourier = types.InlineKeyboardButton("To write courier ✏️", callback_data=f"toWriteCourier#{idActive}")
        toBack = types.InlineKeyboardButton("Back ⬅️", callback_data='myOrders')
        return showActiveOrderMenu.add(toWriteCourier, toBack)


def showCompleteOrderText(completeOrders: list, choosedOrder: int, language: str):
    # print(completeOrders)
    completeOrders.reverse()
    order = completeOrders[choosedOrder]
    order = str(order)

    if language == "RU":
        head = f"*Заказ №{order.split('-#-#-')[9]}*\n\n*Товары:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} грамм - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Итого:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Дата и время заказа:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Способ оплаты:* {order.split('-#-#-')[5]}"
        head += f"\n\n*Адрес для заказа:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Комментарий к адресу:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'не указан'}"
        head += f"\n\n*Закрытие заказа:* {order.split('-#-#-')[6]}"
        return head

    if language == "EN":
        head = f"*Order №{order.split('-#-#-')[9]}*\n\n*Items:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} gramm - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Total:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Date and time order:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Payment:* {'cash' if order.split('-#-#-')[5] == 'наличные' else '-'}"
        head += f"\n\n*Address for order:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Comment for address:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'did not point'}"
        head += f"\n\n*Order closing:* {order.split('-#-#-')[6]}"
        return head


def showCompleteOrderMenu(language: str):
    showCompleteOrderMenu = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        # добавить id ордера в колбэк дату
        toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data='myOrders')
        return showCompleteOrderMenu.add(toBack)

    if language == "EN":
        toBack = types.InlineKeyboardButton("Back ⬅️", callback_data='myOrders')
        return showCompleteOrderMenu.add(toBack)


def showRefusalOrderText(refusalOrders: list, choosedOrder: int, language: str):
    # print(refusalOrders)
    refusalOrders.reverse()
    order = refusalOrders[choosedOrder]
    order = str(order)

    if language == "RU":
        head = f"*Заказ №{order.split('-#-#-')[9]}*\n\n*Товары:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} грамм - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Итого:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Дата и время заказа:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Способ оплаты:* {order.split('-#-#-')[5]}"
        head += f"\n\n*Адрес для заказа:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Комментарий к адресу:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'не указан'}"
        head += f"\n\n*Закрытие заказа:* {order.split('-#-#-')[6]}"
        head += f"\n*Причина закрытия:* {order.split('-#-#-')[10]}"
        return head

    if language == "EN":
        head = f"*Order №{order.split('-#-#-')[9]}*\n\n*Items:*\n"
        items = order.split('-#-#-')[2]

        for item in items[:-1].split(','):
            head += "_{} - {} gramm - {} BATH_\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n*Total:* {order.split('-#-#-')[3]} BATH"
        head += f"\n\n*Date and time order:* {order.split('-#-#-')[4]}"
        head += f"\n\n*Payment:* {'cash' if order.split('-#-#-')[5] == 'наличные' else '-'}"
        head += f"\n\n*Address for order:* {order.split('-#-#-')[7]}"
        head += f"\n\n*Comment for address:* " \
                f"{order.split('-#-#-')[8] if order.split('-#-#-')[8] != 'None' else 'did not point'}"
        head += f"\n\n*Order closing:* {order.split('-#-#-')[6]}"
        head += f"\n*Reason of refusal:* {order.split('-#-#-')[10]}"
        return head


class sliderChangeBinPaginator(InlineKeyboardPaginator):
    first_page_label = ''
    previous_page_label = ' - '
    next_page_label = ' + '
    last_page_label = ''


def textBinProduct(language):
    if language == "RU":
        return 'Изменение.......'

    elif language == "EN":
        return 'Changing.......'


def sliderChangeBin(page, product, language):
    paginator = sliderChangeBinPaginator(
        page_count=500,
        current_page=page,
        data_pattern='binslide#' + str(product.id) + '#{page}'
    )
    paginator.current_page_label = '· {} ·'

    if language == "RU":

        productInfo = types.InlineKeyboardButton(f"{product.nameOfProduct} | "
                                                 f"{pm.getPrice(product.idFromProduct) * product.numOfProducts} BATH",
                                                 callback_data='nowork')

        toDeleteButton = types.InlineKeyboardButton('Удалить ❌', callback_data=f'DeleteFromBin#{product.id}')
        toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='bin')
        paginator.add_before(productInfo)
        paginator.add_after(toBackButton, toDeleteButton)

    elif language == "EN":

        productInfo = types.InlineKeyboardButton(f"{product.nameOfProduct} | "
                                                 f"{pm.getPrice(product.idFromProduct) * product.numOfProducts} BATH",
                                                 callback_data='nowork')

        toDeleteButton = types.InlineKeyboardButton('Delete ❌', callback_data=f'DeleteFromBin#{product.id}')
        toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='bin')
        paginator.add_before(productInfo)
        paginator.add_after(toBackButton, toDeleteButton)

    return paginator.markup


def deletedItemText(name, language):
    if language == "RU":
        return f'Ты совершил ошибку, удалив "{name}"'
    if language == "EN":
        return f'You made a mistake: "{name}" deleted'


toAdminTextRU = "Администрирование"
toAdminTextEN = "Administration"
password = "123"

def toEnterPasswordText(language):
    if language == "RU":
        return "Введите пароль доступа"
    if language == "EN":
        return "Enter password"

def passwordCorrectText(language):
    if language == "RU":
        return "Доступ одобрен"
    if language == "EN":
        return "Access approved"


def passwordUncorrectText(language):
    if language == "RU":
        return "Отказано в доступе"
    if language == "EN":
        return "Access denied"

def helloBoss(language):
    if language == "RU":
        return "Привет, Босс!"
    if language == "EN":
        return "Hello, Boss!"

def helloMenu(language):
    bossMenu = types.InlineKeyboardMarkup(row_width=1)

    if language == "RU":
        orders = types.InlineKeyboardButton("Заказы", callback_data="adminOrders")
        postSale = types.InlineKeyboardButton("Пост-акция", callback_data="adminPostSale")
        catalog = types.InlineKeyboardButton("Каталог товаров", callback_data="adminCatalog")
        lang = types.InlineKeyboardButton("Сменить язык", callback_data="adminSwitchLanguage")
        exitAdmin = types.InlineKeyboardButton("Выйти из админ панели", callback_data="exitAdmin")
        return bossMenu.add(orders, postSale, catalog, lang, exitAdmin)

    if language =="EN":
        orders = types.InlineKeyboardButton("Orders", callback_data="adminOrders")
        postSale = types.InlineKeyboardButton("Post news", callback_data="adminPostSale")
        catalog = types.InlineKeyboardButton("Catalog", callback_data="adminCatalog")
        lang = types.InlineKeyboardButton("Switch language", callback_data="adminSwitchLanguage")
        exitAdmin = types.InlineKeyboardButton("Exit admin", callback_data="exitAdmin")
        return bossMenu.add(orders, postSale, catalog, lang, exitAdmin)
def mainAdmin(language):
    adminMainMenu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if language == "RU":
        adminMainButton = types.KeyboardButton("На главную")
        return adminMainMenu.add(adminMainButton)
    if language == "EN":
        adminMainButton = types.KeyboardButton("Main menu")
        return adminMainMenu.add(adminMainButton)

def chooseListOrdersText(language):
    if language == "RU": return "Выбери список заказов"
    if language == "EN": return "Choose list of orders"

def chooseListOrdersMenu(language):
    chooseListOrdersMenu = types.InlineKeyboardMarkup(row_width=1)
    if language == "RU":
        listActive = types.InlineKeyboardButton("Активные", callback_data="activeList")
        listRefusal = types.InlineKeyboardButton("Отмененные", callback_data="refusalList")
        listComplete = types.InlineKeyboardButton("Завершенные", callback_data="completeList")
        toBack = types.InlineKeyboardButton("Назад ⬅️", callback_data="toMainAdmin")
        return chooseListOrdersMenu.add(listActive, listRefusal, listComplete, toBack)
    if language == "EN":
        listActive = types.InlineKeyboardButton("Active", callback_data="activeList")
        listRefusal = types.InlineKeyboardButton("Canceled", callback_data="refusalList")
        listComplete = types.InlineKeyboardButton("Completed", callback_data="completeList")
        toBack = types.InlineKeyboardButton("Back ⬅️", callback_data="toMainAdmin")
        return chooseListOrdersMenu.add(listActive, listRefusal, listComplete, toBack)

class adminSliderOrderPaginator(InlineKeyboardPaginator):
    first_page_label = '<<'
    previous_page_label = ' < '
    next_page_label = ' > '
    last_page_label = '>>'


def AdminTextOrderActive(active, language):
    if len(active) != 0:
        if language == "RU":
            return 'Список активных заказов:'
        if language == "EN":
            return 'List of active orders'
    else:
        if language == "RU":
            return 'Активных заказов нет ;('
        if language == "EN":
            return 'No active orders'


def adminSliderOrderActive(page, active, language):


    if len(active) != 0:

        paginator = adminSliderOrderPaginator(
            page_count=len(active),
            current_page=page,
            data_pattern='adminActiveOrder#{page}'
        )

        paginator.current_page_label = '· {} ·'

        adminLookActive = types.InlineKeyboardButton("№{} | {} BATH 🟡".format(str(active[page - 1].id),
                                                                              str(active[page - 1].fullprice)),
                                                     callback_data="adminLookActive#{}".format(page - 1))
        paginator.add_before(adminLookActive)
        toBackButton =""
        if language == "RU":
            toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='adminOrders')
        if language == "EN":
            toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='adminOrders')
        paginator.add_after(toBackButton)

        return paginator.markup

    else:
        backingMenu = types.InlineKeyboardMarkup(row_width=1)

        backingButton = ""
        if language == "RU":
            backingButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='adminOrders')
        if language == "EN":
            backingButton = types.InlineKeyboardButton('Back ⬅️', callback_data='adminOrders')
        return backingMenu.add(backingButton)



def adminActiveInfoText(activeOrders: list, choosedOrder: int, language):

    order = activeOrders[choosedOrder]
    customer = db.getCustomer(order.customer_id)
    if language == "RU":
        head = f"Заказ №{order.id}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Покупатель: @{customer.username}\n\n'
        head += f'Язык: {customer.language}\n\n'
        head += 'Товары:\n'
        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} грамм - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nИтого: {order.fullprice} BATH"
        head += f"\n\nДата и время заказа: {order.datetime}"
        head += f"\n\nСпособ оплаты: {order.methodpay}"
        head += f"\n\nАдрес для заказа: {order.address}"
        head += f"\n\nКомментарий к адресу: " \
                f"{order.comment if order.comment is not None else 'не указан'}"
        if order.status.split('#')[0] == "Передано на доставку":
            head += f"\n\nСтатус заказа: {order.status.split('#')[0]}"
            if order.status.split('#')[1] != "":
                head += f"\nОриентировное время доставки:\n{order.status.split('#')[1]}"
        else:
            head += f"\n\nСтатус заказа: {order.status}"
        return head
    if language == "EN":
        head = f"Order №{order.id}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Customer: @{customer.username}\n\n'
        head += f'Language: {customer.language}\n\n'
        head += 'Items:\n'
        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} gram - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nTotal: {order.fullprice} BATH"
        head += f"\n\nDate and time of order: {order.datetime}"
        if order.methodpay == "наличные":
            head += f"\n\nPayment: cash"
        head += f"\n\nAddress for delivery: {order.address}"
        head += f"\n\nComment for address: " \
                f'{order.comment if order.comment is not None else "did not point"}'
        if order.status.split('#')[0] == "Передано на доставку":
            head += f"\n\nStatus order: sent for delivery"
            if order.status.split('#')[1] != "":
                head += f"\nEstimated delivery time:\n{order.status.split('#')[1]}"
        else:
            head += "\n\nStatus order: waiting for courier"
        return head

def adminActiveInfoMenu(activeOrders: list, choosedOrder: int, language):
    order = activeOrders[choosedOrder]
    activeMenu = types.InlineKeyboardMarkup(row_width=1)
    if language == "RU":
        button1 = types.InlineKeyboardButton("Написать покупателю",
                                             callback_data=f"messageToCustomer#{order.customer_id}#{order.id}#{choosedOrder}")

        button3 = types.InlineKeyboardButton("Отменить заказ",
                                             callback_data=f"refusingActive#{order.id}#{choosedOrder}")

        button4 = types.InlineKeyboardButton("Завершить заказ",
                                             callback_data=f"completingActive#{order.id}")

        button5 = types.InlineKeyboardButton("Назад ⬅️", callback_data="activeList")

        activeMenu.add(button1)

        if order.status == "ожидает курьера":
            activeMenu.add(types.InlineKeyboardButton("Обновить статус-принять к доставке",
                                             callback_data=f"acceptingActive#{order.id}#{choosedOrder}"))

        activeMenu.add(button3, button4, button5)

        return activeMenu
    if language == "EN":
        button1 = types.InlineKeyboardButton("Write to customer",
                                           callback_data=f"messageToCustomer#{order.customer_id}#{order.id}#{choosedOrder}")

        button3 = types.InlineKeyboardButton("Cancel order",
                                             callback_data=f"refusingActive#{order.id}#{choosedOrder}")

        button4 = types.InlineKeyboardButton("Complete order",
                                             callback_data=f"completingActive#{order.id}")

        button5 = types.InlineKeyboardButton("Back ⬅️", callback_data="activeList")

        activeMenu.add(button1)

        if order.status == "ожидает курьера":
            activeMenu.add(types.InlineKeyboardButton("Update Status - accept for delivery",
                                                      callback_data=f"acceptingActive#{order.id}#{choosedOrder}"))

        activeMenu.add(button3, button4, button5)
        return activeMenu
def switchStatusText(language):
    if language == "RU":
        return "Статус заказа успешно обновлен\nПокупатель получил уведомление"
    if language == "EN":
        return "Order status updated successfully\nCustomer received notification"
def switchActiveToCompleteText(id: int, language):
    if language == "RU":
        return f"Заказ №{id} успешно завершен"
    if language == "EN":
        return f"Order №{id} completed successfully"

def switchActiveToCompleteMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад ⬅️", callback_data="activeList"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Back ⬅️", callback_data="activeList"))
def switchActiveToRefusalText(languageAdmin, languageCustomer):
    if languageAdmin == "RU":
        return f"Введите причину отмены или вернитесь назад!\nРекомендуется использовать язык: {languageCustomer}"
    if languageAdmin == "EN":
        return f"Enter a reason for canceling or go back!\nRecommended to use the language: {languageCustomer}"
def switchActiveToRefusalMenu(page: int, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад ⬅️", callback_data=f"activeToRefusalCancel#{page}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Back ⬅️", callback_data=f"activeToRefusalCancel#{page}"))

def infoActiveToRefusalText(id: int, language):
    if language == "RU":
        return f"Заказ №{id} успешно отменён\nПокупатель получил уведомление"
    if language == "EN":
        return f"Order №{id} canceled successfully\nCustomer received notification"

def infoActiveToRefusalMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад ⬅️", callback_data="activeList"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Back ⬅️", callback_data="activeList"))

def toCommunicateWithCustomerText(id: int, language):
    if language == "RU":
        return f"Напишите сообщение для покупателя\nпо заказу №{id}\n" \
               f"Рекомендуется использовать язык: {db.getLanguage(ao.getActiveOrder(id).customer_id)}"
    if language == "EN":
        return f"Write a message to the buyer\non order №{id}\n" \
               f"Recommended to use the language: {db.getLanguage(ao.getActiveOrder(id).customer_id)}"
def toCommunicateWithCustomerMenu(page: int, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад ⬅️",
                                                                       callback_data=f"adminCommunicateCancel#{page}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Back ⬅️",
                                                                       callback_data=f"adminCommunicateCancel#{page}"))

def answerNextSendToCustomerText(idOrder: int, language):
    if language == "RU":
        return f'Сообщение покупателю по заказу №{idOrder} успешно отправлено'
    if language == "EN":
        return f'Message to the buyer on order №{idOrder} successfully sent'
def answerNextSendToCustomerMenu(page: int, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад ⬅️", callback_data=f"adminLookActive#{page}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Back ⬅️", callback_data=f"adminLookActive#{page}"))

def sendingToCustomerText(idOrder, text, language):
    if language == "RU":
        return f"Вам сообщение от продавца по заказу №{idOrder}:\n" + text
    if language == "EN":
        return f'You get message from seller on order №{idOrder}:\n' + text
def sendingToCustomerMenu(idOrder, idAdmin, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().\
            add(types.InlineKeyboardButton("Ответить", callback_data=f"toAnswerToAdmin#{idAdmin}#{idOrder}"))
    if language == "EN":
        return types.InlineKeyboardMarkup(). \
            add(types.InlineKeyboardButton("To answer", callback_data=f"toAnswerToAdmin#{idAdmin}#{idOrder}"))

def toAnswerToAdminText(language):
    if language == "RU":
        return 'Напиши сообщение:'
    if language == "EN":
        return 'Write a message:'
def toAnswerToAdminMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Отменить ❌", callback_data="answerToAdminCancel"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Cancel ❌", callback_data="answerToAdminCancel"))
def feedbackToCustomerAfterSendAdminText(language):
    if language == "RU":
        return "Сообщение успешно отправлено"
    if language == "EN":
        return "Message has sent successfully"

def sendingToAdminText(idOrder, text, language):
    if language == "RU":
        return f'Поступило сообщение от покупателя по заказу №{idOrder}:\n' + text
    if language == "EN":
        return f'Received a message from a customer on an order №{idOrder}:\n' + text


def sendingToAdminMenu(idOrder, idCustomer, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().\
            add(types.InlineKeyboardButton("Ответить", callback_data=f"messageToCustomer#{idCustomer}#{idOrder}"))
    if language == "EN":
        return types.InlineKeyboardMarkup(). \
            add(types.InlineKeyboardButton("Answer", callback_data=f"messageToCustomer#{idCustomer}#{idOrder}"))

def toAnswerToCustomerMenu(page: int, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Посмотреть его заказ",
                                                                           callback_data=f"adminCommunicateCancel#{page}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("View his order",
                                                                           callback_data=f"adminCommunicateCancel#{page}"))
def AdminTextOrderRefusal(active, language):
    if len(active) != 0:
        if language == "RU":
            return 'Список отменённых заказов:'
        if language == "EN":
            return 'List of canceled orders'
    else:
        if language == "RU":
            return 'Отменённых заказов нет ;('
        if language == "EN":
            return 'No canceled orders'
def adminSliderOrderRefusal(page, refusal, language):

    if len(refusal) != 0:

        paginator = adminSliderOrderPaginator(
            page_count=len(refusal),
            current_page=page,
            data_pattern='adminRefusalOrder#{page}'
        )

        paginator.current_page_label = '· {} ·'

        adminLookActive = types.InlineKeyboardButton("№{} | {} BATH 🔴".format(str(refusal[page - 1].id_from_active),
                                                                              str(refusal[page - 1].fullprice)),
                                                     callback_data="adminLookRefusal#{}".format(page - 1))
        paginator.add_before(adminLookActive)

        toBackButton = ""
        if language == "RU":
            toBackButton = types.InlineKeyboardButton('Назад ⬅️', callback_data='adminOrders')
        if language == "EN":
            toBackButton = types.InlineKeyboardButton('Back ⬅️', callback_data='adminOrders')
        paginator.add_after(toBackButton)

        return paginator.markup

    else:
        backingMenu = types.InlineKeyboardMarkup(row_width=1)

        if language == "RU":
            backingButton = types.InlineKeyboardButton("Назад ⬅️", callback_data="adminOrders")
            return backingMenu.add(backingButton)
        if language == "EN":
            backingButton = types.InlineKeyboardButton("Back ⬅️", callback_data="adminOrders")
            return backingMenu.add(backingButton)


def adminRefusalInfoText(refusalOrders: list, choosedOrder: int, language):

    order = refusalOrders[choosedOrder]

    customer = db.getCustomer(order.customer_id)
    if language == "RU":
        head = f"Заказ №{order.id_from_active}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Покупатель: @{customer.username}\n\n'
        head += f'Язык: {customer.language}\n\n'
        head += 'Товары:\n'

        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} грамм - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nИтого: {order.fullprice} BATH"
        head += f"\n\nДата и время заказа: {order.datetime}"
        head += f"\n\nДата и время отказа: {order.datetime_refuse}"
        head += f"\n\nСпособ оплаты: {order.methodpay}"
        head += f"\n\nАдрес для заказа: {order.address}"
        head += f"\n\nКомментарий к адресу: " \
                f"{order.comment if order.comment is not None else 'не указан'}"
        head += f"\n\nПричина отказа: {order.reason}"
        return head
    if language == "EN":
        head = f"Order №{order.id_from_active}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Customer: @{customer.username}\n\n'
        head += f'Language: {customer.language}\n\n'
        head += 'Items:\n'

        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} gram - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nTotal: {order.fullprice} BATH"
        head += f"\n\nDate and time of order: {order.datetime}"
        head += f"\n\nDate and time of canceling: {order.datetime_refuse}"
        if order.methodpay == "наличные":
            head += f"\n\nPayment: cash"
        head += f"\n\nAddress for order: {order.address}"
        head += f"\n\nCommet for address: " \
                f"{order.comment if order.comment is not None else 'did not point'}"
        head += f"\n\nReason of canceling: {order.reason}"
        return head

def adminRefusalInfoMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Назад ⬅️", callback_data="refusalList"))
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Back ⬅️", callback_data="refusalList"))

def AdminTextOrderComplete(complete: list, language):
    if len(complete) != 0:
        if language == "RU":
            return 'Список завершенных заказов:'
        if language == "EN":
            return 'List of completed orders:'
    else:
        if language == "RU":
            return 'Завершенных заказов нет!'
        if language == "EN":
            return 'No completed orders!'
def adminSliderOrderComplete(page, complete, language):

    if len(complete) != 0:

        paginator = adminSliderOrderPaginator(
            page_count=len(complete),
            current_page=page,
            data_pattern='adminCompleteOrder#{page}'
        )

        paginator.current_page_label = '· {} ·'

        adminLookActive = types.InlineKeyboardButton("№{} | {} BATH 🟢".format(str(complete[page - 1].id_from_active),
                                                                              str(complete[page - 1].fullprice)),
                                                     callback_data="adminLookComplete#{}".format(page - 1))
        paginator.add_before(adminLookActive)
        toBackButton = ""
        if language == "RU":
            toBackButton = types.InlineKeyboardButton('Назад', callback_data='adminOrders')
        if language == "EN":
            toBackButton = types.InlineKeyboardButton('Back', callback_data='adminOrders')
        paginator.add_after(toBackButton)

        return paginator.markup

    else:
        backingMenu = types.InlineKeyboardMarkup(row_width=1)
        if language == "RU":
            backingButton = types.InlineKeyboardButton("Назад", callback_data="adminOrders")
            return backingMenu.add(backingButton)
        if language == "EN":
            backingButton = types.InlineKeyboardButton("Back", callback_data="adminOrders")
            return backingMenu.add(backingButton)


def adminCompleteInfoText(completeOrders: list, choosedOrder: int, language):

    order = completeOrders[choosedOrder]

    customer = db.getCustomer(order.customer_id)
    if language == "RU":
        head = f"Заказ №{order.id_from_active}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Покупатель: @{customer.username}\n\n'
        head += f'Язык: {customer.language}\n\n'
        head += 'Товары:\n'

        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} грамм - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nИтого: {order.fullprice} BATH"
        head += f"\n\nДата и время заказа: {order.datetime}"
        head += f"\n\nДата и время завершения: {order.datetime_complete}"
        head += f"\n\nСпособ оплаты: {order.methodpay}"
        head += f"\n\nАдрес для заказа: {order.address}"
        head += f"\n\nКомментарий к адресу: " \
                f"{order.comment if order.comment is not None else 'не указан'}"
        return head
    if language == "EN":
        head = f"Order №{order.id_from_active}\n\n"
        if db.getCustomer(order.customer_id).username is not None:
            head += f'Customer: @{customer.username}\n\n'
        head += f'Language: {customer.language}\n\n'
        head += 'Items:\n'

        items = order.items

        for item in items[:-1].split(','):
            head += "{} - {} gram - {} BATH\n".format(
                item.split('#')[0],
                item.split('#')[1],
                int(item.split('#')[1]) * int(item.split('#')[2])
            )

        head += f"\n\nTotal: {order.fullprice} BATH"
        head += f"\n\nDate and time of order: {order.datetime}"
        head += f"\n\nDate and time of completed: {order.datetime_complete}"
        if order.methodpay == "наличные":
            head += f"\n\nPayment: cash"
        head += f"\n\nAddress of order: {order.address}"
        head += f"\n\nComment for address: " \
                f"{order.comment if order.comment is not None else 'did not point'}"
        return head
def adminCompleteInfoMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton("Назад", callback_data="completeList"))
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton("Back", callback_data="completeList"))

def showNewActiveOrderText(idOrder, language):
    if language == "RU":
        return f'Поступил новый заказ №{idOrder}'
    if language == "EN":
        return f'New order №{idOrder}'
def showNewActiveOrderMenu(page: int, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Посмотреть заказ",
                                                                       callback_data=f"adminCommunicateCancel#{page}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("View order",
                                                                           callback_data=f"adminCommunicateCancel#{page}"))
def infoReason(idOrder, text, language):
    if language == "RU":
        return f"Продавец отменил заказ №{idOrder}\nПричина: {text}"
    elif language == "EN":
        return f'Seller has refused order №{idOrder}\nReason: {text}'
def infoAccept(idOrder, language):
    if language == "RU":
        return f'Заказ №{idOrder} принят в доставку'

    elif language == "EN":
        return f'Order №{idOrder} was sent for delivery'

def infoAcceptWithTime(order, language):
    print(order.status)
    if language == "RU":
        return f'Заказ №{order.id} принят в доставку\nОриентировочное время доставки: {order.status.split("#")[1]}'

    elif language == "EN":
        return f'Order №{order.id} was sent for delivery\nEstimated delivery time: {order.status.split("#")[1]}'

def adminBeforePostTextRU(language):
    if language == "RU":
        return "Введите текст поста на русском языке (до 450 символов):"
    if language == "EN":
        return "Enter the text of the post in Russian (up to 450 characters):"

def adminBeforePostTextEN(language):
    if language == "RU":
        return "Введите текст поста на английском языке (до 450 символов):"
    if language == "EN":
        return "Enter the text of the post in English (up to 450 characters):"

def warningPostText(language, length):
    if language == "RU":
        return f"Максимальная длина сообщения 450 символов: вы ввели {length}"
    if language == "EN":
        return f"Maximum message length is 450 characters: you entered {length}"

def warningProductText(language, length):
    if language == "RU":
        return f"Максимальная длина описания 900 символов: вы ввели {length}"
    if language == "EN":
        return f"Maximum description length is 900 characters: you entered {length}"

def warningPostMenuRU(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data="wrongLengthPost#RU"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetPost")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data="wrongLengthPost#RU"),
            types.InlineKeyboardButton("Reset", callback_data="resetPost")
        )
def warningPostMenuEN(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data="wrongLengthPost#EN"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetPost")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data="wrongLengthPost#EN"),
            types.InlineKeyboardButton("Reset", callback_data="resetPost")
        )
def adminBeforePostMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Сбросить", callback_data="resetPost"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Reset", callback_data="resetPost"))
def adminGetTypePostText(textRU, textEN, language):
    if language == "RU":
        return f"Текст для русских пользователей:\n{textRU}" \
               f"\n\nТекст на англоязычных пользователей:\n{textEN}\n\nВыберите вложение для поста"
    if language == "EN":
        return f"Text for russian customers:\n{textRU}" \
               f"\n\nText for english customer:\n{textEN}\n\nChoose an attachment for a post"
def adminGetTypePostMenu(language):
    menu = types.InlineKeyboardMarkup(row_width=1)
    if language == "RU":
        b1 = types.InlineKeyboardButton("Видео", callback_data=f"attachVideo")
        b2 = types.InlineKeyboardButton("Фото", callback_data=f"attachPhoto")
        b3 = types.InlineKeyboardButton("Без вложения", callback_data=f"noAttach")
        b4 = types.InlineKeyboardButton("Сбросить", callback_data="resetPost")
        return menu.add(b1, b2, b3, b4)
    if language == "EN":
        b1 = types.InlineKeyboardButton("Video", callback_data=f"attachVideo")
        b2 = types.InlineKeyboardButton("Photo", callback_data=f"attachPhoto")
        b3 = types.InlineKeyboardButton("No attachment", callback_data=f"noAttach")
        b4 = types.InlineKeyboardButton("Reset", callback_data="resetPost")
        return menu.add(b1, b2, b3, b4)
def adminPostToAttachPhoto(language):
    if language == "RU":
        return 'Прикрепите и отправьте фото:'
    if language == "EN":
        return 'Attach and send a photo:'

def adminPostToAttachVideo(language):
    if language == "RU":
        return f'Прикрепите видео в формате mp4:'
    if language == "EN":
        return f'Attach video in mp4 format:'
def adminFinalPostText(textRU, textEN, language):
    if language == "RU":
        return f"Текст для русских пользователей:\n{textRU}\n\nТекст на англоязычных пользователей:\n{textEN}"
    if language == "EN":
        return f"Text for russian customers:\n{textRU}\n\nText for english customers:\n{textEN}"

def adminFinalPostMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Опубликовать", callback_data="adminToPublishPost"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetPost")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Publish", callback_data="adminToPublishPost"),
            types.InlineKeyboardButton("Reset", callback_data="resetPost")
        )

def adminListProductText(products, language):
    if len(products) != 0:
        if language == "RU":
            return 'Выберите товар для просмотра или удаления'
        if language == "EN":
            return 'Select an item to view or delete'
    else:
        if language == "RU":
            return 'Сейчас товаров нет в магазине'
        if language == "EN":
            return "No items in the shop"

def adminSliderShop(page, products, language):
    if len(products) != 0:

        nameOfProducts = list(i.name for i in products)
        idOrders = list(i.id for i in products)
        paginator = sliderShopPaginator(page_count=len(products),
                                        current_page=page,
                                        data_pattern='adminListProduct#{page}')

        lookProduct = types.InlineKeyboardButton('{}'.format(nameOfProducts[page - 1]),
                                                 callback_data='adminProductName#{}'.format(idOrders[page - 1]))
        paginator.add_before(lookProduct)


        if language == "RU":
            toAddProduct = types.InlineKeyboardButton('Добавить товар', callback_data='adminAddProduct')

            toBackButton = types.InlineKeyboardButton('Назад', callback_data='toMainAdmin')
            paginator.add_after(toBackButton, toAddProduct)

        if language == "EN":
            toAddProduct = types.InlineKeyboardButton('Add item', callback_data='adminAddProduct')

            toBackButton = types.InlineKeyboardButton('Back', callback_data='toMainAdmin')
            paginator.add_after(toBackButton, toAddProduct)

        return paginator.markup

    else:
        if language == "RU":
            return types.InlineKeyboardMarkup(row_width=1).add(
                types.InlineKeyboardButton('Добавить товар', callback_data='adminAddProduct'),
                types.InlineKeyboardButton("Назад", callback_data="toMainAdmin")
            )
        if language == "EN":
            return types.InlineKeyboardMarkup(row_width=1).add(
                types.InlineKeyboardButton('Add item', callback_data='adminAddProduct'),
                types.InlineKeyboardButton("Back", callback_data="toMainAdmin")
            )


def adminTextProduct(product, language, pageOfLanguage):
    if language == "RU":
        if pageOfLanguage == 1:
            return f'''ВЗГЛЯДОМ RU ПОЛЬЗОВАТЕЛЯ:\n
        
{product.name}

{product.infoAbout.split('#')[0]}

Доставка по всему острову
1 грамм - {product.price} BATH
'''
        if pageOfLanguage == 2:
            return f'''ВЗГЛЯДОМ EN ПОЛЬЗОВАТЕЛЯ:\n

{product.name}

{product.infoAbout.split('#')[1]}

Delivery on the whole Island
1 gram - {product.price} BATH'''

    if language == "EN":
        if pageOfLanguage == 1:
            return f'''RU USER'S VIEW:\n
        
{product.name}

{product.infoAbout.split('#')[0]}

Доставка по всему острову
1 грамм - {product.price} BATH
'''
        if pageOfLanguage == 2:
            return f'''EN USER'S VIEW:\n

{product.name}

{product.infoAbout.split('#')[1]}

Delivery on the whole Island
1 gram - {product.price} BATH'''

def adminProductMenu1(idOrder, language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Изменить язык просмотра", callback_data=f"changePageLanguageTo2#{idOrder}"),
            types.InlineKeyboardButton("Изменить название", callback_data=f"adminChangeName#{idOrder}"),
            types.InlineKeyboardButton("Изменить RU описание", callback_data=f"adminChangeInfoAboutRU#{idOrder}"),
            types.InlineKeyboardButton("Изменить EN описание", callback_data=f"adminChangeInfoAboutEN#{idOrder}"),
            types.InlineKeyboardButton("Изменить цену", callback_data=f"adminChangePrice#{idOrder}"),
            types.InlineKeyboardButton("Изменить медиа", callback_data=f"adminChangeMedia#{idOrder}"),
            types.InlineKeyboardButton("Удалить товар", callback_data=f"adminDeleteProduct#{idOrder}"),
            types.InlineKeyboardButton("Назад", callback_data="adminCatalogFromMedia")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Change language view", callback_data=f"changePageLanguageTo2#{idOrder}"),
            types.InlineKeyboardButton("Change name", callback_data=f"adminChangeName#{idOrder}"),
            types.InlineKeyboardButton("Change RU text", callback_data=f"adminChangeInfoAboutRU#{idOrder}"),
            types.InlineKeyboardButton("Change EN text", callback_data=f"adminChangeInfoAboutEN#{idOrder}"),
            types.InlineKeyboardButton("Change price", callback_data=f"adminChangePrice#{idOrder}"),
            types.InlineKeyboardButton("Change media", callback_data=f"adminChangeMedia#{idOrder}"),
            types.InlineKeyboardButton("Delete item", callback_data=f"adminDeleteProduct#{idOrder}"),
            types.InlineKeyboardButton("Back", callback_data="adminCatalogFromMedia")
        )
def adminProductMenu2(idOrder, language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Изменить язык просмотра", callback_data=f"changePageLanguageTo1#{idOrder}"),
            types.InlineKeyboardButton("Изменить название", callback_data=f"adminChangeName#{idOrder}"),
            types.InlineKeyboardButton("Изменить RU описание", callback_data=f"adminChangeInfoAboutRU#{idOrder}"),
            types.InlineKeyboardButton("Изменить EN описание", callback_data=f"adminChangeInfoAboutEN#{idOrder}"),
            types.InlineKeyboardButton("Изменить цену", callback_data=f"adminChangePrice#{idOrder}"),
            types.InlineKeyboardButton("Изменить медиа", callback_data=f"adminChangeMedia#{idOrder}"),
            types.InlineKeyboardButton("Удалить товар", callback_data=f"adminDeleteProduct#{idOrder}"),
            types.InlineKeyboardButton("Назад", callback_data="adminCatalogFromMedia")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Change language view", callback_data=f"changePageLanguageTo1#{idOrder}"),
            types.InlineKeyboardButton("Change name", callback_data=f"adminChangeName#{idOrder}"),
            types.InlineKeyboardButton("Change RU text", callback_data=f"adminChangeInfoAboutRU#{idOrder}"),
            types.InlineKeyboardButton("Change EN text", callback_data=f"adminChangeInfoAboutEN#{idOrder}"),
            types.InlineKeyboardButton("Change price", callback_data=f"adminChangePrice#{idOrder}"),
            types.InlineKeyboardButton("Change media", callback_data=f"adminChangeMedia#{idOrder}"),
            types.InlineKeyboardButton("Delete item", callback_data=f"adminDeleteProduct#{idOrder}"),
            types.InlineKeyboardButton("Back", callback_data="adminCatalogFromMedia")
        )
def changeMediaText(language):
    if language == "RU":
        return "Выберите вложение"
    if language == "EN":
        return "Choose attachment"
def changeMediaMenu(language, idProduct):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Фото", callback_data=f"changeMediaToPhoto#{idProduct}"),
            types.InlineKeyboardButton("Видео", callback_data=f"changeMediaToVideo#{idProduct}"),
            types.InlineKeyboardButton("Назад", callback_data=f"resetChanging#{idProduct}")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Photo", callback_data=f"changeMediaToPhoto#{idProduct}"),
            types.InlineKeyboardButton("Video", callback_data=f"changeMediaToVideo#{idProduct}"),
            types.InlineKeyboardButton("Back", callback_data=f"resetChanging#{idProduct}")
        )
def delProductText(language):
    if language == "RU":
        return "Товар удален из магазина"
    if language == "EN":
        return "Item was deleted from shop"

def adminAddProductName(language):
    if language == "RU":
        return 'Введите название товара\n(Кратко, чтобы вместилось в кнопку)'
    if language == "EN":
        return 'Enter product name\n(Short to fit in button)'
def adminAddProductNameMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Сбросить", callback_data="resetProduct"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Reset", callback_data="resetProduct"))
def adminAddProductTextRU(language):
    if language == "RU":
        return 'Введите описание товара на русском (не более 900 символов):'
    if language == "EN":
        return 'Enter product description in Russian (no more than 900 characters)'

def adminAddProductTextEN(language):
    if language == "RU":
        return 'Введите описание товара на английском (не более 900 символов):'
    if language == "EN":
        return 'Enter product description in English (no more than 900 characters)'

def adminAddProductPrice(language):
    if language == "RU":
        return 'Введите цену за 1 грамм в валюте BATH:'
    if language == "EN":
        return 'Enter the price for 1 gram in BATH currency'
def adminAddProductMediaText(product, language):
    if language == "RU":
        return f'''ВЗГЛЯДОМ RU ПОЛЬЗОВАТЕЛЯ:\n
        
{product.name}

{product.infoAbout.split('#')[0]}

Доставка по всему острову
1 грамм - {product.price} BATH


ВЗГЛЯДОМ EN ПОЛЬЗОВАТЕЛЯ:\n

{product.name}

{product.infoAbout.split('#')[1]}

Delivery on the whole Island
1 gram - {product.price} BATH
'''
    if language == "EN":
        return f'''RU USER'S VIEW:\n
        
{product.name}

{product.infoAbout.split('#')[0]}

Доставка по всему острову
1 грамм - {product.price} BATH


EN USER'S VIEW:\n

{product.name}

{product.infoAbout.split('#')[1]}

Delivery on the whole Island
1 gram - {product.price} BATH


Choose attachment type:'''


def adminAddProductMediaMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Видео", callback_data=f"attachVideoToProduct"),
            types.InlineKeyboardButton("Фото", callback_data=f"attachPhotoToProduct"),
            # types.InlineKeyboardButton("Несколько медиа", callback_data=f"attachMediaGroupToProduct"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Video", callback_data=f"attachVideoToProduct"),
            types.InlineKeyboardButton("Photo", callback_data=f"attachPhotoToProduct"),
            # types.InlineKeyboardButton("Media group", callback_data=f"attachMediaGroupToProduct"),
            types.InlineKeyboardButton("Reset", callback_data="resetProduct")
        )
def adminFinalProductMenu1(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Изменить язык просмотра", callback_data="switchViewNewItemToPageOfLanguageTo2"),
            types.InlineKeyboardButton("Добавить в начало", callback_data="addProductInStart"),
            types.InlineKeyboardButton("Добавить в конец", callback_data="addProductInFinish"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Change language view", callback_data="switchViewNewItemToPageOfLanguageTo2"),
            types.InlineKeyboardButton("Add to start", callback_data="addProductInStart"),
            types.InlineKeyboardButton("Add to end", callback_data="addProductInFinish"),
            types.InlineKeyboardButton("Reset", callback_data="resetProduct")
        )
def adminFinalProductMenu2(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Изменить язык просмотра", callback_data="switchViewNewItemToPageOfLanguageTo1"),
            types.InlineKeyboardButton("Добавить в начало", callback_data="addProductInStart"),
            types.InlineKeyboardButton("Добавить в конец", callback_data="addProductInFinish"),
            types.InlineKeyboardButton("Сбросить", callback_data="resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Change language view", callback_data="switchViewNewItemToPageOfLanguageTo1"),
            types.InlineKeyboardButton("Add to start", callback_data="addProductInStart"),
            types.InlineKeyboardButton("Add to end", callback_data="addProductInFinish"),
            types.InlineKeyboardButton("Reset", callback_data="resetProduct")
        )

def feedbackAdminNewPost(language):
    if language == "RU":
        return "Товар добавлен в магазин\nПользователи получили уведомления"
    if language == "EN":
        return "Item added to shop\nCustomers received notifications"
def feedbackNewPost(language):
    if language == "RU":
        return "Загляни в магазин!\nТам кое что новенькое и интересное"
    elif language == "EN":
        return "Look to shop\nThere is something new and interesting"


def adminChangeMenu(idProduct, language):
    if language == "RU":
        return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Назад", callback_data=f"resetChanging#{idProduct}"))
    if language == "EN":
        return types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("Back", callback_data=f"resetChanging#{idProduct}"))

def adminSwitcherLanguageText(language):
    if language == "RU":
        return "Выберите язык"
    if language == "EN":
        return "Choose language"
def adminSwitcherLanguageMenu():
    switchLanguageProfile = types.InlineKeyboardMarkup(row_width=1)
    languageProfileEN = types.InlineKeyboardButton("English", callback_data="adminToEnLanguage")
    languageProfileRU = types.InlineKeyboardButton("Русский", callback_data="adminToRuLanguage")
    return switchLanguageProfile.add(languageProfileEN, languageProfileRU)


# def adminTextMediaGroupToProduct(language):
#     if language == "RU":
#         return "ПО ОДНОМУ отправляйте фото/видео в формате png,jpg/mp4 (от 2 до 10 в сумме)"
#     if language == "EN":
#         return "Send photos/videos in png,jpg/mp4 format ONE BY ONE (from 2 to 10 in total)"
#
# def adminMenuMediaGroupToProduct(language):
#     if language == "RU":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Сбросить", callback_data="resetProduct")
#         )
#     if language == "EN":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Reset", callback_data="resetProduct")
#         )
#
# def videoHadUploaded(countMedia, language):
#     if language == "RU":
#         return f'Видео было добавлено\nДобавлено {countMedia} из 10 возможных вложений'
#     if language == "EN":
#         return f'Video has uploaded\nAdded {countMedia} out of 10 possible attachments'
#
# def photoHasUploaded(countMedia, language):
#     if language == "RU":
#         return f'Фото было добавлено\nДобавлено {countMedia} из 10 возможных вложений'
#     if language == "EN":
#         return f'Photo has uploaded\nAdded {countMedia} out of 10 possible attachments'
#
# def askToAddMoreMediaMenu(countMedia, language):
#     if language == "RU":
#         menu = types.InlineKeyboardMarkup(row_width=1)
#         if countMedia >= 2:
#             menu.add(types.InlineKeyboardButton("Завершить прикрепление", callback_data="finishAttachment"))
#         menu.add(types.InlineKeyboardButton("Сбросить", callback_data="resetProduct"))
#         return menu
#     if language == "EN":
#         menu = types.InlineKeyboardMarkup(row_width=1)
#         if countMedia >= 2:
#             menu.add(types.InlineKeyboardButton("Finish attaching", callback_data="finishAttachment"))
#         menu.add(types.InlineKeyboardButton("Reset", callback_data="resetProduct"))
#         return menu

def warningOverflowCaption(language, lenght: int):
    if language == "RU":
        return f'Максимальное количество символов 1024\nС таким описанием товар будет иметь {lenght}'
    if language == "EN":
        return f'The maximum number of characters is 1024\nWith this description, the product will have {lenght}'

# def warningOverflowCaptionMenu(language, idProduct):
#     if language == "RU":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminChangeInfoAbout#{idProduct}"),
#             types.InlineKeyboardButton("Назад", callback_data=f"resetChanging#{idProduct}")
#         )
#     if language == "EN":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Try again", callback_data=f"adminChangeInfoAbout#{idProduct}"),
#             types.InlineKeyboardButton("Back", callback_data=f"resetChanging#{idProduct}")
#         )

def warningOverflowCaptionMenuRU(language, idProduct):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminChangeInfoAboutRU#{idProduct}"),
            types.InlineKeyboardButton("Назад", callback_data=f"resetChanging#{idProduct}")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data=f"adminChangeInfoAboutRU#{idProduct}"),
            types.InlineKeyboardButton("Back", callback_data=f"resetChanging#{idProduct}")
        )

def warningOverflowCaptionMenuEN(language, idProduct):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminChangeInfoAboutEN#{idProduct}"),
            types.InlineKeyboardButton("Назад", callback_data=f"resetChanging#{idProduct}")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data=f"adminChangeInfoAboutEN#{idProduct}"),
            types.InlineKeyboardButton("Back", callback_data=f"resetChanging#{idProduct}")
        )


# def warningOverflowCaptionForItemMenu(language):
#     if language == "RU":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminOverflowDescriptionNewItem"),
#             types.InlineKeyboardButton("Сбросить", callback_data=f"resetProduct")
#         )
#     if language == "EN":
#         return types.InlineKeyboardMarkup(row_width=1).add(
#             types.InlineKeyboardButton("Try again", callback_data=f"adminOverflowDescriptionNewItem"),
#             types.InlineKeyboardButton("Reset", callback_data=f"resetProduct")
#         )

def warningOverflowCaptionForProductMenu1(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminOverflowDescriptionNewProductRU"),
            types.InlineKeyboardButton("Сбросить", callback_data=f"resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data=f"adminOverflowDescriptionNewProductRU"),
            types.InlineKeyboardButton("Reset", callback_data=f"resetProduct")
        )

def warningOverflowCaptionForProductMenu2(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminOverflowDescriptionNewProductEN"),
            types.InlineKeyboardButton("Сбросить", callback_data=f"resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data=f"adminOverflowDescriptionNewProductEN"),
            types.InlineKeyboardButton("Reset", callback_data=f"resetProduct")
        )

def wrongDigitPriceText(language):
    if language == "RU":
        return 'Цена должна быть числом! (до 12345678)'
    if language == "EN":
        return 'Price must be a number! (up to 12345678)'
def wrongDigitPriceMenu(language):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Повторить попытку", callback_data=f"adminWrongDigitPrice"),
            types.InlineKeyboardButton("Сбросить", callback_data=f"resetProduct")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Try again", callback_data=f"adminWrongDigitPrice"),
            types.InlineKeyboardButton("Reset", callback_data=f"resetProduct")
        )

def errorAddressText(language):
    if language == "RU":
        return 'Ошибка поиска адреса\nПопробуйте снова или воспользуйтесь другим способом указания адреса'
    if language == "EN":
        return 'Error for search the address\nTry again or use another method of pointing address'

def exitAdminText(language):
    if language == "RU":
        return 'Теперь ты покупатель'
    if language == "EN":
        return 'You are customer now'

def enterEstimatedDeliveryTimeText(language):
    if language == "RU":
        return 'Введите ориентировочное время доставки\nНапример 19:00 или 16:00-17:30'
    if language == "EN":
        return "Enter estimated delivery time\nFor example 19:00 or 16:00-17:30"

def enterEstimatedDeliveryTimeMenu(language, idOrder):
    if language == "RU":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Пропустить", callback_data=f"skipEstimatedTime#{idOrder}")
        )
    if language == "EN":
        return types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton("Skip", callback_data=f"skipEstimatedTime#{idOrder}")
        )