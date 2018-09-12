from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.DataPipelineExecutionRepository import DataPipelineExecutionRepository
from modules.BaseObject import BaseObject


class BaseCommand(BaseObject):
    def __init__(self, db_connection_string, logger=None):
        super().__init__(logger)
        self.db_engine = create_engine(db_connection_string, echo=False)
        self.session_maker = sessionmaker(bind=self.db_engine)
        self.repository = DataPipelineExecutionRepository(self.session_maker)
        self.repository.create_schema(engine=self.db_engine)
