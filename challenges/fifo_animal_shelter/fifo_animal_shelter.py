from queue import Queue

class AnimalShelter:
    def __init__(self):
        self.list_one = Queue()
        self.list_two = Queue()
    
    def enqueue(self, new_animal):
        self.list_one.enqueue(new_animal)

    def dequeue(self, pref):
        while self.list_one.front:
            if self.list_one.front.value is pref:
                return self.list_one.dequeue()

            if self.list_one.front != pref:       
                    b = self.list_one.dequeue()
                    self.list_two.enqueue(b)

        while self.list_two.front:
            a = self.list_two.dequeue()
            self.list_one.enqueue(a)
        if pref != 'dog' and pref != 'cat':
            return None

