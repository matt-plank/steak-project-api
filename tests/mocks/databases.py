from unittest import mock

from .collections import measurements_collection_mock

steak_project_database_mock = mock.Mock()
steak_project_database_mock.measurements = measurements_collection_mock
