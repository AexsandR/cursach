import requests
from mysql.connector.connection_cext import CMySQLConnection
import random


import random

# Словари производителей (для ноутбуков и телефонов) - телефоны только цифры

class Generation_product:

    def __init__(self, conn: CMySQLConnection) -> None:
        """принимает подключение к бд"""
        self.__conn = conn
    
    def add_makers(self, makers: dict[str, str]):
        cur = self.__conn.cursor()
        for maker in makers:
            cur.execute("call online_shop.addManufacturer(%s, %s, %s)", (maker["name"], maker["inn"], maker["phone"]))
        self.__conn.commit()
        cur.close()

    
    def add_product(self, prosducts: list[dict[str, str | int]]) -> None:
        cur = self.__conn.cursor()
        for product in prosducts:
            description = product["description"]
            if len(description) > 400:
                description = description[:397] + "..."
            cur.execute("CALL online_shop.addProduct(%s, %s, %s, %s, %s, %s, %s, %s)", (product["name"],
                                                                description,
                                                                product["category_id"],
                                                                random.randint(1, 3),
                                                                product["manufacturer_id"],
                                                                product["category_id"],
                                                                product["price"],
                                                                product["cost_price"]))
        self.__conn.commit()
        cur.close()

    def generate_review(self, reviews: dict[str, str | int], count_client, count_product) -> None:
        cur = self.__conn.cursor()
        for i in range(1, count_client + 1):
            for j in range(1, count_product + 1):
                review = random.sample(reviews, 1)[0]
                cur.execute("call online_shop.addReview(%s, %s, %s, %s)", (i, j, review["text"], review["rating"]))
        self.__conn.commit()
        cur.close()