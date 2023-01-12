"""empty message

Revision ID: 764d1f72b1f3
Revises: 99c7c3152c37
Create Date: 2023-01-12 17:14:27.031431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '764d1f72b1f3'
down_revision = '99c7c3152c37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
