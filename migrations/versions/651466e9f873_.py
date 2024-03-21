"""empty message

Revision ID: 651466e9f873
Revises: 4f9783f41760
Create Date: 2024-03-21 10:19:22.438791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651466e9f873'
down_revision = '4f9783f41760'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.Enum('USER', 'ADMIN', 'MODERATOR', name='usertype'),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.Enum('USER', 'ADMIN', 'MODERATOR', name='usertype'),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
