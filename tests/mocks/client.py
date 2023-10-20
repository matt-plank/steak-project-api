from unittest import mock

from .databases import steak_project_database_mock

client_mock = mock.Mock()
client_mock.return_value.steak_project = steak_project_database_mock
