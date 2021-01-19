import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add column to fuuu

Revision ID: 537626cc8aa4
Revises: c36518a7ecd1
Create Date: 2021-01-19 18:07:29.437562
"""

# Revision identifiers, used by Alembic.
revision = '537626cc8aa4'
down_revision = 'c36518a7ecd1'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
