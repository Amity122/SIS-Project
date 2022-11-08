"""waaaaaaaaaaaaaaaa

Revision ID: 4a2f482c0654
Revises: 595e6df95aad
Create Date: 2022-11-04 08:33:55.231259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a2f482c0654'
down_revision = '595e6df95aad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('courses_ibfk_1', 'courses', type_='foreignkey')
    op.create_foreign_key(None, 'courses', 'colleges', ['resp_college'], ['college_code'], onupdate='cascade', ondelete='SET NULL')
    op.drop_constraint('student_ibfk_1', 'student', type_='foreignkey')
    op.create_foreign_key(None, 'student', 'courses', ['course'], ['course_code'], onupdate='cascade', ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_foreign_key('student_ibfk_1', 'student', 'courses', ['course'], ['course_code'])
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.create_foreign_key('courses_ibfk_1', 'courses', 'colleges', ['resp_college'], ['college_code'])
    # ### end Alembic commands ###
