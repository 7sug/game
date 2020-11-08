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
            if ask == 'Ржавый меч' or ask == 'ржавый меч':
                print('Цена товара: ' + str(firstSwordValue))
                print('Сила: ' + str(firstSwordPower))
                buy = str(input('Купить? '))
                if buy == 'да':
                    if self.money >= firstSwordValue:
                        self.money -= firstSwordValue
                        inventory.append('Ржавый меч')
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
                    else:
                        print('Недостаточно денег')
            elif ask == 'ничего' or 'нет':
                break

    def farm(self):
        gryadka = 0
        a = 0
        os.system('cls')
        while True:
            print('Если вы купите грядку, то скорость сбора огурцов улеличится!')
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
        else:
            HeroDamage = self.power + self.magic
        print('Ты спустился в подвал')
        print('В подвале ты видишь огромного монстра с красными глазами')
        ask = str(input('Напасть? '))
        if ask == 'да':
            os.system('cls')
            while self.health > 0 or monsterHP > 0:
                monsterPower = [30, 15, 10, 20, 20, 10, 20, 20, 15, 10]
                monsterHit = random.choice(monsterPower)
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
            while self.health > 0 or slimeHP > 0:
                slimePower = [10, 7, 5, 10, 5, 5, 10, 10, 7, 5]
                slimeHit = random.choice(slimePower)
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
        shopitems = ['Кожанная куртка', 'Железный нагрудник', 'Ботинки скорости', 'Зелье лечения']
        if self.shopfirsttime == 0:
            print('Добро пожаловать в мою скромную лавку!')
            print('Здесь ты можешь купить разные предметы, которые тебе обязательно помогут!')
            print('На цены жаловаться смысла нет')
            print('Все равно моя лавка единственная')
            self.shopfirsttime = 1
        print()
        while True:
            print('Желаешь что-нибудь купить?')
            print(shopitems)
            ask = str(input('Что хочешь купить? '))
            if ask == 'Кожанная куртка':
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
            elif ask == 'Железный нагрудник':
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
            elif ask == 'Ботинки скорости':
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
            elif ask == 'Зелье лечения':
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
            elif ask == 'ничего' or 'нет':
                break


print('О, ты очнулся! Ну и долго же ты спал...')
print('Что? Не знаешь, где ты? Не знаешь, что происходит?')
heroName = str(input('Я помогу тебе. Давай ты сначала вспомнишь свое имя, а потом мы продолжим: '))
hero1 = Hero(heroName)
print('Отлично, ' + str(heroName) + ', ты еще не все забыл')
os.system('cls')
print('Для начала несколько правил:')
print('1) Отвечай односложно и старайся не допускать ошибок')
print('2) Если нужно вызвать командное меню - напиши "помощник"')
print('3) Не пытайся сломать игру и наслаждайся процессом')
print('Ну, в путь!')
print()

towns = ['старый дом', 'деревня', 'река', 'поместье', 'лес', 'фонтан']

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
