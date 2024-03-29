"""empty message

Revision ID: 58aab76d46a4
Revises: f5e66c989a72
Create Date: 2023-01-17 14:25:29.046076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58aab76d46a4'
down_revision = 'f5e66c989a72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokeballs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('ability', sa.String(length=50), nullable=False),
    sa.Column('base_experience', sa.Integer(), nullable=False),
    sa.Column('sprite_url', sa.String(), nullable=False),
    sa.Column('attack_base', sa.Integer(), nullable=False),
    sa.Column('hp_base', sa.Integer(), nullable=False),
    sa.Column('defense_base', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pokeball')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokeball',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('ability', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('base_experience', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sprite_url', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('attack_base', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hp_base', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('defense_base', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='pokeball_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pokeball_pkey')
    )
    op.drop_table('pokeballs')
    # ### end Alembic commands ###
