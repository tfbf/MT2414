Step To Execute Bible Transition Using Token Concept
====================================================

1. Create master table using "MAL_NEHEMIAH_SMPL.txt" file script.

2. Create token table using "MAL_NEHEMIAH_SMPL_TOKEN.txt" file script.

3. Create unique token table using "MAL_NEHEMIAH_SMPL_UNI_TOKEN" file
   script.

4. Create consolidate token value table using
   "MAL_NEHEMIAH_SMPL_CSD_EC.txt" file script.

5. Upload the Verse in to the Master table (i.e. MAL_NEHEMIAH_SMPL),
   using excel sheet as per the table format.

6. Once after successfully upload, run the PLSQL
   "Split_Token_Value_Script.txt" script to split the verse into token
   value and same will be inserted into "MAL_NEHEMIAH_SMPL_TOKEN"
   table.

7. Extract unique records from "MAL_NEHEMIAH_SMPL_TOKEN" table &
   export it unique token in excel sheet and update the required
   translation value in the excel sheet.

8. Upload the translated unique token value in to
   "MAL_NEHEMIAH_SMPL_UNI_TOKEN" table.

9. Run the update token values script as mentioned in the
   "Update_Token_Values_Table_Scripts.txt" file.


10. Once step 9 is completed, unique translated values will be updated
    for the all the token records in the "MAL_NEHEMIAH_SMPL_TOKEN" table.

11. Run consolidate the token value scripts as mentioned in the
    "Merge_Token_Values_Script.txt" file.

12. Once step 11 is completed, all the translated values will be
    updated in consolidated verse format in the
    "MAL_NEHEMIAH_SMPL_CSD_EC" table.

13. Download the translate bible verses into excel sheet from
    "MAL_NEHEMIAH_SMPL_CSD_EC" table.
