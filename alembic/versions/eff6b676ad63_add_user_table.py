"""add user table

Revision ID: eff6b676ad63
Revises: 
Create Date: 2023-11-19 12:16:19.610517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eff6b676ad63'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('disabled', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='user_pkey')
    )   

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###