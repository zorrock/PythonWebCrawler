# coding=utf-8

from datetime import datetime
from sqlalchemy import update, select

from pear.models.tables import crawler, engine
from pear.utils.const import Crawler_Status


class CrawlerDao(object):
    conn = engine.connect()

    @classmethod
    def create(cls, args, info=None, extra=None):
        sql = crawler.insert().values(
            status=Crawler_Status.Crawling,
            created=datetime.now()
        )
        if args is not None:
            sql = sql.values(args=args)
        if extra is not None:
            sql = sql.values(extra=extra)
        return cls.conn.execute(sql).inserted_primary_key[0]

    @classmethod
    def update_by_id(cls, crawler_id, status=None, data_count=None, total=None, finished=None, info=None, extras=None):
        sql = update(crawler).where(crawler.c.id == crawler_id)
        if status:
            sql = sql.values(status=status)
        if data_count:
            sql = sql.values(data_count=data_count)
        if total:
            sql = sql.values(total=total)
        if finished:
            sql = sql.values(finished=finished)
        if info:
            sql = sql.values(info=info)
        if extras:
            sql = sql.values(extras=extras)
        cls.conn.execute(sql)

    @classmethod
    def get_by_id(cls, crawler_id, status=None):
        sql = select([crawler]).where(crawler.c.id == crawler_id)
        if status:
            sql = sql.where(crawler.c.status == status)
        return cls.conn.execute(sql).first()

    @classmethod
    def batch_get_by_status(cls, page=1, per_page=20, status=None):
        sql = select([crawler])
        sql = sql.limit(per_page).offset((page - 1) * per_page).order_by(crawler.c.id.asc())
        if status:
            sql = sql.where(crawler.c.status == status)
        return cls.conn.execute(sql).fetchall()