def validate_schema(source_df,target_df):

    #----------------------------
    # Column Count Validation
    #----------------------------

    source_column_count = source_df.shape[1]
    target_column_count = target_df.shape[1]

    column_count_match = (
        source_column_count == target_column_count
    )

    #----------------------------
    # Column Name Validation
    #----------------------------

    source_columns = list(source_df.columns)
    target_columns = list(target_df.columns)

    column_name_match = (
        set(source_columns) == set(target_columns)
    )

    #-----------------------------------
    # Data Type Validation
    #-----------------------------------

    datatype_match = True
    datatype_mismatches = {}

    #compare only common columns
    common_columns = set(source_columns).intersection(set(target_columns))

    for column in common_columns:
        source_dtype = source_df[column].dtype
        target_dtype = target_df[column].dtype

        if source_dtype != target_dtype:
            datatype_match = False
            datatype_mismatches[column]= {
                "source": str(source_dtype),
                "target": str(target_dtype)
            }

    #----------------------------------------------------
    # Overall Result
    #----------------------------------------------------

    if(column_count_match and column_name_match and datatype_match):
        status = "PASS"
    else:
        status = "FAIL"


    #-----------------------------------------------------
    # Return Result
    #-----------------------------------------------------

    result = {
        "validation": "schema validation",
        "source_column_count": source_column_count,
        "target_column_count": target_column_count,
        "column_count_match": column_count_match,
        "column_name_match": column_name_match,
        "datatype_match": datatype_match,
        "datatype_mismatch": datatype_mismatches,
        "status":status
        
        }
    return result




