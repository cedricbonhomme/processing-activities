"""update_nullable_valuefor_objects_and_schemas

Revision ID: fbaf9c31d7bb
Revises: 93451e9eda64
Create Date: 2021-04-12 13:55:09.358585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbaf9c31d7bb'
down_revision = '93451e9eda64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('json_object', 'creator_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('organization', 'is_membership_restricted',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('organization', 'is_membership_restricted',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('json_object', 'creator_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###