"""empty message

Revision ID: 21e2e2da54b4
Revises: 3c676ea1a187
Create Date: 2020-05-25 01:55:51.074408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21e2e2da54b4'
down_revision = '3c676ea1a187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###