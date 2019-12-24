from chapter06_greetingcard import GreetingCard


class BirthdayCard(GreetingCard):

    def __init__(self):
        super().__init__()
        self._sender_age = 0

    def greeting_msg(self):
        print(f'Sender: {self._sender} Happy {self._sender_age} birthday; Recipient: {self._recipient}')
