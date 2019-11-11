"""empty message

Revision ID: feb19f960cf7
Revises: 
Create Date: 2019-11-11 09:20:11.148966

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'feb19f960cf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('job_id')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', postgresql.UUID(), nullable=False),
    sa.Column('app_name', sa.String(length=128), nullable=False),
    sa.Column('state', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('states')
    op.drop_table('jobs')
    # ### end Alembic commands ###