from validations.schema_validation import validate_schema


def test_schema_validation(source_df, target_df):

    result = validate_schema(
        source_df,
        target_df
    )

    assert result["status"] == "PASS"