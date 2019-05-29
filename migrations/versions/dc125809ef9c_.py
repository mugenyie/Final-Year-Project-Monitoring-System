"""empty message

Revision ID: dc125809ef9c
Revises: 3b52ec217d5c
Create Date: 2019-05-29 03:08:05.291407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc125809ef9c'
down_revision = '3b52ec217d5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projectslog', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('projectslog', 'project_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('projectslog', 'supervisor_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('projectslog', 'supervisor_remarks',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projectslog', 'supervisor_remarks',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('projectslog', 'supervisor_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('projectslog', 'project_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('projectslog', 'group_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
