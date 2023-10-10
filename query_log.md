```sql
DELETE FROM birthDB WHERE id=1;
```

```sql
SELECT * FROM birthDB WHERE year = 2000
```

```sql
SELECT * FROM birthDB;
```

```sql

    SELECT year
    FROM default.births2000DB
    LIMIT 10;
    
```

```response from databricks
[Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000)]
```

```sql

    SELECT year
    FROM default.births2000DB
    LIMIT 10;
    
```

```response from databricks
[Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000)]
```

```sql

    SELECT year, sum(births) as annual_births
    FROM default.births2000DB
    GROUP BY year
    LIMIT 10;
    
```

```response from databricks
[Row(year=2000, annual_births=1117947)]
```

```sql

    SELECT t1.year, SUM(t1.births) as annual_births
            FROM default.births2000 t1
            GROUP BY t1.year
            LIMIT 10;
    
```

```response from databricks
[]
```

```sql
SELECT year FROM default.births2000DB
```

```response from databricks
[Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000)]
```

```sql
SELECT year, SUM(births)
            FROM default.births2000DB
            GROUP BY year
            
```

```response from databricks
[Row(year=2000, sum(births)=1117947)]
```

```sql
SELECT year, SUM(births)
            FROM default.births2000DB
            GROUP BY year
            ORDER BY year
            
```

```response from databricks
[Row(year=2000, sum(births)=1117947)]
```

```sql
SELECT month, SUM(births)
            FROM default.births2000DB
            GROUP BY month
            ORDER BY month
            
```

```response from databricks
[Row(month=1, sum(births)=328656), Row(month=2, sum(births)=324046), Row(month=3, sum(births)=347824), Row(month=4, sum(births)=117421)]
```

```sql
SELECT month, SUM(births)
            FROM default.births2000DB
            GROUP BY month
            ORDER BY month
            
```

```response from databricks
[Row(month=1, sum(births)=328656), Row(month=2, sum(births)=324046), Row(month=3, sum(births)=347824), Row(month=4, sum(births)=117421)]
```

```sql
SELECT year FROM default.births2000DB
```

```response from databricks
[Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000), Row(year=2000)]
```

```sql
SELECT month, SUM(births)
            FROM default.births2000DB
            GROUP BY month
            ORDER BY month
            
```

```response from databricks
[Row(month=1, sum(births)=328656), Row(month=2, sum(births)=324046), Row(month=3, sum(births)=347824), Row(month=4, sum(births)=117421)]
```

```sql
SELECT month, SUM(births)
            FROM default.births2000DB
            GROUP BY month
            ORDER BY month
            
```

```response from databricks
[Row(month=1, sum(births)=328656), Row(month=2, sum(births)=324046), Row(month=3, sum(births)=347824), Row(month=4, sum(births)=117421)]
```

