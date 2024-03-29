"""followers

Revision ID: 5887cd6da84e
Revises: 756e053d4051
Create Date: 2019-07-03 14:18:24.981286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5887cd6da84e'
down_revision = '756e053d4051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
