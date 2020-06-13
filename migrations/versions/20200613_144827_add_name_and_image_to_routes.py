"""Add name and image to routes

Revision ID: c83d5c808d7c
Revises: 80997cd240df
Create Date: 2020-06-13 14:48:27.786288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c83d5c808d7c'
down_revision = '80997cd240df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('routes', sa.Column('image', sa.Text(), nullable=True))
    op.add_column('routes', sa.Column('name', sa.String(), nullable=True))
    op.alter_column('runs', 'calories',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('runs', 'date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('runs', 'distance',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('runs', 'time',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('runs', 'time',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('runs', 'distance',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('runs', 'date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('runs', 'calories',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.drop_column('routes', 'name')
    op.drop_column('routes', 'image')
    # ### end Alembic commands ###
