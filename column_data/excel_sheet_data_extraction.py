# This program needs pandas and openpyxl Python libraries installed to run.
# Sample data from Tags column
# costcenter:123.4505.87678, env:prd, compliance:none, appid:7896, dataclass:restricted, businessunit:cbu, appname:channel_it_system_of_enablement_layer, appowner:somebody@gmail.com, pii:true, appclass:vital, canumber:23it198547, otl:567907, sharedservices:no, triageticket:cps-9945

import pandas as pd

# Read the Excel file
df = pd.read_excel("C:\\Users\\sriram\\Desktop\\Tags.xlsx")

# Function to extract values from the "Tags" column
def extract_info(tags):
    app_id = ""
    app_owner = ""
    for tag in tags.split(", "):
        if tag.startswith("appid:"):
            app_id = tag.split(":")[1]
        elif tag.startswith("appowner:"):
            app_owner = tag.split(":")[1]
    return app_id, app_owner

# Apply the function to the "Tags" column and create new columns
df[['AppId', 'AppOwner']] = df['Tags'].apply(lambda x: pd.Series(extract_info(x)))

# Save the result to a new Excel file
df.to_excel("C:\\Users\\sriram\\Desktop\\Output_extracted.xlsx", index=False)
