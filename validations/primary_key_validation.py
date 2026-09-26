def primary_key_validation(source_df,target_df, primary_key):

    missing_records = []
    extra_records = []

    source_key = set(source_df[primary_key])
    target_key = set(target_df[primary_key])

    # missing record 
    for key in source_key:

        if key not in target_key:

            missing_records.append(key)

    #extra record
    for key in target_key:

        if key not in source_key:

            extra_records.append(key)

    status = (
              "PASS" if len(missing_records)== 0 and len(extra_records) == 0
              else
                "FAIL")
    
    result = {
    "validation": "Primary Key Validation",
    "source_key": list(source_key),
    "target_key": list(target_key),
    "missing_records": missing_records,
    "extra_records": extra_records,
    "status": status
    }

    return result


