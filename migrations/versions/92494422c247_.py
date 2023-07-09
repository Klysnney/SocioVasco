"""empty message

Revision ID: 92494422c247
Revises: 
Create Date: 2023-07-09 08:01:06.139146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92494422c247'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socio',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('idade', sa.String(length=50), nullable=False),
    sa.Column('plano', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('socio')
    # ### end Alembic commands ###