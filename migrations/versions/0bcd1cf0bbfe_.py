"""empty message

Revision ID: 0bcd1cf0bbfe
Revises: dbef325152f1
Create Date: 2021-08-26 08:25:05.449224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bcd1cf0bbfe'
down_revision = 'dbef325152f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film', sa.Column('featured_cast', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('film', 'featured_cast')
    # ### end Alembic commands ###