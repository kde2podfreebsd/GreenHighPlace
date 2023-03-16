"""empty message

Revision ID: 7de62e106479
Revises: 
Create Date: 2023-03-14 11:20:58.712594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de62e106479'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('active',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.BigInteger(), nullable=False),
    sa.Column('items', sa.String(), nullable=False),
    sa.Column('fullprice', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.String(length=64), nullable=False),
    sa.Column('methodpay', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatId', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.BigInteger(), nullable=False),
    sa.Column('nameOfProduct', sa.String(), nullable=False),
    sa.Column('numOfProducts', sa.Integer(), nullable=False),
    sa.Column('idFromProduct', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('complete',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.BigInteger(), nullable=False),
    sa.Column('items', sa.String(), nullable=False),
    sa.Column('fullprice', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.String(length=64), nullable=False),
    sa.Column('methodpay', sa.String(length=64), nullable=True),
    sa.Column('datetime_complete', sa.String(length=64), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('id_from_active', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatId', sa.BigInteger(), nullable=False),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('dateLogin', sa.String(length=64), nullable=True),
    sa.Column('refCode', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('newproduct',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatId', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('typeMedia', sa.String(), nullable=True),
    sa.Column('dirMedia', sa.String(), nullable=True),
    sa.Column('infoAbout', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatId', sa.BigInteger(), nullable=False),
    sa.Column('textRU', sa.String(), nullable=True),
    sa.Column('textEN', sa.String(), nullable=True),
    sa.Column('dirMedia', sa.String(), nullable=True),
    sa.Column('dirType', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('typeMedia', sa.String(), nullable=True),
    sa.Column('dirMedia', sa.String(), nullable=True),
    sa.Column('infoAbout', sa.String(), nullable=True),
    sa.Column('queue', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('refuse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.BigInteger(), nullable=False),
    sa.Column('items', sa.String(), nullable=False),
    sa.Column('fullprice', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.String(length=64), nullable=False),
    sa.Column('methodpay', sa.String(length=64), nullable=False),
    sa.Column('datetime_refuse', sa.String(length=64), nullable=False),
    sa.Column('reason', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('id_from_active', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refuse')
    op.drop_table('product')
    op.drop_table('post')
    op.drop_table('newproduct')
    op.drop_table('customer')
    op.drop_table('complete')
    op.drop_table('cart')
    op.drop_table('admin')
    op.drop_table('active')
    # ### end Alembic commands ###
