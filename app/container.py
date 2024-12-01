from contextlib import contextmanager
from typing import Optional

from db import PostgreSQL
from dependency_injector import containers, providers
from sqlalchemy import Engine
from repositories.book_repository import BookRepository
from services.book_service import BookService
from controllers.book_controller import BookController

class DatabaseContainer(containers.DeclarativeContainer):
    posSQL = providers.Singleton(
        PostgreSQL, uri='postgresql://postgres:123456@localhost:5432/biblioteca'
    )

class ReporitoriesContainer(containers.DeclarativeContainer):
    databases : DatabaseContainer = providers.DependenciesContainer()
    book_repository = providers.Singleton(
        BookRepository, 
        session_factory = databases.posSQL.provided.session)
    

class ServicesContainer(containers.DeclarativeContainer):
    repositories: ReporitoriesContainer = providers.DependenciesContainer()
    book_service = providers.Factory(BookService,
                                     book_repository=repositories.book_repository)

class ControllersContainer(containers.DeclarativeContainer):
    services: ServicesContainer = providers.DependenciesContainer()
    book_controller = providers.Factory(BookController,
                                        book_service=services.book_service)

class BaseContainer(containers.DeclarativeContainer):
    databases = providers.Container(DatabaseContainer)
    repositories = providers.Container(
        ReporitoriesContainer, databases =databases
    )
    services = providers.Container(
        ServicesContainer, repositories = repositories
    )
    controllers = providers.Container(
        ControllersContainer, services = services
    )

class AppContainer:
    container: Optional[BaseContainer] = None

    @classmethod
    @contextmanager
    def scope(cls):
        try:
            cls.container.services.init_resources()
            yield cls.container
        finally:
            cls.container.services.shutdown_resources()

    @classmethod
    def init(cls) -> None:
        if cls.container is None:
            cls.container = BaseContainer()

    @classmethod
    def db_engine(cls) -> Engine:
        return cls.container.databases.posSQL().engine()
