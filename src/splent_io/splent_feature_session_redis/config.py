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

    # Isolate sessions per product. Two products served from the same host
    # (e.g. localhost on different ports) share cookies, and a shared Redis
    # store would otherwise mix their sessions. A per-product key prefix and
    # cookie name keep them fully separate.
    product = os.getenv("SPLENT_APP") or app.import_name.split(".")[0]

    app.config.update(
        {
            "SESSION_TYPE": "redis",
            "SESSION_PERMANENT": False,
            "SESSION_REDIS": redis.from_url(redis_url),
            "SESSION_KEY_PREFIX": f"{product}:",
            "SESSION_COOKIE_NAME": f"{product}_session",
        }
    )
