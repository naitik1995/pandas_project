# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
print(type(ipl_df['bowler'] == 'I Sharma'))
def create_bowler_filter(bowler_name):
    return(ipl_df['bowler'] == bowler_name)
create_bowler_filter('I Sharma')    


