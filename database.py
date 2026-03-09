from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text
from flask_login import UserMixin


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)


class ImageMetadata(db.Model):
    __tablename__ = "image_metadata"

    id = db.Column(db.Integer, primary_key=True)
    original_filename = db.Column(db.String(255), nullable=False)
    blob_name = db.Column(db.String(255), nullable=False, unique=True)
    blob_url = db.Column(db.String(1024), nullable=False)
    container_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    user = db.relationship("User", backref="files")

    file_format = db.Column(db.String(20), nullable=False)
    file_size_bytes = db.Column(db.Integer, nullable=False)
    original_size_kb = db.Column(db.Float, nullable=True)
    processed_size_kb = db.Column(db.Float, nullable=True)

    resize_applied = db.Column(db.Boolean, nullable=False, default=False)
    compress_applied = db.Column(db.Boolean, nullable=False, default=False)
    compression_level = db.Column(db.String(20), nullable=True)
    download_count = db.Column(db.Integer, nullable=False, default=0)
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)

    uploaded_at = db.Column(db.DateTime, nullable=False)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        _ensure_columns()
        migrate_database()


def _ensure_columns():
    """Add newly introduced columns for existing deployments."""
    engine = db.engine
    dialect = engine.dialect.name
    inspector = inspect(engine)
    existing_columns = {col["name"] for col in inspector.get_columns("image_metadata")}

    columns_to_add = {
        "original_size_kb": "FLOAT",
        "processed_size_kb": "FLOAT",
        "compression_level": "VARCHAR(20)",
        "download_count": "INTEGER DEFAULT 0",
    }

    with engine.begin() as connection:
        for column_name, column_type in columns_to_add.items():
            if column_name not in existing_columns:
                # SQL Server uses "ADD <column>", while SQLite/MySQL/Postgres accept "ADD COLUMN <column>".
                add_keyword = "ADD" if dialect.startswith("mssql") else "ADD COLUMN"
                connection.execute(
                    text(f"ALTER TABLE image_metadata {add_keyword} {column_name} {column_type} NULL")
                )


def migrate_database():
    """Compatibility migration for legacy deployments."""
    inspector = inspect(db.engine)
    table_names = set(inspector.get_table_names())

    def _add_column_if_missing(table_name, column_name, column_sql):
        columns = {c["name"] for c in inspector.get_columns(table_name)}
        if column_name in columns:
            return
        dialect = db.engine.dialect.name
        add_keyword = "ADD" if dialect.startswith("mssql") else "ADD COLUMN"
        with db.engine.begin() as connection:
            connection.execute(
                text(f"ALTER TABLE {table_name} {add_keyword} {column_name} {column_sql}")
            )

    # Existing project table.
    if "image_metadata" in table_names:
        _add_column_if_missing("image_metadata", "user_id", "INTEGER NULL")

    # Fallback for requested legacy naming.
    if "upload_file" in table_names:
        _add_column_if_missing("upload_file", "user_id", "INTEGER NULL")
