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
            time.sleep(2)
            print('*Подойдя к столу, ты увидел на нем 3 золотые монетки и старую книгу*')
            time.sleep(2)
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
            hero1.magazin()
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
        weapons = ['Ржавый меч', 'Секира ужаса', 'Посох обнуления', 'Обычный меч']
        print('Привет странник! Не желаешь купить что-нибудь?')
        print(weapons)
        while True:
            ask = str(input('Что-нибудь приглянулось? '))
            if ask == 'ржавый меч':
                print('Цена товара: ' + str(firstSwordValue))
                print('Сила: ' + str(firstSwordPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= firstSwordValue:
                        self.money -= firstSwordValue
                        inventory.append('Ржавый меч')
                    else:
                        print('Недостаточно денег')
            elif ask == 'секира ужаса':
                print('Цена товара: ' + str(sekiraValue))
                print('Сила: ' + str(sekiraPower1))
                print('Сила ужаса: ' + str(sekiraPower2))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= sekiraValue:
                        self.money -= sekiraValue
                        inventory.append('Секира ужаса')
                    else:
                        print('Недостаточно денег')
            elif ask == 'посох обнуления':
                print('Цена товара: ' + str(zeroWandValue))
                print('Сила: ' + str(zeroWandPower1))
                print('Сила обнуления: ' + str(zeroWandPower2))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= zeroWandValue:
                        self.money -= zeroWandValue
                        inventory.append('Посох обнуления')
                    else:
                        print('Недостаточно денег')
            elif ask == 'обычный меч':
                print('Цена товара: ' + str(secondSwordValue))
                print('Сила: ' + str(secondSwordPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= secondSwordValue:
                        self.money -= secondSwordValue
                        inventory.append('Обычный меч')
                    else:
                        print('Недостаточно денег')
            elif ask == 'ничего' or 'нет':
                break

    def farm(self):
        gryadka = 0
        a = 0
        os.system('cls')
        while True:
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
        aks = str(input('Хотите сажать огурцы?(1 золотая за огурец) '))
        if aks == 'да':
            N = int(input('Сколько дней сажать? '))
            how = str(input('Какой режим? (Автоматический(нельзя прервать) / ручной(можно прервать)) '))
            if how == 'Автоматический' or 'автоматический':
                for i in range(N):
                    self.money += 1
                    print('Огурцов посажено = ',a)
                    a+=1
                    time.sleep(10 - gryadka)
                    os.system('cls')
                    print()
            elif how == 'ручной':
                for i in range(N):
                    self.money += 1
                    #os.system('cls')
                    print('Огурцов посажено = ',a)
                    a+=1
                    time.sleep(10 - gryadka)
                    print()
                    ask = str(input('Нажми любую ENTER, чтоб собрать огурец. Напиши "нет", чтобы выйти: '))
                    if ask == 'нет':
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
                print('Я буду платить тебе за одну рыбу 5 золотых монет')
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
                    self.money += 5
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
            time.sleep(2)
            print('*Вас встретил мужчина с длинной седой бородой*')
            time.sleep(2)
            ask = str(input('Хотите с ним поговорить? '))
            if ask == 'да':
                self.count3 += 1
                print(Fore.GREEN + 'Давно никто не заходил ко мне в гости...')
                time.sleep(2)
                print('Все боятся чудищ в подвале этого дома')
                time.sleep(2)
                print('Обходят стороной мое жилище')
                time.sleep(2)
                print('А ЭТО ЧЕРТОВО ПРАВИТЕЛЬСТВО НЕ МОЖЕТ ОТПРАВИТЬ ПАРУ СОЛДАТ!')
                time.sleep(2)
                print('Кстати, не хочешь мне помочь? А я взамен расскажу тебе кое-что...')
                time.sleep(2)
                print('...кое-что про царскую семью')
                time.sleep(2)
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
        HeroHP = self.health
        HeroDamage = 0
        if len(inventory) > 0:
            for elem in inventory:
                if elem == 'Ржавый меч':
                    HeroDamage = self.power + firstSwordPower
                elif elem == 'Обычный меч':
                    HeroDamage = self.power + secondSwordPower
                elif elem == 'Секира ужаса':
                    HeroDamage = self.power + sekiraPower1 + sekiraPower2
                elif elem == 'Посох обнуления':
                    HeroDamage = self.power + zeroWandPower1 + zeroWandPower2
        else:
            HeroDamage = self.power + self.magic
        print('Ты спустился в подвал')
        print('В подвале ты видишь огромного монстра с красными глазами')
        ask = str(input('Напасть? '))
        if ask == 'да':
            herohealth = self.health
            os.system('cls')
            while self.health > 0 or monsterHP > 0:
                monsterPower = [10, 15, 10, 10, 10, 10, 10, 20, 15, 10]
                monsterHit = random.choice(monsterPower)
                os.system('cls')
                print('Ваш урон = ' + str(HeroDamage) + ' Урон монстра = ',str(monsterHit))
                print('Ваше здоровье = '+ str(herohealth) + ' Здоровье монстра = ',str(monsterHP))
                herohealth -= monsterHit
                monsterHP -= HeroDamage
                time.sleep(1)
                if monsterHP < 0:
                    print()
                    print('Монстр повержен!')
                    self.deadmonster = 1
                    break
                elif herohealth < 0:
                    print()
                    print('Вы проиграли!')
                    self.health = HeroHP
                    break
        else:
            print('Вы покинули подвал')


print('О, ты очнулся! Ну и долго же ты спал...')
print()
time.sleep(2)
print('Что? Не знаешь, где ты? Не знаешь, что происходит?')
print()
time.sleep(2)
heroName = str(input('Я помогу тебе. Давай ты сначала вспомнишь свое имя, а потом мы продолжим: '))
hero1 = Hero(heroName)
print()
print('Отлично, ' + str(heroName) + ', ты еще не все забыл')
print()
time.sleep(2)
os.system('cls')
print('Для начала несколько правил:')
print('1) Отвечай односложно и старайся не допускать ошибок')
time.sleep(2)
print('2) Если нужно вызвать командное меню - напиши "помощник"')
time.sleep(2)
print('3) Не пытайся сломать игру и наслаждайся процессом')
time.sleep(2)
print('Ну, в путь!')
time.sleep(2)
print()

towns = ['старый дом', 'деревня', 'река', 'поместье']

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
