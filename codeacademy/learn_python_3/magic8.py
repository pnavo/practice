# Simulation of a magic eight ball

import random

name = ''
# question = 'Is this real life?'
question = ''
answer = ''

# generate random ints between 1 and 9
random_number = random.randint(1,9)

# check to see if it's working
# print(random_number)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very Doubtful'
else: answer = 'Error'
if name:
  print(f'{name} asks: {question}')
else:
  print(f'Question: {question}')
if question:
  print(f'Magic 8-Ball\'s answer: {answer}')
else:
  print('You didn\'t ask a question')