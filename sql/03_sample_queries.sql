--this command used to identify the constraint stopping column is_active from dropping in the staff table
SELECT name
FROM sys.default_constraints
WHERE parent_object_id = OBJECT_ID('staff')
  AND parent_column_id = COLUMNPROPERTY(parent_object_id, 'is_active', 'ColumnId');