"""empty message

Revision ID: 6f3111154870
Revises: 8a4bb95aaec2
Create Date: 2022-10-08 22:16:34.032616

"""
from alembic import op
import sqlalchemy as sa
import models.news
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6f3111154870'
down_revision = '8a4bb95aaec2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('news', sa.Column('original', postgresql.UUID(), nullable=True))
    op.drop_constraint('fk__news__source__raw', 'news', type_='foreignkey')
    op.create_foreign_key(op.f('fk__news__original__raw'), 'news', 'raw', ['original'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk__news__original__raw'), 'news', type_='foreignkey')
    op.create_foreign_key('fk__news__source__raw', 'news', 'raw', ['source'], ['id'])
    op.drop_column('news', 'original')
    op.drop_column('news', 'summary')
    # ### end Alembic commands ###
