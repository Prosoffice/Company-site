"""empty message

Revision ID: d01b13b4f4be
Revises: b6ba9a41b2ed
Create Date: 2020-08-02 21:27:52.074083

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd01b13b4f4be'
down_revision = 'b6ba9a41b2ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('projects', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio', 'projects')
    # ### end Alembic commands ###
