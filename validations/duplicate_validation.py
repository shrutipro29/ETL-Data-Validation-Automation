def validate_duplicate(dataframe,tablename,columns):

    duplicate_records = []

    duplicate_rows = dataframe[dataframe.duplicated(subset=columns,keep=False)]

    for _,row in duplicate_rows.iterrows():
        duplicate_records.append({
            "tablename":tablename,
            "Duplicate Values":{
                column:row[column]
                for column in columns
            }
        })

    status = "PASS" if len(duplicate_records)==0 else "FAIL"

    result = {
        "validation": "Duplicate Validation",
        "status":status,
        "duplicate_records":duplicate_records,
        "duplicate count": len(duplicate_records)
    }

    return result

