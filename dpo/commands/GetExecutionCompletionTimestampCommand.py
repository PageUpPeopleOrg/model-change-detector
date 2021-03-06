from dpo.commands.BaseCommand import BaseCommand
from dpo.Shared import Constants


class GetExecutionCompletionTimestampCommand(BaseCommand):
    def __init__(self, db_connection_string, execution_id, logger=None):
        super().__init__(db_connection_string, logger)
        self._execution_id = execution_id

    def execute(self):
        if self._execution_id == Constants.NO_LAST_SUCCESSFUL_EXECUTION:
            self.logger.debug('Received no execution id, so returning current database datetime with timezone')
            self.output(self.repository.get_current_db_datetime_with_timezone())
            return

        data_pipeline_execution = self.repository.get_execution(self._execution_id)
        if data_pipeline_execution is None:
            raise ValueError(self._execution_id)
        self.output(data_pipeline_execution.completed_on)
        return

    def output(self, timestamp):
        print(timestamp.isoformat() if timestamp is not None else '')
