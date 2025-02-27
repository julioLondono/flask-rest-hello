"""empty message

Revision ID: 3925afa4242b
Revises: b8d1524cb690
Create Date: 2019-08-08 16:13:00.654176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3925afa4242b'
down_revision = 'b8d1524cb690'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('isBillingAddress', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('addresses', 'isBillingAddress')
    # ### end Alembic commands ###
