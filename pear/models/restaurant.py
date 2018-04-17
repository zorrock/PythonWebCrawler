# coding=utf-8
from sqlalchemy import select

from pear.models.base import BaseDao
from pear.models.tables import ele_restaurant


class EleRestaurantDao(BaseDao):

    @classmethod
    def create(cls, restaurant_id, name, source, sales, arrive_time, send_fee, score, latitude, longitude):
        sql = ele_restaurant.insert().values(
            restaurant_id=restaurant_id,
            name=name,
            source=source,
            sales=sales,
            arrive_time=arrive_time,
            send_fee=send_fee,
            score=score,
            latitude=latitude,
            longitude=longitude
        )
        return cls.insert(sql)

    @classmethod
    def get_by_restaurant_id(cls, restaurant_id):
        sql = select([ele_restaurant]).where(ele_restaurant.c.restaurant_id == restaurant_id)
        return cls.get_one(sql)

    @classmethod
    def update_by_restaurant_id(cls, restaurant_id, name, source, sales, arrive_time, send_fee, score, latitude,
                                longitude):
        sql = ele_restaurant.update().where(ele_restaurant.c.restaurant_id == restaurant_id).values(
            name=name,
            source=source,
            sales=sales,
            arrive_time=arrive_time,
            send_fee=send_fee,
            score=score,
            latitude=latitude,
            longitude=longitude
        )
        return cls.update(sql)

    @classmethod
    def batch(cls, page=1, per_page=20):
        sql = select([ele_restaurant]).order_by(ele_restaurant.c.id.asc())
        return cls.get_list(sql, page, per_page)

    @classmethod
    def wrap_item(cls, item):
        if not item:
            return None
        return {
            "id": item.id,
            "restaurant_id": item.restaurant_id,
            "name": item.name,
            "source": item.source,
            "sales": item.sales,
            "arrive_time": item.arrive_time,
            "score": item.score,
            "latitude": item.latitude,
            "longitude": item.longitude
        }
