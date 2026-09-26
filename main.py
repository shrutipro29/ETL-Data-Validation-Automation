import pandas as pd
from database.db_connection import get_connection
from config.config import DB_CONFIG
from utils.logger import logger

logger.info("========== ETL VALIDATION STARTED ==========")

source_con = get_connection(DB_CONFIG["source_database"])
logger.info("Source database connected successfully")

target_con = get_connection(DB_CONFIG["target_database"])
logger.info("Target database connected successfully")

# # source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# # target_df = pd.read_sql("SELECT * FROM Policy", target_con)

# # print("Source Data")
# # print(source_df)
# # #first 5 rows
# # print(source_df.head())
# # #column names
# # print(source_df.columns)
# # #datatype
# # print(source_df.dtypes)
# # #number of rows
# # print(len(source_df))
# # #number of columns
# # print(source_df.shape)
# # #last 5 records
# # print(source_df.tail())
# # #print one column
# # print(source_df['premium'])


# # print("Target Data")
# # print(target_df)
# # #first 5 rows
# # print(target_df.head())
# # #column names
# # print(target_df.columns)
# # #datatype
# # print(target_df.dtypes)
# # #number of rows
# # print(len(target_df))
# # #number of columns
# # print(target_df.shape)
# # #last 5 records
# # print(target_df.tail())
# # #print one column
# # print(target_df['premium'])



# # source_con.close()
# # target_con.close()


# ## -------------------------------------------------------
# # # RECORD COUNT VALIDATION
# ## -------------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.record_count_validation import validate_record_count

# source_con = get_connection("insurance_source")
# print("source connected")

# target_con = get_connection("insurance_target")
# print("target connected")

source_df = pd.read_sql("SELECT * FROM Policy", source_con)
target_df = pd.read_sql("SELECT * FROM Policy", target_con)

print("SOURCE DATA")
print(source_df)

print("TARGET DATA")
print(target_df)

print()

logger.info("Starting record count validation")

count_val = validate_record_count(source_df, target_df)

logger.info(f"Record count validation result: {count_val}")

print(count_val)

source_con.close()
target_con.close()

# # #------------------------------------
# # # SCHEMA VALIDATION
# # #------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.schema_validation import validate_schema

# source_con = get_connection("insurance_source")
# print("source connected")
# target_con = get_connection("insurance_target")
# print("target connected")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)

# print("SOURCE DATA")
# print(source_df)

# print("TARGET DATA")
# print(target_df)

schema_val = validate_schema(source_df, target_df)
# print(schema_val)

logger.info("========== SCHEMA VALIDATION ==========")
logger.info("Schema validation started")

schema_val = validate_schema(source_df, target_df)

logger.info(
    f"Schema validation status: {schema_val['status']}"
)

logger.info(
    f"Datatype match: {schema_val['datatype_match']}"
)

if not schema_val["datatype_match"]:
    logger.warning(
        f"Datatype mismatches: {schema_val['datatype_mismatch']}"
)

for key, value in schema_val.items():
    print(f"{key}:{value}")

# # # --------------------------------------------------
# # # PRIMARY KEY VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.primary_key_validation import primary_key_validation

# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

result = primary_key_validation(source_df, target_df, "policy_number")
# # print(result)
# # print(type(result))

logger.info("========== PRIMARY KEY VALIDATION ==========")
logger.info("Primary key validation started")

result = primary_key_validation(
    source_df,
    target_df,
    "policy_number"
)

logger.info(
    f"Primary key validation status: {result['status']}"
)

logger.info(
    f"Missing records: {len(result['missing_records'])}"
)

logger.info(
    f"Extra records: {len(result['extra_records'])}"
)

for key, value in result.items():
    print(f"{key}:{value}")

# # # --------------------------------------------------
# # # FULL TABLE VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.full_table_validation import validate_full_table

# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

full_table_val_result = validate_full_table(source_df,target_df,"policy_number")

logger.info("========== FULL TABLE VALIDATION ==========")
logger.info("Full table validation started")

full_table_val_result = validate_full_table(
    source_df,
    target_df,
    "policy_number"
)

logger.info(
    f"Full table validation status: "
    f"{full_table_val_result['status']}"
)

logger.info(
    f"Total mismatches: "
    f"{full_table_val_result['total_mismatches']}"
)

for key, value in full_table_val_result.items():
    print(f"{key}:{value}")

# # # --------------------------------------------------
# # # SELECTED COLUMN TABLE VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.selected_column_validation import selected_column_validation
# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

selected_columns = [
    "premium",
    "policy_status"
]

selected_column_val_result = selected_column_validation(source_df,target_df,"policy_number",selected_columns)

logger.info("========== SELECTED COLUMN VALIDATION ==========")
logger.info("Selected column validation started")

selected_column_val_result = selected_column_validation(
    source_df,
    target_df,
    "policy_number",
    selected_columns
)

logger.info(
    f"Selected column validation status: "
    f"{selected_column_val_result['status']}"
)

logger.info(
    f"Selected column mismatches: "
    f"{selected_column_val_result['mismatch_count']}"
)

for key, value in selected_column_val_result.items():
    print(f"{key}:{value}")

# # # --------------------------------------------------
# # # INDIVIDUAL COLUMN NULL VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.individual_null_validation import individual_null_validation


# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

# print()

columns = [
    "driver_id",

    "premium",

    "policy_status"
]

individual_null_val_result_source = individual_null_validation(source_df,"Source Table","policy_number",columns)

logger.info("========== INDIVIDUAL NULL VALIDATION ==========")
logger.info("Source null validation started")

