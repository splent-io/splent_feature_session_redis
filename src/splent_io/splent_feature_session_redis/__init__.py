from splent_framework.blueprints.base_blueprint import BaseBlueprint

session_redis_bp = BaseBlueprint("session_redis", __name__, template_folder="templates")


def init_feature(app):
    from splent_io.splent_feature_session_redis.config import inject_config

    inject_config(app)


def inject_context_vars(app):
    return {}
