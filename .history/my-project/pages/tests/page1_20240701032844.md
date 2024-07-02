

```sql Unit_Tests1
SELECT
    date,
    SUM(duration) AS total_duration,
    COUNT(*) AS num_tests
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

<LineChart
    data={Unit_Tests1}
    y="total_duration"
    title="Total Duration of Tests by Month"
/>


```sql Tests_over_Time
SELECT
    date,
    COUNT(*) AS num_tests,
    SUM(duration) AS total_duration,
    AVG(duration) AS avg_duration,
    MIN(duration) AS min_duration,
    MAX(duration) AS max_duration
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

<BarChart
    data={Tests_over_Time}
    title="Bar Chart"
    x="date"
    y="avg_duration"
    tooltip="module, name, file, doc, message"
/>

<ScatterPlot
    data={Tests_over_Time}  
    title="Scatter Plot"
    x="date"                  
    y="avg_duration"             
    xFmt="date"            
/>

<DataTable 
data={Tests_over_Time}
/>