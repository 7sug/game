import time
import random
import os
from colorama import init, Fore, Back
init()
comandlist = ('я', 'инвентарь', 'счет')
items = ('Старая книга', 'Золотые монеты', 'Ржавый меч')

def helper(a):
    count = 0
    while count < 1:
        if a == 'я':
            count += 1
            hero1.commands(a)
        elif a == 'инвентарь':
            count += 1
            hero1.commands(a)
        elif a == 'счет':
            count += 1
            hero1.commands(a)
        else:
            break

        if count == 1:
            count -= 1
            a = str(input('Что-нибудь еще?(введите команду): '))

class Hero():
    def __init__(self, name):
        global families
        global bodies
        global inventory
        global loc

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.money = 0
        self.deadmonster = 0
        self.firsttimefountain = 0
        self.shopfirsttime = 0
        self.deadboss = 0
        locs = ['Старый дом', 'Развилка', 'Деревня', 'Заброшенное поместье']
        inventory = []
        bodies = ('Обычный', 'Глаз', 'Рука', 'Нога', 'Обычный', 'Дух', 'Обычный', 'Магия', 'Обычный')
        families = ('Независимое содружество стихий', 'Вандергоф', 'Ваттерхил', 'Айсбраун')
        self.name = name
        self.family = random.choice(families)
        self.body = random.choice(bodies)
        self.health = 100
        if self.family == 'Независимое содружество стихий':
            self.health = 100
            self.power = 10
            self.speed = 150
            self.lucky = 110
            self.aliluja = 50
            self.magic = 20
        elif self.family == 'Вандергоф':
            self.health = 150
            self.power = 30
            self.speed = 50
            self.lucky = 50
            self.aliluja = 10
            self.magic = 10
        elif self.family == 'Ваттерхил':
            self.health = 100
            self.power = 20
            self.speed = 120
            self.lucky = 90
            self.aliluja = 70
            self.magic = 15
        else:
            self.health = 80
            self.power = 15
            self.speed = 100
            self.lucky = 70
            self.aliluja = 60
            self.magic = 30
        if self.body == 'Глаз':
            self.health -= 10
            self.power -= 10
            self.power -= 10
            self.speed -= 10
            self.lucky += 20
            self.aliluja += 40
            self.magic += 40
        elif self.body == 'Рука':
            self.power = self.power/2
            self.aliluja = self.aliluja*2
        elif self.body == 'Нога':
            self.speed = self.speed/2
            self.power = self.power*2
        elif self.body == 'Магия':
            self.magic += 50
            self.lucky += 10
            self.aliluja += 10
        elif self.body == 'Дух':
             self.aliluja += self.magic
             self.magic = 0
        self.healthConst = self.health

    def showing(self):
        print('Ваше имя: ' + str(self.name))
        print('Ваша семья: ' + str(self.family))
        print('Ваша особенность: ' + str(self.body))
        print('Ваше здоровье: ' + str(self.health))
        print('Ваша сила: ' + str(self.power))
        print('Ваша скорость: ' + str(self.speed))
        print('Ваша удача: ' + str(self.lucky))
        print('Ваш природный дар: ' + str(self.aliluja))
        print('Ваша магия: ' + str(self.magic))

    def HealthDown(self, damage):
        self.health -= damage

    def backpack(self):
        c = 0
        if len(inventory) == 0:
            print('Инвентарь пуст')
        else:
            print(inventory)
            while True:
                try:
                    vvod = str(input('Какой предмет осмотреть?("выход" для выхода) '))
                    if vvod == 'выход':
                        break
                    elif (vvod == 'старая книга') or (vvod =='Старая книга'):
                        os.startfile(os.getcwd()+'\\stripes\\старая книга.jpg')
                    elif (vvod == 'Письмо королю') or (vvod == 'письмо королю'):
                        os.startfile(os.getcwd()+'\\stripes\\письмо королю.jpg')
                    elif vvod == 'Зелье лечения' or vvod == 'зелье лечения':
                        ask = str(input('Оно восстановит вам 30 здоровья. Применить?' ))
                        if ask == 'да' or 'Да':
                            if self.health < self.healthConst:
                                self.health += 30
                                print('Ваше здоровье восстановленно!')
                            elif self.health > self.healthConst:
                                self.health = self.healthConst
                            elif self.heath == self.healthConst:
                                print('Ваше здоровье полное!')
                        else:
                            break
                    elif vvod == 'Голова чудовища' or vvod == 'голова чудовища':
                        print('Это голова монстра из подвала того поместья...')
                        print('Ее глаза все еще светятся, и кровь капает изо рта')

                    elif vvod == 'Голова минотавра' or vvod == 'голова минотавра':
                        print('Это ваш трофей за победу над боссом. Сомнительный приз, не так ли?')

                    else:
                        vvod = str(input('Этот предмет нельзя осмотреть. Нажмите ENTER для продолжения: '))
                        break
                    break
                except:
                    print('Ошибка ввода. Попробуйте снова: ')



    def showloc(self):
        print(loc)

    def oldHouse(self):
        os.system('cls')
        if self.count1 == 0:
            print('*Ты видишь перед собой стол*')
            time.sleep(0.5)
            print('*Подойдя к столу, ты увидел на нем 3 золотые монетки и старую книгу*')
            time.sleep(0.5)
            while True:
                try:
                    a3 = str(input('Хочешь взять эти предметы?(да/нет): '))
                    break
                except:
                    print('Ошибка ввода. Попробуйте снова: ')
            if a3 == 'да':
                vvod = str(input('Предметы добавлены в инвентарь! Нажмите ENTER для продолжения'))
                hero1.inventoryAdd(items[0])
                self.money += 3
                self.count1 += 1
            else:
                self.count1 = 0
        else:
            print('дом уже исследован!')


    def location(self, loc):
        newloc = loc

    def inventoryAdd(self, item):
        inventory.append(item)

    def showMoney(self):
        print(self.money)

    def commands(self, command):
        if command == 'я':
            hero1.showing()
        elif command == 'инвентарь':
            hero1.backpack()
        elif command == 'счет':
            hero1.showMoney()


    def penza(self):
        locs = ['магазин', 'оружейная', 'ферма']
        print(locs)
        ask2 = str(input('Куда дальше?? '))
        if ask2 == 'магазин':
            hero1.shop()
        elif ask2 == 'оружейная':
            hero1.guns()
        else:
            hero1.farm()


    def guns(self):
        global firstSwordPower
        global sekiraPower1
        global sekiraPower2
        global zeroWandPower1
        global zeroWandPower2
        global secondSwordPower
        global sasaikudasai
        sasaikudasaiValue = 150
        sasaikudasaiPower = 30
        firstSwordValue = 15
        firstSwordPower = 3
        sekiraValue = 350
        sekiraPower1 = 50
        sekiraPower2 = 20
        zeroWandValue = 300
        zeroWandPower1 = 30
        zeroWandPower2 = 30
        secondSwordValue = 25
        secondSwordPower = 5
        os.system('cls')
        weapons = ['Ржавый меч', 'Секира ужаса', 'Посох обнуления', 'Обычный меч', 'Сасай кудасай']
        print('Привет странник! Не желаешь купить что-нибудь?')
        print(weapons)
        while True:
            ask = str(input('Что-нибудь приглянулось? '))
            if ask == 'Ржавый меч' or ask == 'ржавый меч':
                print('Цена товара: ' + str(firstSwordValue))
                print('Сила: ' + str(firstSwordPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= firstSwordValue:
                        self.money -= firstSwordValue
                        inventory.append('Ржавый меч')
                        self.power += firstSwordPower
                        print('Оружие купленно!')
                    else:
                        print('Недостаточно денег')
            elif ask == 'Секира ужаса' or ask == 'секира ужаса':
                print('Цена товара: ' + str(sekiraValue))
                print('Сила: ' + str(sekiraPower1))
                print('Сила ужаса: ' + str(sekiraPower2))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= sekiraValue:
                        self.money -= sekiraValue
                        inventory.append('Секира ужаса')
                        self.power += 50
                        self.magic += 20
                        print('Оружие купленно!')
                    else:
                        print('Недостаточно денег')
            elif ask == 'Посох обнуления' or ask == 'посох обнуления':
                print('Цена товара: ' + str(zeroWandValue))
                print('Сила: ' + str(zeroWandPower1))
                print('Сила обнуления: ' + str(zeroWandPower2))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= zeroWandValue:
                        self.money -= zeroWandValue
                        inventory.append('Посох обнуления')
                        self.power += zeroWandPower1
                        self.magic += zeroWandPower2
                        print('Оружие купленно!')
                    else:
                        print('Недостаточно денег')
            elif ask == 'Обычный меч' or ask == 'обычный меч':
                print('Цена товара: ' + str(secondSwordValue))
                print('Сила: ' + str(secondSwordPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= secondSwordValue:
                        self.money -= secondSwordValue
                        inventory.append('Обычный меч')
                        self.power += secondSwordPower
                        print('Оружие купленно!')
                    else:
                        print('Недостаточно денег')
            elif ask == 'Сасай кудасай' or ask == 'сасай кудасай':
                print('Цена товара: ' + str(sasaikudasaiValue))
                print('Сила: '+ str(sasaikudasaiPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= sasaikudasaiValue:
                        self.money -= sasaikudasaiValue
                        inventory.append('Сасай кудасай')
                        self.power += sasaikudasaiPower
                        print('Оружие купленно!')
                    else:
                        print('Недостаточно денег')
            elif ask == 'ничего' or ask == 'нет':
                break

    def farm(self):
        gryadka = 0
        a = 0
        os.system('cls')
        while True:
            print('Если вы купите грядку, то скорость сбора огурцов улеличится!')
            if gryadka < 9:
                buying = str(input('Хотите купить грядку?(10 золотых): '))
                if buying == 'да':
                    if self.money >= 10:
                        print('Грядка куплена!')
                        gryadka += 1
                        self.money -= 10
                    else:
                        print('Нет денег на грядку!')
                else:
                    break
            else:
                print('Достигнут предел грядок!')
                break

        aks = str(input('Хотите сажать огурцы?(1 золотая за огурец) '))
        if aks == 'да':
            N = int(input('Сколько дней сажать? '))
            how = str(input('Какой режим? (автоматический(нельзя прервать) / ручной(можно прервать)) '))
            if how == 'автоматический':
                for i in range(N):
                    self.money += 1
                    print('Огурцов посажено = ',a)
                    a+=1
                    time.sleep(10 - gryadka)
                    os.system('cls')
                    print()
            else:
                for i in range(N):
                    self.money += 1
                    #os.system('cls')
                    print('Огурцов посажено = ',a)
                    a+=1
                    time.sleep(10 - gryadka)
                    print()
                    take = str(input('Нажми любую ENTER, чтоб собрать огурец. Напиши "нет", чтобы выйти: '))
                    if take == 'нет':
                        break
                    else:
                        os.system('cls')

    def river(self):
        if self.count2 == 0:
            self.count2 += 1
            os.system('cls')
            print()
            print('*Ты видишь дом рыбака*')
            time.sleep(2)
            print('*Зайдя в дом, рыбак вас поприветствовал*')
            time.sleep(2)
            ribak = str(input('Хотите поговорить с рыбаком? '))
            if ribak == 'да':
                print(Fore.GREEN + 'Привет, странник! Меня зовут Джейк')
                time.sleep(2)
                print('Я занимаюсь рыбной ловлей, и я как раз ищу помощника!')
                time.sleep(2)
                print('Ты мог бы ловить рыбу, а я мог бы ее продавать')
                time.sleep(2)
                print('Рыбу я буду брать не просто так, конечно')
                time.sleep(2)
                print('Я буду платить тебе за одну рыбу 10 золотых монет')
                time.sleep(2)
                print('Но для рыбной ловли тебе нужна удочка')
                time.sleep(2)
                print('Можешь купить ее у меня за 100 золотых монет')
                time.sleep(2)
                print(Fore.WHITE)
                udochka = str(input('Купить удочку? '))
                if udochka == 'да':
                    if self.money >= 100:
                        inventory.append('udochka')
                        self.money -= 100
                        self.count2 += 1
                    else:
                        print('Недостаточно денег!')
                else:
                    print(Fore.GREEN)
                    print('Приходи, как надумаешь!')
        elif self.count2 == 1:
            udochka = str(input('Купить удочку? '))
            if udochka == 'да':
                if self.money >= 100:
                    inventory.append('udochka')
                    self.money -= 100
                    self.count2 += 1
                else:
                    print('Недостаточно денег!')
            else:
                print(Fore.GREEN)
                print('Приходи, как надумаешь!')
        else:
            a = 0
            lovlya = str(input('Хотите ловить рыбу? (одна рыба в 10 секунд): '))
            if lovlya == 'да':
                N = int(input('Сколько рыбы ловить? '))
                for i in range(N):
                    self.money += 10
                    print('Рыбы поймано = ',a)
                    a+=1
                    time.sleep(10)
                    print()
                    ask = str(input('Нажми ENTER, чтоб подсечь рыбу. Напиши "нет", чтоб выйти: '))
                    if ask == 'нет':
                        break
                    else:
                        os.system('cls')

    def pomestie(self):
        os.system('cls')
        if self.count3 == 0:
            print('*Вы зашли в старое поместье*')
            time.sleep(0.5)
            print('*Вас встретил мужчина с длинной седой бородой*')
            time.sleep(0.5)
            ask = str(input('Хотите с ним поговорить? '))
            if ask == 'да':
                self.count3 += 1
                print(Fore.GREEN + 'Давно никто не заходил ко мне в гости...')
                time.sleep(0.5)
                print('Все боятся чудищ в подвале этого дома')
                time.sleep(0.5)
                print('Обходят стороной мое жилище')
                time.sleep(0.5)
                print('А ЭТО ЧЕРТОВО ПРАВИТЕЛЬСТВО НЕ МОЖЕТ ОТПРАВИТЬ ПАРУ СОЛДАТ!')
                time.sleep(0.5)
                print('Кстати, не хочешь мне помочь? А я взамен расскажу тебе кое-что...')
                time.sleep(0.5)
                print('...кое-что про царскую семью')
                time.sleep(0.5)
                ent = str(input('Нажми ENTER для продолжения...'))
                os.system('cls')
                print(Fore.WHITE)
                starik = str(input('Помочь? '))
                if starik == 'да':
                    hero1.dungeon()
                else:
                    print('Жаль, очень жаль...')
            else:
                print('*Вы покинули дом*')
        elif self.count3 == 1 and self.deadmonster == 0:
            starik = str(input('Помочь? '))
            if starik == 'да':
                hero1.dungeon()
            else:
                print('Жаль, очень жаль...')
        elif self.count3 == 1 and self.deadmonster == 1:
            print(Fore.GREEN + 'Спасибо, путник! Ты одолел монстра в подвале!')
            print('Вот тебе обещенная информация. Бывай!')
            inventory.append('Письмо королю')
            self.count3 += 1
        elif self.count3 == 2:
            print(Fore.GREEN + 'С тобой было приятно иметь дело!')

    def dungeon(self):
        monsterHP = 450
        monsterSpeed = 100
        HeroDamage = self.power + self.magic
        print('Ты спустился в подвал')
        print('В подвале ты видишь огромного монстра с красными глазами')
        ask = str(input('Напасть? '))
        if ask == 'да':
            os.system('cls')
            monsterPower = [30, 15, 10, 20, 20, 10, 20, 20, 15, 10]
            monsterHit = random.choice(monsterPower)
            while self.health > 0 or monsterHP > 0:
                os.system('cls')
                print('Ваш урон = ' + str(HeroDamage) + ' Урон монстра = ', str(monsterHit))
                print('Ваше здоровье = ' + str(self.health) + ' Здоровье монстра = ', str(monsterHP))
                if monsterSpeed > self.speed:
                    self.health -= monsterHit
                    if monsterHP < 0:
                        print()
                        print('Монстр повержен!')
                        self.deadmonster = 1
                        break
                    elif self.health < 0:
                        print()
                        print('Вы проиграли!')
                        break
                    monsterHP -= HeroDamage
                else:
                    monsterHP -= HeroDamage
                    if monsterHP < 0:
                        print()
                        print('Монстр повержен!')
                        self.deadmonster = 1
                        self.money += 100
                        inventory.append('Голова чудовища')
                        break
                    elif self.health < 0:
                        print()
                        print('Вы проиграли!')
                        break
                    self.health -= monsterHit
                time.sleep(1)

        else:
            print('Вы покинули подвал')

    def spawner(self):
        HeroDamage = self.power + self.magic
        print('Ты видишь перед собой слизня.')
        ask = str(input('Напасть? '))
        while ask == 'да':
            slimeHP = 50
            slimeSpeed = 50
            slimePower = [10, 7, 5, 10, 5, 5, 10, 10, 7, 5]
            slimeHit = random.choice(slimePower)
            while self.health > 0 or slimeHP > 0:
                os.system('cls')
                print('Ваш урон = ' + str(HeroDamage) + ' Урон монстра = ', str(slimeHit))
                print('Ваше здоровье = ' + str(self.health) + ' Здоровье монстра = ', str(slimeHP))
                if slimeSpeed > self.speed:
                    self.health -= slimeHit
                    if slimeHP < 0:
                        print()
                        print('Монстр повержен! Вот твои 5 монет')
                        self.money += 5
                        break
                    elif self.health < 0:
                        print()
                        print('Вы проиграли!')
                        break
                    slimeHP -= HeroDamage
                else:
                    slimeHP -= HeroDamage
                    if slimeHP < 0:
                        print()
                        print('Монстр повержен! Вот твои 5 монет')
                        self.money += 5
                        break
                    elif self.health < 0:
                        print()
                        print('Вы проиграли!')
                        break
                    self.health -= slimeHit
                time.sleep(1)
            ask = str(input('Напасть? '))



    def fountain(self):
        if self.firsttimefountain == 0:
            print('Это фонтан жизни. Здесь ты можешь отдохнуть после боя и восстановить здоровье')
            print('Скорость восстановления здоровья зависит от вашего природного дара и магии.')
            print('Чем выше эти показатели, тем быстрее будет восстанавливаться здоровье')
            self.firsttimefountain = 1
        while True:
            ask = str(input('Хотите отдохнуть? '))
            if ask == 'да' or 'Да':
                if self.health == self.healthConst:
                    print('Ваше здоровье полностью восстановленно!')
                    break
                else:
                    while self.health < self.healthConst:
                        print('Ваше текущее здоровье: ', self.health)
                        self.health += (self.aliluja + self.magic) // 3
                        time.sleep(2)
                    if self.health >= self.healthConst:
                        self.health = self.healthConst
                        print('Вы здоровы!')
                        break
    def shop(self):
        shopitems = ['Кожанная куртка', 'Железный нагрудник', 'Ботинки скорости', 'Зелье лечения', 'Броня Гефеста']
        if self.shopfirsttime == 0:
            print('Добро пожаловать в мою скромную лавку!')
            print('Здесь ты можешь купить разные предметы, которые тебе обязательно помогут!')
            print('На цены жаловаться смысла нет')
            print('Все равно моя лавка единственная')
            print()
            self.shopfirsttime = 1
        print()
        while True:
            print('Желаешь что-нибудь купить?')
            print(shopitems)
            ask = str(input('Что хочешь купить? '))
            if ask == 'Кожанная куртка' or ask == 'кожанная куртка':
                print('Данный предмет увеличит твое здоровье на 15 единиц')
                print('Цена предмета: 50 монет')
                buy = str(input('Купить?'))
                if buy == 'Да' or 'да':
                    if self.money >= 50:
                        self.money -= 50
                        print('Вы купили кожанную куртку!')
                        self.healthConst += 15
                        self.health += 15
                        inventory.append('Кожанная куртка')
                    else:
                        print('Недостаточно монет!')
            elif ask == 'Железный нагрудник' or ask == 'железный нагрудник':
                print('Данный предмет увеличит твое здоровье на 30 единиц')
                print('Цена предмета: 100 монет')
                buy = str(input('Купить?'))
                if buy == 'Да' or 'да':
                    if self.money >= 100:
                        self.money -= 100
                        print('Вы купили железный нагрудник!')
                        self.healthConst += 30
                        self.health += 30
                        inventory.append('Железный нагрудник')
                    else:
                        print('Недостаточно монет!')
            elif ask == 'Ботинки скорости' or ask == 'ботинки скорости':
                print('Данный предмет увеличит твою скорость на 15 единиц')
                print('Цена предмета: 150 монет')
                buy = str(input('Купить?'))
                if buy == 'Да' or 'да':
                    if self.money >= 150:
                        self.money -= 150
                        print('Вы купили ботинки скорости!')
                        self.speed += 15
                        inventory.append('Ботинки скорости')
                    else:
                        print('Недостаточно монет!')
            elif ask == 'Зелье лечения' or ask == 'зелье лечения':
                print('Данный предмет мнговенно восстановит 30 единиц здоровья')
                print('Цена предмета: 50 монет')
                buy = str(input('Купить?'))
                if buy == 'Да' or 'да':
                    if self.money >= 50:
                        self.money -= 50
                        print('Вы купили зелье лечения!')
                        inventory.append('Зелье лечения')
                    else:
                        print('Недостаточно монет!')
            elif ask == 'Броня Гефеста' or ask == 'броня гефеста' or ask == 'броня Гефеста':
                print('Данный предмет увеличит ваше здоровье на 300 единиц')
                print('Цена предмета: 1000 монет')
                buy = str(input('Купить?'))
                if buy == 'Да' or 'да':
                    if self.money >= 1000:
                        self.money -= 1000
                        print('Вы купили Броню Гефеста!')
                        inventory.append('Броня Гефеста')
                    else:
                        print('Недостаточно монет!')

            elif ask == 'ничего' or 'нет':
                break
    def boss(self):
        print('Ты набрался мужества и отправился на бой с боссом!')
        print('Ты видишь перед собой огромное тело минотавра')
        print('Его глаза залиты кровью, а в руках огромный топор')
        fight = str(input('Напасть? '))
        if self.deadboss == 0:
            if fight == 'да' or fight == 'Да':
                bosspower = [50, 50, 50, 100, 150, 35, 50, 80, 25]
                bossspeed = 150
                bosshp = 500
                bosshit = random.choice(bosspower)
                HeroDamage = self.power + self.magic
                while self.health > 0 or bosshp > 0:
                    os.system('cls')
                    print('Ваш урон = ' + str(HeroDamage) + ' Урон монстра = ', str(bosshit))
                    print('Ваше здоровье = ' + str(self.health) + ' Здоровье монстра = ', str(bosshp))
                    if bossspeed > self.speed:
                        self.health -= bosshit
                        if bosshp < 0:
                            print()
                            print('Босс повержен! Ты лучший. Гейм овер')
                            self.money += 100000
                            inventory.append('Голова минотавра')
                            self.deadboss = 1
                            break
                        elif self.health < 0:
                            print()
                            print('Вы проиграли!')
                            break
                        bosshp -= HeroDamage
                    else:
                        bosshp -= HeroDamage
                        if bosshp < 0:
                            print()
                            print('Босс повержен! Ты лучший. Гейм овер')
                            self.money += 100000
                            inventory.append('Голова минотавра')
                            self.deadboss = 1
                            break
                        elif self.health < 0:
                            print()
                            print('Вы проиграли!')
                            break
                        self.health -= bosshit
                    time.sleep(1)
            else:
                print('Вы покинули локацию, трус!')
        else:
            print('Ты уже одолел босса!')

print('О, ты очнулся! Ну и долго же ты спал...')
print('Что? Не знаешь, где ты? Не знаешь, что происходит?')
heroName = str(input('Я помогу тебе. Давай ты сначала вспомнишь свое имя, а потом мы продолжим: '))
hero1 = Hero(heroName)
print('Отлично, ' + str(heroName) + ', ты еще не все забыл')
print('Для начала несколько правил:')
print('1) Отвечай односложно и старайся не допускать ошибок')
print('2) Если нужно вызвать командное меню - напиши "помощник"')
print('3) Не пытайся сломать игру и наслаждайся процессом')
print('Ну, в путь!')
print()

towns = ['старый дом', 'деревня', 'река', 'поместье', 'лес', 'фонтан', 'логово минотавра']

while True:
    print()
    print(Fore.WHITE + 'Я слышал про эти места:' + str(towns))
    ask = str(input('Куда отправимся? '))
    print()
    if ask == 'деревня':
        hero1.penza()
    elif ask == 'помощник':
        help = str(input(comandlist))
        helper(help)
    elif ask == 'старый дом':
        hero1.oldHouse()
    elif ask == 'река':
        hero1.river()
    elif ask == 'поместье':
        hero1.pomestie()
    elif ask == 'лес':
        hero1.spawner()
    elif ask == 'фонтан':
        hero1.fountain()
    elif ask == 'логово минотавра':
        hero1.boss()

