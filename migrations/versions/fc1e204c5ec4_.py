"""empty message

Revision ID: fc1e204c5ec4
Revises: 8580b596a1b9
Create Date: 2020-08-07 21:55:37.259172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc1e204c5ec4'
down_revision = '8580b596a1b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('staff_username', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'portfolio', ['staff_username'])
    op.create_foreign_key(None, 'portfolio', 'staff', ['staff_username'], ['username'])
    op.create_unique_constraint('unique_username', 'staff', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_username', 'staff', type_='unique')
    op.drop_constraint(None, 'portfolio', type_='foreignkey')
    op.drop_constraint(None, 'portfolio', type_='unique')
    op.drop_column('portfolio', 'staff_username')
    # ### end Alembic commands ###