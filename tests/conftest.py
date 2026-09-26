import pytest
import pandas as pd

from database.db_connection import get_connection
from config.config import DB_CONFIG


@pytest.fixture
def source_df():

    connection = get_connection(
        DB_CONFIG["source_database"]
    )

    df = pd.read_sql(
        "SELECT * FROM Policy",
        connection
    )

    connection.close()

    return df


@pytest.fixture
def target_df():

    connection = get_connection(
        DB_CONFIG["target_database"]
    )

    df = pd.read_sql(
        "SELECT * FROM Policy",
        connection
    )

    connection.close()

    return df