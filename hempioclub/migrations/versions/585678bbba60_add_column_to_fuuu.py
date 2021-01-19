import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add column to fuuu

Revision ID: 585678bbba60
Revises: c36518a7ecd1
Create Date: 2021-01-19 17:51:21.569825
"""

# Revision identifiers, used by Alembic.
revision = '585678bbba60'
down_revision = 'c36518a7ecd1'
branch_labels = None
depends_on = None


def upgrade():
        op.add_column('foos', sa.Column('hello_on', AwareDateTime(),
                                default=tzware_datetime))


def downgrade():
        op.drop_column('foos', 'hello_on')
