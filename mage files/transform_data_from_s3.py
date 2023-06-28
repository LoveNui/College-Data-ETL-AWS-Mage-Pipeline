if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(data_frames, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block (if applicable)
        args: The output from any additional upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    town_names=data_frames[0]
    town_internet=data_frames[1]
    town_places=data_frames[2]
    town_walk_scores=data_frames[3]
    town_work_spaces=data_frames[4]
    #town_internet
    town_internet['college_towns']=town_internet.apply(lambda row: row['town_name'] + ', ' + row['state_name'], axis=1)
    #replace state in town_places with full name instead of abbrevations
    # Create a dictionary of state abbreviations and full names
    state_dict = {'AL': 'Alabama','AK': 'Alaska','AZ': 'Arizona','AR': 'Arkansas','CA': 'California','CO': 'Colorado',
            'CT': 'Connecticut','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','ID': 'Idaho',
            'IL': 'Illinois','IN': 'Indiana','IA': 'Iowa','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana',
            'ME': 'Maine','MD': 'Maryland','MA': 'Massachusetts','MI': 'Michigan','MN': 'Minnesota','MS': 'Mississippi',
            'MO': 'Missouri','MT': 'Montana','NE': 'Nebraska','NV': 'Nevada','NH': 'New Hampshire','NJ': 'New Jersey',
            'NM': 'New Mexico','NY': 'New York','NC': 'North Carolina','ND': 'North Dakota','OH': 'Ohio','OK': 'Oklahoma',
            'OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota',
            'TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VT': 'Vermont','VA': 'Virginia','WA': 'Washington',
            'WV': 'West Virginia','WI': 'Wisconsin','WY': 'Wyoming'}

    # Replace state abbreviations with full names
    town_places['state'] = town_places['state'].replace(state_dict)
    #create new column for town_places to use as key for joining
    town_places['college_towns']=town_places.apply(lambda row: row['name'] + ', ' + row['state'], axis=1)
    town_places['cost_of_living']=(town_places['cost_of_living'].str.split('%').str.get(0))
    town_places['cost_of_living']=town_places['cost_of_living'].astype('float')+100
    #rename cost of living column
    town_places.rename(columns={'cost_of_living':'cost_of_living_index'},inplace=True)

    #to create college town column:
    town_work_spaces['state']=town_work_spaces['town_name'].str.split(',').str.get(1)
    town_work_spaces['town']=town_work_spaces['town_name'].str.split(',').str.get(0)
    # Replace state abbreviations with full names
    town_work_spaces['state']=town_work_spaces['state'].str.strip()
    town_work_spaces['state'] = town_work_spaces['state'].replace(state_dict)
    #create new column for town_internet to use as key for joining
    town_work_spaces['college_towns']=town_work_spaces.apply(lambda row: row['town'] + ', ' + row['state'], axis=1)

    #join town_walk_scores and town_work_spaces
    town_walk_and_work_spaces=town_work_spaces.merge(town_walk_scores,left_on='town_name',right_on='town_name',how='inner')
    #join town_places and town_internet
    town_places['unemployment_rate']=(town_places['unemployment_rate'].str.split('%').str.get(0).str.strip()).astype('float')
    town_places_and_internet=town_places.merge(town_internet,left_on='college_towns',right_on='college_towns',how='inner')

    #join town_places_and_internet and town_walk_and_work_spaces
    town_info_combined=town_places_and_internet.merge(town_walk_and_work_spaces,left_on='college_towns',
                                            right_on='college_towns',how='inner')

    town_data=town_info_combined[['population', 'unemployment_rate', 'median_income',
       'median_age', 'cost_of_living_index', 'college_towns','median_download_speed', 'median_upload_speed',
       'median_latency', 'num_coworking_space','walk_score', 'bike_score', 'num_eateries']]

    #remove comma in population column
    town_data['population']=town_data['population'].str.replace(',','')
    #remove dollar and comma in median income column
    town_data['median_income']=town_data['median_income'].str.strip('$').str.replace(',','').str.strip()
    town_data['num_eateries']=town_data['num_eateries'].str.replace(',','')
    #change necessary data type
    town_data['population']=town_data['population'].astype('int')
    town_data['median_income']=town_data['median_income'].astype('float')
    town_data['num_eateries']=town_data['num_eateries'].astype('int')

    town_data.drop_duplicates(inplace=True)
    town_data.reset_index(drop=False,inplace=True)

    #split data back into individual datasets
    town_internet=town_data[['median_download_speed','median_upload_speed', 'median_latency', 'college_towns']]

    town_places=town_data[['population', 'unemployment_rate', 'median_income','median_age', 'cost_of_living_index', 'college_towns']]

    town_walk_scores=town_data[['walk_score', 'bike_score', 'num_eateries', 'college_towns']]

    town_work_spaces=town_data[['num_coworking_space', 'college_towns']]

    #final cleaning step:
    #town_internet
    town_internet['town_id'] = range(1, len(town_internet) + 1)
    town_internet = town_internet[['town_id', 'college_towns', 'median_download_speed', 'median_upload_speed', 'median_latency']]

    # town_places
    town_places = town_places[['college_towns', 'population', 'unemployment_rate', 'median_income',
                           'median_age', 'cost_of_living_index']]
   

    # town_walk_scores
    town_walk_scores['walkability_id'] = range(1, len(town_walk_scores) + 1)
    town_walk_scores.rename(columns={'college_towns':'college_town'},inplace=True)
    town_walk_scores = town_walk_scores[['walkability_id', 'college_town', 'walk_score', 'bike_score', 'num_eateries']]

    # town_work_spaces
    town_work_spaces['coworking_spaces_id'] = range(1, len(town_work_spaces) + 1)
    town_work_spaces = town_work_spaces[['coworking_spaces_id', 'college_towns', 'num_coworking_space']]
    #replace 0 values in num_coworking_space to median value
    town_work_spaces['num_coworking_space']=town_work_spaces['num_coworking_space'].replace(0,(town_work_spaces['num_coworking_space'].median()))



    return [town_internet,town_places,town_walk_scores,town_work_spaces]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
