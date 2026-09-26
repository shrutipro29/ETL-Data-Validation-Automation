import pandas as pd

def validate_business_rules(
        source_df,
        target_df,
        primary_key,
        excel_path
):

    # Read Excel Mapping
    rules_df = pd.read_excel(
        excel_path,
        sheet_name="BusinessRules"
    )

    # Convert tables into dictionaries
    source_dict = source_df.set_index(primary_key).to_dict("index")
    target_dict = target_df.set_index(primary_key).to_dict("index")

    common_keys = (
        set(source_dict.keys())
        &
        set(target_dict.keys())
    )

    mismatches = []

    # Compare every common record
    for key in common_keys:

        source_row = source_dict[key]
        target_row = target_dict[key]

        # Execute every active rule
        for _, rule in rules_df.iterrows():

            if str(rule["Active"]).upper() != "Y":
                continue

            variables = source_row.copy()

            try:

                expected_value = eval(
                    rule["Rule_Expression"],
                    {},
                    variables
                )

                actual_value = target_row[
                    rule["Target_Column"]
                ]

                if expected_value != actual_value:

                    mismatches.append({

                        "Rule ID": rule["Rule_ID"],

                        "Rule Name": rule["Rule_Name"],

                        "Primary Key": key,

                        "Target Column": rule["Target_Column"],

                        "Rule": rule["Rule_Expression"],

                        "Expected": expected_value,

                        "Actual": actual_value

                    })

            except Exception as error:

                mismatches.append({

                    "Rule ID": rule["Rule_ID"],

                    "Rule Name": rule["Rule_Name"],

                    "Primary Key": key,

                    "Target Column": rule["Target_Column"],

                    "Rule": rule["Rule_Expression"],

                    "Error": str(error)

                })

    status = (
        "PASS"
        if len(mismatches) == 0
        else "FAIL"
    )

    return {

        "validation": "Business Rule Validation",

        "total_rules": len(rules_df),

        "total_mismatches": len(mismatches),

        "mismatches": mismatches,

        "status": status

    }