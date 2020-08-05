"""empty message

Revision ID: b6ba9a41b2ed
Revises: 5fcd6106e4a0
Create Date: 2020-07-25 17:20:50.392184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b6ba9a41b2ed'
down_revision = '5fcd6106e4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('expertise', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio', 'expertise')
    # ### end Alembic commands ###