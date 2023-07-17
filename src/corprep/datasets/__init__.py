from typing import Optional

from hyfi.task import TaskConfig
from hyfi.utils.logging import LOGGING

logger = LOGGING.getLogger(__name__)


class DatasetsTask(TaskConfig):
    _config_name_ = "datasets"
