"""Created new task table because could not reset task_id to 0 in original task table.

Revision ID: dfe8847b101b
Revises: f1bf59b1ec0f
Create Date: 2023-05-08 03:51:57.762248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfe8847b101b'
down_revision = 'f1bf59b1ec0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('task', 'title',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'title',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('task', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
