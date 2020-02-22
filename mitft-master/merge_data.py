import os
import pandas as pd
from Code.General_Utils import *

# Find the current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Assign Directories
directories=get_directory_paths(dir_path)

# Pull Data In
loss_file=directories['data']+'Hiscox_MITChallenge_LossData.csv'
submission_file=directories['data']+'Hiscox_MITChallenge_SubmissionData.csv'
date_diff_file=directories['data']+'DateDiff_Received_Quoted.csv'
out_file=directories['data']+'clean_full.csv'
bound_out_file=directories['data']+'bound_data.csv'
quoted_out_file=directories['data']+'quoted_data.csv'

# Assign Directories
directories=get_directory_paths(dir_path)

# Get in data
loss_data=pd.read_csv(loss_file, encoding='windows-1252')
submission_data=pd.read_csv(submission_file, encoding='windows-1252')
date_diff_data=pd.read_csv(date_diff_file)

# Clean Loss Data
def p2f(x):
    return float(x.strip('%'))/100
loss_data['Gross Earned Loss Ratio']=loss_data['Gross Earned Loss Ratio'].apply(p2f)
loss_data['Retention % ($)']=loss_data['Retention % ($)'].apply(p2f)

# Merge data
clean_data=pd.merge(submission_data, loss_data, how='left', on=['Product', 'Industry'])
out_data=pd.merge(clean_data, date_diff_data, how='left', left_on=['SubmissionID'], right_on=['submission_id'])
out_data=out_data.drop(['submission_id'], axis=1)

# Make adjustments and filter
out_data['revenue_error_flag']=1
out_data.loc[out_data['Revenue']>10000, 'revenue_error_flag']=0
out_data['date_diff_error_flag']=1
out_data.loc[out_data['Datediff_Recieved_Quoted']>=0, 'date_diff_error_flag']=0
bound_data=out_data.loc[out_data['BoundFlag']==1]
quoted_data=out_data.loc[out_data['QuotedFlag']==1]

write=write_data(out_data, out_file)
write=write_data(bound_data, bound_out_file)
write=write_data(quoted_data, quoted_out_file)
