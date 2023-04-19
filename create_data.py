import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trello.settings")
django.setup()

from myapp.models import Board, List, Card, User

# get the User model
user = User.objects.get(email="duonghuy.180602@gmail.com")

# create the boards
board1 = Board.objects.create(name='Board 1', owner=user)
board2 = Board.objects.create(name='Board 2', owner=user)

# create the lists for board1
list1_board1 = List.objects.create(name='List 1', board=board1)
list2_board1 = List.objects.create(name='List 2', board=board1)
list3_board1 = List.objects.create(name='List 3', board=board1)

# create the lists for board2
list1_board2 = List.objects.create(name='List 1', board=board2)
list2_board2 = List.objects.create(name='List 2', board=board2)

# create the cards for list1_board1
card1_list1_board1 = Card.objects.create(description='Card 1', order=1,  list=list1_board1)
card2_list1_board1 = Card.objects.create(description='Card 2', order=2,  list=list1_board1)
card3_list1_board1 = Card.objects.create(description='Card 3', order=3,  list=list1_board1)
