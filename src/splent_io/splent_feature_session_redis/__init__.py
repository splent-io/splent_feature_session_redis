from splent_framework.blueprints.base_blueprint import create_blueprint

session_redis_bp = create_blueprint(__name__)


def init_feature(app):
    from splent_io.splent_feature_session_redis.config import inject_config

    inject_config(app)


def inject_context_vars(app):
    return {}
