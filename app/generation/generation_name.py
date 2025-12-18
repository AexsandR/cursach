import requests
from mysql.connector.connection_cext import CMySQLConnection
import time

class Generation_people:
    def __init__(self, conn: CMySQLConnection) -> None:
        """принимает подключение к бд"""
        self.__conn = conn
    
    def __get_people(self, count_people: int) -> list[dict[str, str | int]]:
        response = requests.get(f"https://api.randomdatatools.ru/?count={count_people}")
        data = response.json()

        return data if type(data) is list else [data]
    
    def generation_clients(self, count_client: int) -> None:
        """создаем пользователей для таблицы Clients"""
        cur = self.__conn.cursor()
        while count_client != 0:
            if count_client - 100 < 0:
                people = self.__get_people(count_client)
                count_client = 0
            else:
                people = self.__get_people(count_client - 100)
                count_client -= 100
            print(len(people))
            for human in people:
                print(human)
                fio = f'{human["LastName"]} {human["FirstName"]} {human["FatherName"]}'
                email = human["Email"]
                cur.execute("CALL online_shop.addClient(%s, %s)", (fio, email))                
            if count_client != 0:
                time.sleep(1)
        self.__conn.commit()
        cur.close()




  
