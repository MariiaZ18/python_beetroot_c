"""TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above."""

channels = ["BBC", "Discovery", "TV1000"]


class TV_controller:
    def __init__(self, channels: list):
        self.channels = channels
        self._current_channel = 0
        self.count = 0
        self.it = iter(channels)
        self.t = channels[self.count]

    def first_channel(self):
        return next(self.it)

    def last_channel(self):
        self.len_of_chan = len(channels) - 1
        return channels[self.len_of_chan]

    def turn_channel(self, num: int):
        self._current_channel = num - 1
        return self.current_channel()

    def next_channel(self):
        if self.count == self.len_of_chan:
            self.count = 0
        else:
            self.count += 1
        self.t = self.channels[self.count]
        return self.t

    def previous_channel(self):
        if self.count == 0:
            self.count = self.len_of_chan
        else:
            self.count -= 1
        self.t = self.channels[self.count]
        return self.t

    def current_channel(self):
        return self.channels[self.count]

    def is_exist(self, chan_ex: str or int):
        self.if_chan_ex = chan_ex
        try:
            if type(chan_ex) == int and chan_ex in self.channels[chan_ex - 1]:
                print('Yes')
            elif type(chan_ex) == str and chan_ex in self.channels:
                print('Yes')
            else:
                print('No')
        except IndexError:
            print('No')


controller = TV_controller(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
