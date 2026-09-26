from validations.individual_null_validation import individual_null_validation


def test_target_null_validation(
    target_df
):

    columns = [
        "driver_id",
        "vehicle_id",
        "policy_status",
        "premium",
        "effective_date",
        "expiry_date"
    ]

    result = individual_null_validation(
        target_df,
        "Target Table",
        "policy_number",
        columns
    )

    assert result["status"] == "FAIL"
    assert result["null_count"] == 3