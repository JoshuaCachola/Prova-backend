"""create-personal-stats-table

Revision ID: 4f31cb1692df
Revises: 895794fff0a6
Create Date: 2020-06-11 12:15:12.238717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f31cb1692df'
down_revision = '895794fff0a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personal_route_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('best_time', sa.Integer(), nullable=True),
    sa.Column('average_time', sa.Integer(), nullable=True),
    sa.Column('number_of_runs', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('routes', sa.Column('total_number_of_runs', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('routes', 'total_number_of_runs')
    op.drop_table('personal_route_stats')
    # ### end Alembic commands ###