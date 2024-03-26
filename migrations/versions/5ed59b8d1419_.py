"""empty message

Revision ID: 5ed59b8d1419
Revises: 3e1d0083687a
Create Date: 2024-03-21 16:59:55.642140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed59b8d1419'
down_revision = '3e1d0083687a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint('question_answer_key', type_='unique')
        batch_op.drop_constraint('question_option_a_key', type_='unique')
        batch_op.drop_constraint('question_option_b_key', type_='unique')
        batch_op.drop_constraint('question_option_c_key', type_='unique')
        batch_op.drop_constraint('question_option_d_key', type_='unique')
        batch_op.drop_constraint('question_questiona_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.create_unique_constraint('question_questiona_key', ['questiona'])
        batch_op.create_unique_constraint('question_option_d_key', ['option_d'])
        batch_op.create_unique_constraint('question_option_c_key', ['option_c'])
        batch_op.create_unique_constraint('question_option_b_key', ['option_b'])
        batch_op.create_unique_constraint('question_option_a_key', ['option_a'])
        batch_op.create_unique_constraint('question_answer_key', ['answer'])

    # ### end Alembic commands ###