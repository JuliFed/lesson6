class Clock:
    def __init__(self):
        self.i = 0

    def tick(self):
        self.i += 1

    def time(self):
        return self.i


# Часы будем прокидывать в конструкторе юнита
# за секунду сделать тысячу tick к примеру

