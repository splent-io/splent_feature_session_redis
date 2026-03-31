"""
Redis-backed session configuration.

Configures Flask-Session to use Redis as the session store.
Requires splent_feature_redis to be installed (provides REDIS_URL).
"""

import os
import redis


def inject_config(app):
    redis_url = app.config.get("REDIS_URL") or os.getenv(
        "REDIS_URL", "redis://redis:6379"
    )

    app.config.update(
        {
            "SESSION_TYPE": "redis",
            "SESSION_PERMANENT": False,
            "SESSION_REDIS": redis.from_url(redis_url),
        }
    )
