"""empty message

Revision ID: c04057dd1da9
Revises: c1de6a451490
Create Date: 2021-08-25 09:41:32.203982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04057dd1da9'
down_revision = 'c1de6a451490'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor_film',
    sa.Column('actor_id', sa.String(), nullable=True),
    sa.Column('film_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actor_film')
    # ### end Alembic commands ###