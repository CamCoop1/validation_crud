"""Added Mode table

Revision ID: a66718b15d56
Revises: b7ac697d1e37
Create Date: 2024-11-09 09:02:56.508578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a66718b15d56'
down_revision = 'b7ac697d1e37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Mode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('group', sa.Enum('tracking', 'physics', 'slme', 'neutrals', name='vibegroups'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Mode')),
    sa.UniqueConstraint('name', name=op.f('uq_Mode_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Mode')
    # ### end Alembic commands ###
