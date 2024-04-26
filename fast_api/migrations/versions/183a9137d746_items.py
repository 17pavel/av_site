"""items

Revision ID: 183a9137d746
Revises: f26a4bc193cc
Create Date: 2024-04-24 19:20:12.519156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183a9137d746'
down_revision = 'f26a4bc193cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('brand', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand'], ['brand.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('brand', sa.Integer(), nullable=True),
    sa.Column('model', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('parameters', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['brand'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.ForeignKeyConstraint(['model'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('item', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('items')
    op.drop_table('model')
    op.drop_table('category')
    op.drop_table('brand')
    # ### end Alembic commands ###
