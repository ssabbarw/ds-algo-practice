class Notifier:

    def send(self, message):
        self.i = 0
        print(message, self.i)

n = Notifier()
n.send("asd")
print(n.i)