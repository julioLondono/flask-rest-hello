"""empty message

Revision ID: 6e570913eba3
Revises: 43b0cf244958
Create Date: 2019-08-09 19:53:49.424250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e570913eba3'
down_revision = '43b0cf244958'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopingcart',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('products_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users_id', 'products_id')
    )
    op.drop_table('shoping_cart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoping_cart',
    sa.Column('users_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('products_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], name='shoping_cart_ibfk_1'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='shoping_cart_ibfk_2'),
    sa.PrimaryKeyConstraint('users_id', 'products_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('shopingcart')
    # ### end Alembic commands ###
