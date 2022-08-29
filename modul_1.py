from datetime import date, datetime
from os.path import exists



class Logger:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, path_to = './') -> None:
        self.path = path_to
        self.today = self.__date()
        self.__last_log = None
        self.name = f"log_{self.today.day}.{self.today.month}.{self.today.year%100}"
        if not exists(self.path+self.name):
            with open(self.path+self.name, "w") as f:
                pass

    @staticmethod
    def __date():
        return date.today()

    def write_log(self, mess: str):
        event = f"[{datetime.now().time()}] {mess}\n"
        self.__last_log = event
        with open(self.path+self.name, "a") as f:
            f.write(event)

    def claer_log(self) -> None:
        pass

    def get_logs(self) -> list:
        pass

    def get_last_event(self) -> str:
        return self.__last_log

    def get_all_logs(self) -> list:
        pass


if __name__ == "__main__":
    a = Logger()
    a.write_log("messs")
    print(a.get_last_event())
