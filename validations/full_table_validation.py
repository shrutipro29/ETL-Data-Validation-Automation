def validate_full_table(source_df,target_df, primary_key):

    mismatches = []


    # convert dataframe to dictionary using prirmary key
    source_dict = source_df.set_index(primary_key).to_dict("index")
    target_dict = target_df.set_index(primary_key).to_dict("index")

    #compare only the records that exists in both table
    common_keys = set(source_dict.keys()).intersection(set(target_dict.keys()))

    for key in common_keys:

        source_row = source_dict[key]
        target_row = target_dict[key]

        for column in source_row:

            source_value = source_row[column]
            target_value = target_row[column]

            # Handling Nan Values
            if (source_value != source_value
                and 
                target_value != target_value): continue
            
            if source_value!= target_value:
                mismatches.append({
                    "key":key,
                    "Column": column,
                    "source_value":source_value,
                    "target_value":target_value

                })

    status = "PASS" if len(mismatches) == 0 else "FAIL"

    result = {
        "Validdation": "Full Table Validation",
        "total_mismatches":len(mismatches),
        "mismatches":mismatches,
        "status": status
    }

    return result

