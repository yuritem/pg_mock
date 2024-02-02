from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    pg_username: str
    pg_password: str
    pg_host: str
    pg_port: str
    pg_database: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding="utf-8", case_sensitive=False)

    def build_postgres_dsn(self, db_name: str = None) -> str:
        db = db_name or self.pg_database
        return f"postgresql://{self.pg_username}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{db}"
