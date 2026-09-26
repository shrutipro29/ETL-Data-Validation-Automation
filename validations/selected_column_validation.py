def selected_column_validation(source_df,target_df,primary_key,selected_column):
    mismatches =[]

    #compare dataframe to dictionary
    source_dict = source_df.set_index(primary_key).to_dict("index")
    target_dict = target_df.set_index(primary_key).to_dict("index")

    #common keys
    common_keys = set(source_dict.keys()).intersection(set(target_dict.keys()))

    for key in common_keys:
         source_row = source_dict[key]
         target_row = target_dict[key]

         for column in selected_column:
              
              source_value = source_row[column]
              target_value = target_row[column]

              # handling NaN values
              if(source_value!=source_value
                 and
                 target_value!=target_value): continue
              
              if source_value!=target_value:
                   mismatches.append({
                        "Key": key,
                        "column": column,
                        "Source Value": source_value,
                        "Target Value": target_value

                   })

    status = "PASS" if len(mismatches) == 0 else "FAIL"

    result = {
    "validation": "Selected Column Validation",
    "mismatch_count": len(mismatches),
    "mismatches": mismatches,
    "status": status
    }

    return result
                   


