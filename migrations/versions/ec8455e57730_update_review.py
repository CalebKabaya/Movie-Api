"""update review

Revision ID: ec8455e57730
Revises: 8b2491e96838
Create Date: 2022-05-06 06:39:00.638984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec8455e57730'
down_revision = '8b2491e96838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('movie_title', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('movie_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
