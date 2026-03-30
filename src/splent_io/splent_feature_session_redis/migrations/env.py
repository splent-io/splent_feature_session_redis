"""Alembic migration environment for splent_feature_session_redis."""

from splent_io.splent_feature_session_redis import models  # noqa
from splent_framework.migrations.feature_env import run_feature_migrations

FEATURE_NAME = "splent_feature_session_redis"
FEATURE_TABLES = set()

run_feature_migrations(FEATURE_NAME, FEATURE_TABLES)
