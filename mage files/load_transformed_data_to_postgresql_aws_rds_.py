from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    
    """
    town_internet=df[0]
    town_places=df[1]
    town_walk_scores=df[2]
    town_work_spaces=df[3]



    schema_name = 'public'  # Specify the name of the schema to export data to
    #table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    table_names=['demographics','internet_speed','walkability_scores','coworking_spaces']
    dfs=[town_places,town_internet,town_walk_scores,town_work_spaces]

    for table_name,df in zip(table_names,dfs):

        with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            loader.export(
                df,
                schema_name,
                table_name,
                index=False,  # Specifies whether to include index in exported table
                if_exists='replace',  # Specify resolution policy if table name already exists
            )


