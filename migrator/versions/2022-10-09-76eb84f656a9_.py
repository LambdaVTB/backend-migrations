"""empty message

Revision ID: 76eb84f656a9
Revises: c5c82f02b18f
Create Date: 2022-10-09 09:16:28.882449

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete, insert, and_, select
import models.news
from models.jobs import Jobs
from models.tags import Tags
from models.tags_jobs import TagsJobs


# revision identifiers, used by Alembic.
revision = '76eb84f656a9'
down_revision = 'c5c82f02b18f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    query = insert(Jobs).values(name='Бухгалтер').returning(Jobs.id)
    buh_id = session.execute(query).scalars().first()
    session.commit()
    query = insert(Jobs).values(name='Генеральный директор').returning(Jobs.id)
    gen_id = session.execute(query).scalars().first()
    session.commit()
    ids = dict()
    for name in ['Финансы', 'Экономика',  'Криптовалюты', 'Учет и налогообложение', 'Бизнес', 'Бухгалтеру',  'Вебинары для бухгалтеров', 'Банкротство', 'Кредитование', 'Банки',  'Трудовое право', 'Экономика России',  'Электронные трудовые книжки', 'ЕГАИС', 'Налоги, взносы, пошлины', 'ЭДО', 'НДФЛ', 'АУСН', 'Перевозка', 'Отчетность в ПФР', 'Мошенничество', 'Первичные документы', 'Экономические преступления', 'ПСН', 'Онлайн-кассы']:
        query = insert(Tags).values(name=name).returning(Tags.id)
        try:
            id = session.execute(query).scalars().first()
            session.commit()
        except Exception:
            session.rollback()
            query = select(Tags.id).where(Tags.name == name)
            id = session.execute(query).scalars().first()
        ids[name] = id
    for pair in ids.items():
        print(str(pair[1]))
        if not str(pair[1]):
            continue
        query = insert(TagsJobs).values(
            tag_id = str(pair[1]),
            job_id = str(buh_id)
        )
        session.execute(query)
        session.commit()
    ids = dict()
    for name in ['Финансы', 'Экономика', 'Маркетинг', 'PR', 'HR',  'Компании', 'Рынки', 'Бизнес', 'Технологии', 'Автоматизация', 'Мобилизация',  'Работодателю', 'Кредитование', 'Инвестиции', 'Санкции 2022',  'Общее', 'Карьера',  'Экономика России', 'IT-компании',  'Налоги, взносы, пошлины',  'Мошенничество', 'Экономические преступления']:
        query = insert(Tags).values(name=name).returning(Tags.id)
        try:
            id = session.execute(query).scalars().first()
            session.commit()
        except Exception:
            session.rollback()
            query = select(Tags.id).where(Tags.name == name)
            id = session.execute(query).scalars().first()
        ids[name] = id
    for pair in ids.items():
        print(str(pair[1]))
        if not str(pair[1]):
            continue
        query = insert(TagsJobs).values(
            tag_id = str(pair[1]),
            job_id = str(gen_id)
        )
        session.execute(query)
        session.commit()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    session.execute(delete(Jobs))
    session.execute(delete(TagsJobs))
    session.execute(delete(Tags))
    # ### end Alembic commands ###
