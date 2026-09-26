import pandas as pd

def comparative_null_validation(source_df,target_df,primary_key,columns):

    mismatches=[]

    #convert df to dict
    source_dict = source_df.set_index(primary_key).to_dict("index")
    target_dict = target_df.set_index(primary_key).to_dict("index")

    #common keys
    common_keys = set(source_dict.keys()).intersection(set(target_dict.keys()))

    for key in common_keys:

        source_row = source_dict[key]
        target_row = target_dict[key]

        for column in columns:

# | Source Value | Target Value | source_null | target_null | Mismatch? |
# | ------------ | ------------ | ----------- | ----------- | --------- |
# | 12000        | 12000        | False       | False       | ❌ No      |
# | NULL         | NULL         | True        | True        | ❌ No      |
# | NULL         | 15000        | True        | False       | ✅ Yes     |
# | 12000        | NULL         | False       | True        | ✅ Yes     |


            source_value = source_row[column]
            target_value = target_row[column]

            # source_null = (source_value!=source_value)
            # target_null = (target_value!=target_value)
            source_null = pd.isna(source_value)
            target_null = pd.isna(target_value)

            if source_null!=target_null:
                mismatches.append({
                    "Source Value":source_value,
                    "Target Value": target_value,
                    "column": column,
                    "primary_key":key

                })

        
    status = "PASS" if len(mismatches) == 0 else "FAIL"

    result = {
        "validation":"COMPARATIVE NULL VALIDATION",
        "status": status,
        "mismatches": mismatches,
        "mismatch count":len(mismatches)

    }

    return result