CREATE TABLE cleansed_transactions AS
SELECT *
FROM raw_transactions
WHERE amount > 0;
