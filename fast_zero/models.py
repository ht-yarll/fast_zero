from datetime import datetime

from sqlalchemy.orm import registry, Mapped, mapped_column


table_registry = registry()

@table_registry.mapped_as_dataclass                     #define as dataclass
class User:
    __tablename__ = 'users'                             #nome da tabela no banco

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime]