from operator import contains
import random
from tokenize import String
from nextcord.ext import commands
import os
import time
import json
from dotenv import load_dotenv
import nextcord

artistsf=open('artists.json',)
artistlist=json.load(artistsf)

selection=random.randint(1, 4)

j="yes"


j=artistlist[f'{selection}'][0]['Song']
j.lower
print(f"The correct song is {j}")
# while j=='yes':
#     j=input("Go again?")
#     guess=input("Who sings that song?!")

#     if guess==artistlist[f'1'][0]['Artist']:
#         print("Correct!")
#     else:
#         print("Sorry, you were wrong!")



# test=input("Enter something shithead: ")
# print(f"input was {test}")
# if test==artistlist['2'][0]['Artist']:
#     print("LETS GO!")
# else:
#     print("NOOOOO")

