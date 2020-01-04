# from greetingcard import GreetingCard
import greetingcard
# from birthdaycard import BirthdayCard
import birthdaycard

gc = greetingcard.GreetingCard()
gc.greeting_msg()

bc = birthdaycard.BirthdayCard()
bc.greeting_msg()

bc2 = birthdaycard.BirthdayCard(5, 'Dan', 'Oren')
bc2.greeting_msg()

bc3 = birthdaycard.BirthdayCard(recipient='Dan', sender='Oren')
bc3.greeting_msg()
