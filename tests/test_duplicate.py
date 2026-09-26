from validations.duplicate_validation import validate_duplicate


def test_duplicate_validation(source_df):

    columns = [
        "policy_number"
    ]

    result = validate_duplicate(
        source_df,
        "Source",
        columns
    )

    assert result["status"] == "PASS"
    assert result["duplicate count"] == 0