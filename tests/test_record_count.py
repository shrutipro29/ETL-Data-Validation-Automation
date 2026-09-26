from validations.record_count_validation import validate_record_count


def test_record_count(source_df, target_df):

    result = validate_record_count(
        source_df,
        target_df
    )

    assert result["status"] == "PASS"