individual_null_val_result_source = individual_null_validation(
    source_df,
    "Source Table",
    "policy_number",
    columns
)

logger.info(
    f"Source null validation status: "
    f"{individual_null_val_result_source['status']}"
)

logger.info(
    f"Source null count: "
    f"{individual_null_val_result_source['null_count']}"
)

for key, value in individual_null_val_result_source.items():
    print(f"{key}:{value}")

individual_null_val_result_target = individual_null_validation(target_df,"Target Table","policy_number",columns)

logger.info("Target null validation started")

individual_null_val_result_target = individual_null_validation(
    target_df,
    "Target Table",
    "policy_number",
    columns
)

logger.info(
    f"Target null validation status: "
    f"{individual_null_val_result_target['status']}"
)

logger.info(
    f"Target null count: "
    f"{individual_null_val_result_target['null_count']}"
)

for key, value in individual_null_val_result_target.items():
    print(f"{key}:{value}")

# # # --------------------------------------------------
# # # COMPARATIVE NULL COLUMN VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.comparative_null_validation import comparative_null_validation


# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

# print()

# columns = [
#     "driver_id",

#     "premium",

#     "policy_status"
# ]

comp_null_val_result = comparative_null_validation(source_df,target_df,"policy_number",columns)

logger.info("========== COMPARATIVE NULL VALIDATION ==========")
logger.info("Comparative null validation started")

comp_null_val_result = comparative_null_validation(
    source_df,
    target_df,
    "policy_number",
    columns
)

logger.info(
    f"Comparative null validation status: "
    f"{comp_null_val_result['status']}"
)

logger.info(
    f"Comparative null mismatches: "
    f"{comp_null_val_result['mismatch count']}"
)

for key, value in comp_null_val_result.items():
    print(f"{key}:{value}")


# # # --------------------------------------------------
# # # DUPLICATE VALIDATION
# # # --------------------------------------------------

# import pandas as pd
# from database.db_connection import get_connection
from validations.duplicate_validation import validate_duplicate


# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

# print()

# columns = [
#     "driver_id",

#     "premium",

#     "policy_status"
# ]

dup_val_result = validate_duplicate(source_df,"Source",columns)

logger.info("========== DUPLICATE VALIDATION ==========")
logger.info("Duplicate validation started")

dup_val_result = validate_duplicate(
    source_df,
    "Source",
    columns
)

logger.info(
    f"Duplicate validation status: "
    f"{dup_val_result['status']}"
)

logger.info(
    f"Duplicate count: "
    f"{dup_val_result['duplicate count']}"
)

for key, value in dup_val_result.items():
    print(f"{key}:{value}")

# # --------------------------------------------------
# # BUSINESS RULE VALIDATION
# # --------------------------------------------------

from validations.business_rule_validation import validate_business_rules
# import pandas as pd
# from database.db_connection import get_connection


# source_con = get_connection("insurance_source")
# print("source connceted")
# target_con = get_connection("insurance_target")
# print("target conncted")

# source_df = pd.read_sql("SELECT * FROM Policy", source_con)
# print("SOURCE DATA")
# print(source_df)
# target_df = pd.read_sql("SELECT * FROM Policy", target_con)
# print("TARGET DATA")
# print(target_df)

# print()

business_rule_result = validate_business_rules(

    source_df,

    target_df,

    "policy_number",

    "mapping/Business_Rules.xlsx"

)

logger.info("========== BUSINESS RULE VALIDATION ==========")
logger.info("Business rule validation started")

business_rule_result = validate_business_rules(
    source_df,
    target_df,
    "policy_number",
    "mapping/Business_Rules.xlsx"
)

logger.info(
    f"Business rule validation status: "
    f"{business_rule_result['status']}"
)

logger.info(
    f"Total business rules: "
    f"{business_rule_result['total_rules']}"
)

logger.info(
    f"Total business rule mismatches: "
    f"{business_rule_result['total_mismatches']}"
)

print("\n========== BUSINESS RULE VALIDATION ==========\n")

print(f"Validation : {business_rule_result['validation']}")

print(f"Status : {business_rule_result['status']}")

print(f"Total Rules : {business_rule_result['total_rules']}")

print(f"Total Mismatches : {business_rule_result['total_mismatches']}")

print()

#print every mismatch
for mismatch in business_rule_result["mismatches"]:

    print("--------------------------------")

    for key, value in mismatch.items():

        print(f"{key} : {value}")

# # --------------------------------------------------
# # GENERATE EXCEL REPORT
# # --------------------------------------------------

from reports.report_generator import generate_excel_report

validation_results = {

    "Record Count": count_val,

    "Schema Validation": schema_val,

    "Primary Key Validation": result,

    "Full Table Validation": full_table_val_result,

    "Selected Column Validation": selected_column_val_result,

    # "Individual Null Validation":[individual_null_val_result_source, individual_null_val_result_target],
    "Individual Null - Source": individual_null_val_result_source,

    "Individual Null - Target": individual_null_val_result_target,

    "Comparative Null Validation": comp_null_val_result,

    "Duplicate Validation": dup_val_result,

    "Business Rule Validation": business_rule_result

}

logger.info("Generating Excel validation report")

generate_excel_report(
    report_path="reports/Validation_Report.xlsx",
    validation_results=validation_results
)

logger.info("Excel validation report generated successfully")

print("\n===========================================")
print(" ETL Validation Report Generated Successfully ")
print("===========================================")
print("Location : reports/Validation_Report.xlsx")

logger.info("========== ETL VALIDATION COMPLETED ==========")









