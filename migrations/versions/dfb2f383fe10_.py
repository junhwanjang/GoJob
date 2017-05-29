"""empty message

Revision ID: dfb2f383fe10
Revises: None
Create Date: 2017-05-29 14:00:47.824348

"""

# revision identifiers, used by Alembic.
revision = 'dfb2f383fe10'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('location', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('userid', sa.String(length=30), nullable=False),
    sa.Column('userpw', sa.String(length=30), nullable=False),
    sa.Column('fb_id', sa.String(length=100), nullable=False),
    sa.Column('fb_accesstoken', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=True),
    sa.Column('updated', sa.DATETIME(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fb_accesstoken'),
    sa.UniqueConstraint('fb_id'),
    sa.UniqueConstraint('userid')
    )
    op.create_table('job',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('pay', sa.INTEGER(), nullable=False),
    sa.Column('work_style', sa.String(length=50), nullable=False),
    sa.Column('role', sa.String(length=30), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.Column('fb_article_id', sa.String(length=100), nullable=True),
    sa.Column('end', sa.DATE(), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fb_article_id'),
    sa.UniqueConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    op.drop_table('user')
    op.drop_table('company')
    ### end Alembic commands ###
