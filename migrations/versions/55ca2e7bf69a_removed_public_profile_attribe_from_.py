"""removed_public_profile_attribe_from_user_table

Revision ID: 55ca2e7bf69a
Revises: fbaf9c31d7bb
Create Date: 2021-04-12 14:04:41.688345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55ca2e7bf69a'
down_revision = 'fbaf9c31d7bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'public_profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('public_profile', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###