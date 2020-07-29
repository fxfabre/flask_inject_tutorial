#!/usr/bin/env python3

from .containers import ApplicationContainer


def create_app():
    """Create and return Flask application."""
    container = ApplicationContainer()
    container.config.from_yaml('config.yml')
    container.config.github.auth_token.from_env('GITHUB_TOKEN')

    app = container.app()
    app.container = container

    bootstrap = container.bootstrap()
    bootstrap.init_app(app)

    app.add_url_rule('/', view_func=container.index_view.as_view())

    return app
