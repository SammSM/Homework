# ex1
# import random

# class Warior:
#     def __init__(self, name):
#         self.XP=100
#         self.name=name
#         self.is_not_dead=True

#     def die(self):
#         print(f'{self.name} is dead!')
#         self.is_not_dead=False

#     def deal_damage(self):
#         return (f'{self.name} deals damage to ')

#     def take_damage(self):
#         if self.XP>0:
#             self.XP-=20
#             print(f'{self.name} get damaged! -20XP')
#         if self.XP==0:
#             self.die()

# w1=Warior('Warior1')
# w2=Warior('Warior2')

# while w1.XP>0 and w2.XP>0:

#     s=random.choice(['w1', 'w2'])

#     if s=='w1':
#         print(f'{w2.deal_damage()}{w1.name}')
#         w1.take_damage()
#     elif s=='w2':
#         print(f'{w1.deal_damage()}{w2.name}')
#         w2.take_damage()

#     if w1.is_not_dead and w2.is_not_dead:
#         print(f'{w1.name} XP - {w1.XP}\
#             \n{w2.name} XP - {w2.XP}\n')

# print('\nBattle is over!')

#------------------------------------------------------------------------
# ex2
# class Student:

#     def __init__(self, name, surname, group, mark):
#         self.name=name
#         self.surname=surname
#         self.group=group
#         self.mark=mark

#     def student_info(self):
#         print(f'Name: {self.name}, Surname: {self.surname}, Group: {self.group}, Mark: {self.mark}')

# a=Student('A', 'AA', 1, 10)
# b=Student('B','BB', 2, 15)
# c=Student('C', 'CC', 1, 12)
# d=Student('D', 'DD', 2, 10)
# e=Student('E','EE', 3, 15)
# f=Student('F', 'FF', 4, 12)
# g=Student('G', 'GG', 5, 9)
# h=Student('H','HH', 5, 16)
# i=Student('I', 'II', 4, 20)
# j=Student('J', 'JJ', 3, 8)

# student_list=[a,b,c,d,e,f,g,h,i,j]
# student_list.sort(key=lambda Student: Student.mark, reverse=True)
# for i in student_list:
#     i.student_info()

#------------------------------------------------------------------------
# ex3
# from math import pi
# class Circle:
#     def __init__(self, x, y):
#         self.radius=1
#         self.x=x
#         self.y=y

#     def area(self):
#         print(f'Makeres: {pi*self.radius**2}')

#     def perimeter(self):
#         print(f'Paragic: {2*pi*self.radius}')

#     def multiple(self, k):
#         self.radius*=k

#     def intersect(self, other):
#         if ((self.x-self.y)**2+(self.y-other.y)**2)**0.5>2:
#             print('Not intersect!')
#         else:
#             print('Intersect!')

# c1=Circle(2,2)
# c2=Circle(5,6)
# c3=Circle(6,7)
# c4=Circle(3,6)

# circle_list=[c1, c2, c3, c4]

# c1.intersect(c2)
# c2.intersect(c3)
# c2.intersect(c4)
# c1.intersect(c4)

#------------------------------------------------------------------------
# ex4
# class Parent:
#     def __init__(self, name, age, child_list):
#         self.name=name
#         self.age=age
#         self.child_list=child_list

#     def give_info(self):
#         print(self.name, self.age)

#     def calm_child(self, child):
#         if child in self.child_list:
#             if child.calmness=='not_calm':
#                 child.calmness='calm'
#             else:
#                 print('Child is calm!')
#         else:
#             print('Cant calm the child!')

#     def feed_child(self, child):
#         if child in self.child_list:
#             if child.fullness=='hungry':
#                 child.fullness='full'
#             else:
#                 print('Child is full!')
#         else:
#             print('Cant feed the child!')

# class Child:
#     def __init__(self, name, age, calmness, fullness):
#         self.name=name
#         self.age=age
#         self.calmness=calmness
#         self.fullness=fullness

# C1=Child('C1', 5, 'not_calm', 'hungry')
# C2=Child('C2', 2, 'calm', 'hungry')
# C3=Child('C3', 5, 'calm', 'full')

# M1=Parent('Mother1', 25, [C1, C2])
# F1=Parent('Father1', 30, [C1, C2])

# M2=Parent('Mother1', 27, [C3])
# F2=Parent('Father1', 29, [C3])

# print(C1.calmness)
# M1.calm_child(C1)
# print(C1.calmness)
# print()
# print(C1.fullness)
# F2.feed_child(C1)
# print(C1.fullness)
# print()
# print(C3.fullness)
# M2.feed_child(C2)
# print(C3.fullness)


#------------------------------------------------------------------------
# ex5
# class Gardener:
#     def __init__(self, name):
#         self.name=name
#         self.garden_bed=[1,2,3,4,5]
#         self.garden_bed_dict={
#             1:1,
#             2:1,
#             3:1,
#             4:1,
#             5:1
#         }
#         self.potatoes_list=[]

#     def take_care(self, i):
#         if self.garden_bed_dict[i]<4:
#             self.garden_bed_dict[i]+=1
#         else:
#             print(f'Potato_{i} is already grown!')

#     def pick(self, i):
#         if i in self.garden_bed_dict and self.garden_bed_dict[i]==4:
#             self.potatoes_list.append(i)
#             self.garden_bed.remove(i)
#             self.garden_bed_dict.pop(i)
#         else:
#             print('Isn\'t grown yet!')

# G1=Gardener('James')
# G1.take_care(1)
# G1.take_care(1)
# G1.take_care(1)
# G1.take_carel(1)
# G1.pick(1)

