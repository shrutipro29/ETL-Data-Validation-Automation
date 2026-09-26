from validations.primary_key_validation import primary_key_validation


def test_primary_key_validation(source_df, target_df):

    result = primary_key_validation(
        source_df,
        target_df,
        "policy_number"
    )

    assert result["status"] == "PASS"
    assert result["missing_records"] == []
    assert result["extra_records"] == []