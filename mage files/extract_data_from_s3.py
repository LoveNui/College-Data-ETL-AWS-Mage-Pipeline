from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from os import path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_s3_bucket(*args, **kwargs):
    """
    Template for loading data from a S3 bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#s3
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    bucket_name = 'college-towns-bucket'
    object_keys = ['data/us_college_towns.csv', 'data/us_towns_internet_full.csv',
                    'data/best_places.csv','data/walk_score_.csv',
                    'data/city_feet_coworking_space.csv']
    
    s3_client = S3.with_config(ConfigFileLoader(config_path, config_profile))
    data_frames = []
    
    for object_key in object_keys:
        df = s3_client.load(bucket_name, object_key)
        data_frames.append(df)
    
    return data_frames


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # Add additional assertions or checks as needed


