import pandas as pd


def write_to_file(filename:str, query_list:list):
    # query_tuple.append([index, query_id, query_title, query_string2])

    with open(filename, "w", encoding="utf-8") as fob:
        for item in query_list:
            fob.write("=======================================================================================\n")
            fob.write("=======================================================================================\n")
            fob.write("QUERY_NO: " + str(item[0]) + "\n")
            fob.write("QUERY_ID: " + str(item[1]) + "\n")
            fob.write("QUERY_TITLE: " + str(item[2]) + "\n\n")
            fob.write("QUERY_STRING:\n\n")
            fob.write(item[3] + "\n\n\n\n")


if __name__ == "__main__":

    # change names=range(n) to whatever the maximum fields you encounter via pandas exception msgs..
    df = pd.read_csv("download-my-queries.csv", header=None, names=range(100000), low_memory=False)

    print(df)

    query_tuple = []

    for index, row in df.iterrows():
        print("Current Row:", index)

        if index == 0:
            continue

        item_counter = 0
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
                item_counter += 1
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
        '''
        The below substring replacement operations will have to be fine-tuned as per User SQL writing style
            - query_string1/query_string2 should beautify shit enough to be readable/legible...
            - Probably needs regex based substitutions and not hardcoded substitutions as done here!
            - DO KEEP IN MIND: each replacement/sub step changes the string! so the order in which subs are done MATTERS
        '''
        query_string1 = query_string.replace("   ", "\n\t")
        query_string2 = query_string1.replace(" 	", "\n\t")
        query_string3 = query_string2.replace("UNION ALL", "\n\tUNION ALL\n")
        print("INDEX: ", index, " ID:", query_id, " TITLE: ", query_title, "\nQUERY_STRING:\n", query_string2)

        query_tuple.append([index, query_id, query_title, query_string2])

    write_to_file("query_collection.txt", query_tuple)



