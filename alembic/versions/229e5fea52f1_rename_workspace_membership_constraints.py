"""rename workspace membership constraints

Revision ID: 229e5fea52f1
Revises: 39684f8b8a78
Create Date: 2026-10-22 18:56:39.226569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '229e5fea52f1'
down_revision: Union[str, Sequence[str], None] = '39684f8b8a78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("workspace_member") as batch_op:
        batch_op.drop_constraint(
            "uq_workspace_member_user_workspce",
            type_="unique"
        )
        batch_op.create_unique_constraint(
            "uq_workspace_member_user_workspace",
            ["user_id", "workspace_id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("workspace_member") as batch_op:
        batch_op.drop_constraint(
            "uq_workspace_member_user_workspace",
            type_="unique"
        )
        batch_op.create_unique_constraint(
            "uq_workspace_member_user_workspce",
            ["user_id", "workspace_id"]
        )