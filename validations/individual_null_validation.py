def individual_null_validation(dataframe,table_name, primary_key, columns):

    null_records = []

    for column in columns:

        null_rows = dataframe[dataframe[column].isna()]

# iterrows() means:

# "Go through each row one by one."

# Each iteration returns two things:

# 1. Index
# 2. Row

# The underscore (_) means:

# "I'm receiving this value, but I'm not going to use it."

# So

# for _, row in null_rows.iterrows():

# is exactly the same as

# for index, row in null_rows.iterrows():

# except we're ignoring the index.

        for _,row in null_rows.iterrows():

            null_records.append({
                "value":row[column],
                "column":column,
                "primary_key": row[primary_key]
            })

    status = "PASS" if len(null_records)==0 else "FAIL"
    
    result = {

    "validation": "Individual Null Validation",

    "status": status,

    "table_name": table_name,

    "null_records": null_records,

    "null_count": len(null_records)
    }

    return result

