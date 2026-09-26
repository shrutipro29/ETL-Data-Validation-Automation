from validations.selected_column_validation import selected_column_validation


def test_selected_column_detects_mismatches(
    source_df,
    target_df
):

    selected_columns = [
        "premium",
        "policy_status"
    ]

    result = selected_column_validation(
        source_df,
        target_df,
        "policy_number",
        selected_columns
    )

    assert result["status"] == "FAIL"
    assert result["mismatch_count"] == 2