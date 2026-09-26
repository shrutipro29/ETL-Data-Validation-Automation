from validations.full_table_validation import validate_full_table


def test_full_table_detects_mismatches(source_df, target_df):

    result = validate_full_table(
        source_df,
        target_df,
        "policy_number"
    )

    assert result["status"] == "FAIL"
    assert result["total_mismatches"] == 4