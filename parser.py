import pandas as pd

# change names=range(n) to whatever the maximum fields you encounter via pandas exception msgs..
df = pd.read_csv("download-my-queries.csv", header=None, names=range(19424), low_memory=False)

print(df)

lines = 0

for index, row in df.iterrows():
    print("Current Row:", index)

    if index==0:
        continue

    item_counter=0
    query_id = None
    query_title = None
    query_string = ""

    for col_name, value in row.items():

        if item_counter == 0:
            query_id = value
            item_counter += 1
            continue

        elif item_counter == 1:
            query_title = value
            item_counter +=1
            continue

        else:
            # print(col_name)
            if pd.isnull(value):
                break
            else:
                if query_string == "":
                    query_string = query_string + str(value)
                else:
                    query_string = query_string + "," + str(value)

    print("INDEX: ", index, " ID:", query_id, " TITLE: ", query_title, " QUERY_STRING: ", query_string)

'''
NEXT STEP(s):
    - OUTPUT each csv row into a beautiful/formatted/readable textfile
    - Attempt to format the only space/no whitespace type info sql string into actual SQL-formatted string...
    
    SAMPLE:
        ===============================================
        ===============================================
        QUERY_ID: <query_id>
        QUERY_TITLE: <query_title>
        QUERY_STRING:
        <query_string>
        
        
        ===============================================
        ===============================================
        QUERY_ID: <query_id>
        QUERY_TITLE: <query_title>
        QUERY_STRING:
        <query_string>
'''


