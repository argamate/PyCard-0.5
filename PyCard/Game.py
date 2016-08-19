import random, sys, time
class game:

    def __init__(self):
        self.health = 10
        self.level = 1
        self.materials = {
            "drister" : {"amount" : 0,"rare" : 1},
            "jenemite" : {"amount" : 0,"rare" : 2},
            "frostone" : {"amount" : 0,"rare" : 3},
            "hicrogin" : {"amount" : 0,"rare" : 4},
            "pandrome" : {"amount" : 0,"rare" : 5} ,
            "hyporilium" : {"amount" : 0,"rare" : 6},
            "kryptonite" : {"amount" : 0,"rare" : 7},
            "awrient" : {"amount" : 0,"rare" : 8},
            "solarius" : {"amount" : 0,"rare" : 9},
            "O-Qiralium" : {"amount" : 0,"rare" : 10}
        }
        self.money = 3
        self.animal = 0
        self.up = 10
        # drister (made by gama)
        # jenemite (made by nrgGick)
        # frostone (made by nrgGick)
        # hicrogin (made by nrgGick)
        # pandrome (made by nrgGick)
        # hyporilium (made by gama)
        # kryptonite (made by nrgGick)
        # awrient (made by nrgGick)
        # solarius  (made by nrgGick)
        # o-qiralium (made by gama)
    def die(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("you died.")
            sys.exit(0)
        else:
            print(" >>> you lost {0} health".format(damage))
            return True
    def sell(self, cost):
        i = 1
        while i < 10:
            if self.getcost(self.getbyrare(i)) >= cost:
                break
            i += 1
        for m in self.materials: 
                if self.materials[m]["amount"] > 0 and self.materials[m]["rare"] > i:
                    self.materials[m]["amount"] -= 1
                    print(" >>> thank you for trading!")
                    self.money += cost
                    self.upgrade(2)
                    time.sleep(1)
                    return True
        else:
            print(" >>> you cant.")
            time.sleep(1)
            return False
    
    def upgrade(self, num):
        print(" >>> you got {0} UP!".format(num))
        time.sleep(1)
        change = int(self.up / 10)
        self.up += num
        if change != int(self.up / 10):
            print(" >>> you have reached a new level")
            self.level += 1
            time.sleep(2)
            self.health = self.level * 6
            self.money += self.level
            
    def animalsFight(self,animal,player):
        most = 0
        animalHealth = animal * 5
        animal = int(animal/2)
        if animal > player:
            most = animal
        else:
            most = player
        i = 1
        while i < most:
            rp = random.randint(1,14)
            ap = random.randint(1,animal)
            if i <= animal:
                if not self.die(ap):
                    return False
                time.sleep(1)
            if i <= self.level:
                if animalHealth - rp <= 0:
                    print(" >>> you killed the animals.")
                    self.upgrade(5)
                    time.sleep(1)
                    self.money += (animal * 2)
                    return True
                else:
                    animalHealth -= rp
                    print(" >>> you hit the animals with {0} damage".format(rp))
                    time.sleep(1)
            i += 1
        else:
            print(" >>> the animals ran away")
            self.upgrade(2)
            time.sleep(1)
            return True
    def getbyrare(self, num):
        for m in self.materials:
            if self.materials[m]["rare"] == num:
                return m
    def getcost(self,material):
        if material == "drister" : 
            return 2
        elif material == "jenemite" : 
            return 5
        elif material == "frostone" : 
            return 10
        elif material == "hicrogin" : 
            return 20
        elif material == "pandrome" : 
            return 45
        elif material == "hyporilium" : 
            return 65
        elif material == "kryptonite" : 
            return 90
        elif material == "awrient" : 
            return 120
        elif material == "solarius" : 
            return 150
        elif material == "O-Qiralium" :
            return 200
    def fight(self,enemy, player = 0):
        most = 0
        enemyHealth = enemy * 7
        if enemy > player:
            most = enemy
        else:
            most = player
        i = 1
        while i <= most:
            rp = random.randint(1,14)
            ep = random.randint(1,14)
            if i <= enemy:
                if not self.die(ep):
                    return False
            if i <= self.level:
                if enemyHealth - rp <= 0:
                    money = random.randint(1,13)
                    print(" >>> dont kill me! i will pay you some money!")
                    time.sleep(1)
                    choice = input(" >>> the player offers {0}$ for letting him go away(y/n)"
                                   .format(money))
                    if choice == 'y':
                        self.money += money
                        time.sleep(1)
                        self.upgrade(3)
                        return True
                    else:
                        print(" >>> you killed the enemy.")
                        self.upgrade(5)
                        time.sleep(1)
                        return True
                else:
                    enemyHealth -= rp
                    print(" >>> you hit the enemy with {0} damage".format(rp))
                    time.sleep(1)
            i += 1
        else:
            print(" >>> the enemy ran away")
            self.upgrade(3)
            time.sleep(1)
            return True
    def enemy(self, attack):
                return self.fight(attack, self.level)

    def paye(self, money):
        if self.money < money:
            print(" >>> you cant.")
            time.sleep(1)
            return False
        else:
            print(" >>> its nice to do buisness with you. ")
            time.sleep(1)
            self.money -= money
            return True
    def pay(self, money):
        if self.money < money:
            print(" >>> you cant.")
            time.sleep(1)
            return False
        else:
            print(" >>> good trade. ")
            time.sleep(1)
            self.money -= money
            return True
    def animals(self, amount):
        bof = input(" >>> you want to fight or buy? ((B)uy / (F)ight)")
        b = False
        if bof == 'b':
            if self.pay(amount):
                self.animal += amount
                return True
            else:
                return self.animals(amount)
        elif bof == 'f':
            attack = amount
            if self.animal > 0:
                print(" >>> your animals attacked the enemy animals!")
                attack -= self.animal
                self.animal = 0
                if attack <= 0:
                    self.money += amount
                    return True
            return self.animalsFight(attack, self.level)
                    
    def tsell(self, cost):
        i = 1
        while i < 10:
            if self.getcost(self.getbyrare(i))+5 >= cost:
                break
            i += 1
        for m in self.materials: 
                if self.materials[m]["amount"] > 0 and self.materials[m]["rare"] > i:
                    return m
        else:
            return self.getbyrare(i)
    def trysell(self, cost):
        i = 1
        while i < 10:
            if self.getcost(self.getbyrare(i))+5 >= cost:
                break
            i += 1
        for m in self.materials: 
                if self.materials[m]["amount"] > 0 and self.materials[m]["rare"] > i:
                    return True
        else:
            return False
    def buy(self, t, cost):
        if self.pay(cost):
            self.materials[self.getbyrare(t)]["amount"] += 1
            print(" >>> thank you for trading!")
            self.upgrade(2)
            time.sleep(1)
            return True
        else:
            print(" >>> you cant.")
            time.sleep(1)
            return False
        
    def gettype(self, t, num):
        if num > 10:
            return "Player"
        elif t == 1:
            return "Money"
        elif t == 2:
            return "Animal"
        elif t == 3:
            return "Upgrade"
        else:
            return self.getbyrare(num)
    
    def stats(self):
        print("health : " + str(self.health))
        print("level : " + str(self.level))
        print("money : " + str(self.money))
        print("UP: " + str(self.up))
        print("animals : " + str(self.animal))
        for m in self.materials:
            if self.materials[m]["amount"] != 0:
                print("{0} : ".format(m) + str(self.materials[m]["amount"]))
                

    def start(self, turns):
        turn = -1
        while turn < turns:
            sss = random.randint(0,666)
            if sss == 666:
                print("45 72 72 6f 72 3a 20 55 6e 6b 6e 6f 77 6e 53 6f 75 72 63 65")
                sys.exit(0)
            num = random.randint(0, 13) 
            t = random.randint(1, 4) 
            if num == 0:
                self.stats()
                print(" >>> you have stopped by an enemy!")
                time.sleep(1)
                br = False
                turn += 1
                if not self.enemy(1):
                    break
                else:
                    continue
            if num > 10:
                self.stats()
                print(" >>> Player level {0} stopped you.".format(num-10+self.level-1))
                br = False
                turn += 1
                cards = {}
                while True:
                    choose = input(" >>> what would you like to do? ((P)ay / (T)rade / (F)ight) ")
                    if choose == 'p':
                        if self.paye(num-10+self.level-1):
                            br = True
                            break
                        else:
                            continue
                    elif choose == 't':
                        if len(cards) > 0:
                            print(" >>> nothing to trade")
                            continue
                        b = False
                        i = 0
                        while i < num - 10:
                            numt = random.randint(1, 14)
                            tt = random.randint(1, 4)
                            if numt > 10:
                                i += 1
                                continue
                            else:
                                cards[tt] = numt
                            i += 1
                        if b:
                            break
                        if len(cards) == 0:
                            print(" >>> nothing to trade")
                            continue
                        for c in cards:
                            if c == 4:
                                ran = random.randint(-5,5)
                                print(" > {0} that cost {1}".format(self.gettype(c,cards[c]), self.getcost
                                                         (self.getbyrare(cards[c])) + ran))
                            elif c == 1:                                
                                print(" > sell {0} for {1}".format(self.tsell(cards[c]), cards[c]))
                            elif c == 2:
                                print(" > {0} animals".format(cards[c]))
                            else:
                                print(" > upgrade your level by {0} UP".format(cards[c]))
                            buy = input(" >>> do you want to trade? (y/n)")
                            if buy == 'y':
                                if c == 1:
                                    if self.sell(cards[c]):
                                        b = True
                                        br = True
                                elif c == 2:
                                    if self.animals(cards[c]):
                                        b = True
                                        br = True 
                                elif c == 3:
                                    self.upgrade(cards[c])
                                    b = True
                                    br = True
                                elif c == 4:
                                    if self.buy(cards[c], self.getcost
                                                (self.getbyrare(cards[c])) + ran):
                                        b = True
                                        br = True
                            else:
                                continue
                            if b:
                                break
                        if b:
                            break
                    elif choose == 'f':
                        if self.enemy(num-10+self.level-1):
                            br = True
                            break
                        else:
                            sys.exit(0)
                if br:
                    continue
            if t == 4 and self.getcost(self.getbyrare(num)) > self.money:
                continue
            bm = 0
            if t == 1:
                if not self.trysell(num):
                    continue
            br = False
            turn += 1
            self.stats()
            if t == 4:
                print(" >>> you found {0} that cost {1}, you want to buy? (y/n)"
                      .format(self.gettype(t, num), self.getcost(self.getbyrare(num))), end='')
            elif t == 1:
                print(" >>> want to sell {0} for {1}$? (y/n)"
                      .format(self.tsell(num), num), end='')
            elif t == 2:
                print(" >>> you found {0} animals"
                      .format(num))
            if t == 1 or t == 4:
                open = input()
                if open == 'n':
                    time.sleep(1)
                    continue
            if t == 1:
                self.sell(num)
                continue
            elif t == 2:
                if not self.animals(num):
                    break
                continue
            elif t == 3:
                self.upgrade(int(num/2))
                time.sleep(1)
                continue
            else:
                if self.buy(num, self.getcost(self.getbyrare(num))):
                    continue
        else:
            print(" >>> GAME OVER! level: {0}".format(self.level))
myGame = game()
myGame.start(100)
