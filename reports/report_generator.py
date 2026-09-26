import pandas as pd

def generate_excel_report(report_path, validation_results):

    with pd.ExcelWriter(report_path, engine="openpyxl") as writer:

        # ==========================
        # Summary Sheet
        # ==========================

        summary = []

        for validation_name, result in validation_results.items():

            summary.append({

                "Validation": validation_name,

                "Status": result.get("status", "N/A")

            })

        summary_df = pd.DataFrame(summary)

        summary_df.to_excel(

            writer,

            sheet_name="Summary",

            index=False

        )

        # ==========================
        # Detail Sheets
        # ==========================

        for validation_name, result in validation_results.items():

            detail_df = None

            # ---------- Full Table / Business Rule / Comparative Null ----------
            if "mismatches" in result:

                detail_df = pd.DataFrame(result["mismatches"])

            # ---------- Selected Column Validation ----------
            elif "Mismatch" in result:

                detail_df = pd.DataFrame(result["Mismatch"])

            # ---------- Individual Null ----------

            # elif "Null Records" in result:

            #     detail_df = pd.DataFrame(result["Null Records"])

            # elif "null_records" in result:

            #     detail_df = pd.DataFrame(result["null_records"])

            elif "null_records" in result:

                null_summary = pd.DataFrame([
                    {
                        "Validation": "Individual Null Validation",
                        "Table": result["table_name"],
                        "Null Count": result["null_count"],
                        "Status": result["status"]
                    }
                ])

                if result["null_records"]:

                    null_details = pd.DataFrame(result["null_records"])

                else:

                    null_details = pd.DataFrame({
                        "Message": ["No NULL records found"]
                    })

                null_summary.to_excel(
                    writer,
                    sheet_name=validation_name[:31],
                    index=False,
                    startrow=0
                )

                null_details.to_excel(
                    writer,
                    sheet_name=validation_name[:31],
                    index=False,
                    startrow=3
                )

                continue

            # ---------- Duplicate ----------
            elif "duplicate_records" in result:

                detail_df = pd.DataFrame(result["duplicate_records"])

            # ---------- Primary Key ----------
            elif "Missing Records" in result:

                detail_df = pd.DataFrame({

                    "Missing Records": result["Missing Records"],

                    "Extra Records": result["Extra Records"]

                })

            # ---------- Schema ----------
            elif "datatype_mismatch" in result:

                summary = pd.DataFrame([
                    {
                        "Validation": "Source Column Count",
                        "Result": result["source_column_count"]

                    },
                    {
                        "Validation": "Target Column Count",
                        "Result": result["target_column_count"]
                    },
                    {
                        "Validation": "Column Count Match",
                        "Result": result["column_count_match"]
                    },
                    {
                        "Validation": "Column Name Match",
                        "Result": result["column_name_match"]
                    },
                    {
                        "Validation": "Datatype Match",
                        "Result": result["datatype_match"]
                    },
                    {
                        "Validation": "Overall Status",
                        "Result": result["status"]
                    }
                ])

                mismatch_rows = []

                for column, datatype in result["datatype_mismatch"].items():
                    mismatch_rows.append({
                        "Column": column,
                        "Source Datatype": datatype["source"],
                        "Target Datatype": datatype["target"]
                    })

                mismatch_df = pd.DataFrame(mismatch_rows)

                summary.to_excel(
                    writer,
                    sheet_name=validation_name[:31],
                    index=False,
                    startrow=0
                )

                mismatch_df.to_excel(
                    writer,
                    sheet_name=validation_name[:31],
                    index=False,
                    startrow=len(summary) + 3
                )

                continue

            # ---------- Record Count ----------
            elif "source_count" in result:

                detail_df = pd.DataFrame([{

                    "Source Count": result["source_count"],

                    "Target Count": result["target_count"],

                    "Status": result["status"]

                }])

            # ---------- If nothing found ----------
            if detail_df is None:

                detail_df = pd.DataFrame({

                    "Message": ["No detailed records available"]

                })

            detail_df.to_excel(

                writer,

                sheet_name=validation_name[:31],

                index=False

            )

    print(f"\nExcel Report Generated Successfully : {report_path}")

