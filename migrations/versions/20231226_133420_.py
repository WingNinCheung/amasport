"""empty message

Revision ID: 7c3fecde7d4f
Revises: 99687f23bfec
Create Date: 2023-12-26 13:34:20.562790

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c3fecde7d4f'
down_revision = '99687f23bfec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('images', postgresql.ARRAY(sa.TEXT()), nullable=True))
    op.drop_constraint('products_name_key', 'products', type_='unique')
    op.drop_column('products', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('image', sa.VARCHAR(length=1000), autoincrement=False, nullable=False))
    op.create_unique_constraint('products_name_key', 'products', ['name'])
    op.drop_column('products', 'images')
    # ### end Alembic commands ###
