"""location table linked to user table guardian detail inside student table

Revision ID: 0a99f65139bb
Revises: fa60a6d22496
Create Date: 2020-08-30 15:55:30.069390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a99f65139bb'
down_revision = 'fa60a6d22496'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('travel_distance', sa.String(length=64), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('district', sa.String(length=64), nullable=True),
    sa.Column('municipality', sa.String(length=64), nullable=True),
    sa.Column('ward_no', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('guardian_address', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('guardian_name', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('guardian_phone', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('guardian_phone')
        batch_op.drop_column('guardian_name')
        batch_op.drop_column('guardian_address')
        batch_op.drop_column('full_name')

    op.drop_table('location')
    # ### end Alembic commands ###
