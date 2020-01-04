from greetingcard import GreetingCard


class BirthdayCard(GreetingCard):

    def __init__(self, sender_age=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sender_age = sender_age

    def greeting_msg(self):
        print(f'Sender: {self._sender} Happy {self._sender_age} birthday; Recipient: {self._recipient}')
