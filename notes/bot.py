"""
Example of a race condition
---------------------------

Run the script with different number of tables like

$ python bot.py 30
$ python bot.py 300
$ python bot.py 3000

When we increase the number of tables to serve, it's clear that the kitchen
inventory before and after won't match any more and the failure is not
reproducible. This is a simple example of race condition.

This problem can be fixed by placing a lock around the modification of the
shared state. In a large project, this requires you to know all the places
where the state is shared between threads.
"""
import sys
import threading
import queue
from attr import attrs, attrib


@attrs
class Cutlery:
    knives = attrib(default=42)
    forks = attrib(default=20)
    lock = attrib(default=threading.Lock())

    def change(self, knives, forks):
        # The += is implemented internally as
        # 1. Read the current value self.knives into a temporary location
        # 2. Add the new value knives to the value in that temporary location
        # 3. Copy the total in the temporary location to the original
        # location
        # The problem with preemptive multitasking is that any thread busy
        # with the steps above can be interrupted at any time
        self.knives += knives
        self.forks += forks

    def locked_change(self, knives, forks):
        with self.lock:
            self.change(knives, forks)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.locked_change(-knives, -forks)
        to.locked_change(knives, forks)


def demo_cutlery():
    cutlery = Cutlery(knives=20, forks=15)
    print(cutlery)
    cutlery.change(40, 25)
    print(cutlery)


KITCHEN = Cutlery(100, 100)


class ThreadBot(threading.Thread):
    def __init__(self, name):
        super(ThreadBot, self).__init__(target=self.manage_table)
        self.name = name
        self.tasks = queue.Queue()
        self.cutlery = Cutlery(0, 0)

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                KITCHEN.give(self.cutlery, 10, 10)
            elif task == "clean table":
                self.cutlery.give(KITCHEN, 10, 10)
            elif task == "shut down":
                # The “shutdown” will make the bots stop (so that
                # bot.join() a bit further down will return)
                # print(f"shut down the bot {self.name}")
                return


def main(n_tables):
    bots = [ThreadBot(i) for i in range(10)]
    for bot in bots:
        for _ in range(n_tables):
            bot.tasks.put("prepare table")
            bot.tasks.put("clean table")
        bot.tasks.put("shut down")

    print("The kitchen inventory before and after serving should be the same")
    print("Kitchen ->", KITCHEN)
    print("[main] bot start...")
    for bot in bots:
        bot.start()

    print("[main] bot join...")
    for bot in bots:
        bot.join()
    print("Kitchen ->", KITCHEN)


if __name__ == "__main__":
    # demo_cutlery()
    main(int(sys.argv[1]))

