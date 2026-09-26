def validate_record_count(source_df, target_df):
    """
    Compare the number of records in source and target dataframe.
    """

    source_count = len(source_df)
    target_count = len(target_df)

    result = {
        "validation": "Record Count Validation",
        "source_count": source_count,
        "target_count": target_count,
        "status": "PASS" if source_count == target_count else "FAIL"
    }

    return result