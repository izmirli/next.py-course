class GreetingCard:

    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f'Sender: {self._sender}; Recipient: {self._recipient}')