# G1.take_care(5)
# G1.take_care(5)
# G1.take_care(5)
# G1.take_care(5)
# G1.pick(5)
# print(G1.potatoes_list)
# print(G1.garden_bed, G1.garden_bed_dict)

#------------------------------------------------------------------------
# ex7
# import random

# class Home:
#     def __init__(self):
#         self.food=50
#         self.money=0

# class Inhabitant:
#     def __init__(self):
#         self.fullness=50

#     def work(self, other):
#         other.money+=20
#         self.fullness-=5

#     def go_shop(self, other):
#         other.food+=10
#         other.money-=10

#     def eat(self, other):
#         self.fullness+=5
#         other.food-=10

#     def play(self):
#         self.fullness-=5

# home1=Home()

# inhabitant1=Inhabitant()
# inhabitant2=Inhabitant()

# for i in range(365):
#     print(f'Day{i}')
#     if inhabitant1.fullness<0:
#         print('Inhabitant1 died!')
#         break
#     if inhabitant2.fullness<0:
#         print('Inhabitant2 died!')
#         break
#     cube=random.randint(1, 6)
#     if inhabitant1.fullness<20:
#         inhabitant1.eat(home1)
#     if inhabitant2.fullness<20:
#         inhabitant2.eat(home1)
#     if home1.food<10:
#         inhabitant1.go_shop(home1)
#         inhabitant2.go_shop(home1)
#     if home1.money<50:
#         inhabitant1.work(home1)
#         inhabitant2.work(home1)
#     if cube==1:
#         inhabitant1.work(home1)
#         inhabitant2.work(home1)
#     elif cube==2:
#         inhabitant1.eat(home1)
#         inhabitant2.eat(home1)
#     else:
#         inhabitant1.play()
#         inhabitant2.play()

# if inhabitant2.fullness<0:
#     print('Inhabitant2 died!')


#------------------------------------------------------------------------
# ex8
# from random import shuffle

# class Card:
#     def __init__(self, hamar, mast):
#         self.hamar = hamar
#         self.mast = mast

#     def __str__(self):
#         return f"{self.hamar}{self.mast}"

# class Deck:
#     def __init__(self):
#         self.card_deck = []
#         for mast in ['♥', '♦', '♣', '♠']:
#             for hamar in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
#                 self.card_deck.append(Card(hamar, mast))
#         shuffle(self.card_deck)
#         self.card_deck_dict = {
#             '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
#             'J': 10, 'Q': 10, 'K': 10, 'A': 11
#         }
    
#     def print_deck(self):
#         for card in self.card_deck:
#             print(card, end=' ')
#         print()


# class Player:
#     def __init__(self, name, deck):
#         self.name = name
#         self.self_deck = deck.card_deck[:2]
#         deck.card_deck = deck.card_deck[2:]
#         self.summ = 0
#         for card in self.self_deck:
#             self.summ += deck.card_deck_dict[card.hamar]

#     def player_deck(self):
#         print(f'Player {self.name}: {", ".join(str(card) for card in self.self_deck)}')


# deck1 = Deck()
# deck1.print_deck()

# p1 = Player('A', deck1)
# p1.player_deck()
# print(f'{p1.name} score: {p1.summ}')

# p2 = Player('B', deck1)
# p2.player_deck()
# print(f'{p2.name} score: {p2.summ}')

# if p1.summ<=21 and p2.summ<=21:
#     if p1.summ<p2.summ:
#         print(f'{p2.name} is winner!')
#     elif p1.summ>p2.summ:
#         print(f'{p1.name} is winner!')

# if p1.summ>21:
#     print(f'{p2.name} is winner!')
# elif p2.summ>21:
#     print(f'{p1.name} is winner!')

#------------------------------------------------------------------------
# ex9
# class Cell:
#     def __init__(self, no):
#         self.no = no
#         self.val = ' '
#         self.free = True

# class Board:
#     def __init__(self):
#         self.board = {i: Cell(i) for i in range(1, 10)}

#     def display(self):
#         for i in range(1, 10, 3):
#             print(f"{self.board[i].val} | {self.board[i+1].val} | {self.board[i+2].val}")
#             if i < 7:
#                 print("--+---+--")

#     def check_winner(self):
#         win_combinations = [
#             (1, 2, 3), (4, 5, 6), (7, 8, 9),
#             (1, 4, 7), (2, 5, 8), (3, 6, 9),
#             (1, 5, 9), (3, 5, 7)
#         ]
        
#         for comb in win_combinations:
#             if (self.board[comb[0]].val == 
#                 self.board[comb[1]].val == 
#                 self.board[comb[2]].val != ' '):
#                 return self.board[comb[0]].val
        
#         return None

#     def is_full(self):
#         return all(not self.board[i].free for i in self.board)

# class Player:
#     def __init__(self, name, symbol):
#         self.name = name
#         self.symbol = symbol

#     def cell_togo(self, board, no):
#         if board.board[no].free:
#             board.board[no].val = self.symbol
#             board.board[no].free = False
#             return True
#         else:
#             print("Choose another cell!")
#             return False


# board = Board()
# player1 = Player("A", "X")
# player2 = Player("B", "O")

# current_player = player1

# while True:
#     board.display()
    
#     try:
#         i = int(input(f"{current_player.name} ({current_player.symbol}) goes to: "))
#         if i not in board.board:
#             print("Cell is not free!")
#             continue
#     except ValueError:
#         print("Enter a number between 1-9.")
#         continue

#     if current_player.cell_togo(board, i):
#         winner = board.check_winner()
#         if winner:
#             board.display()
#             print(f"{current_player.name} ({winner}) wins!")
#             break
        
#         if board.is_full():
#             board.display()
#             print("Full board!")
#             break
        
#         if current_player==player1:
#             current_player=player2
#         elif current_player==player2:
#             current_player=player1