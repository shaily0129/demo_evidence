<!-- Query to get total duration and number of tests per month -->
```sql table1
SELECT
    DATE_TRUNC('month', date) AS month,
    SUM(duration) AS total_duration,
    COUNT(*) AS num_tests,
    AVG(duration) AS avg_duration
FROM test_database.test_data1
GROUP BY month
ORDER BY month;
```

<!-- 
 Query to get total duration and number of tests per day -->
```sql table2
SELECT
    date,
    SUM(duration) AS total_duration,
    COUNT(*) AS num_tests,
    AVG(duration) AS avg_duration
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

```sql table3
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

<DataTable 
data={table3}
/>

<BarChart
    data={table3}
    title="Average Test Duration Over Time"
    x="date"
    y="avg_duration"
    tooltip={["module", "name", "file", "doc", "message"]}
    xLabel="Date"
    yLabel="Average Duration (s)"
    color="#4CAF50"
    grid={{ stroke: "#ccc" }}
/>

<ScatterPlot
    data={table3}
    title="Test Duration Analysis Over Time"
    x="date"
    y="avg_duration"
    xFmt="%Y-%m-%d"
    tooltip={["module", "name", "file", "doc", "message"]}
    xLabel="Date"
    yLabel="Average Duration (s)"
    color="#FF5722"
    grid={{ stroke: "#ccc" }}
/>


<!-- -- Line chart to visualize the total duration of tests by month -->
<LineChart
    data={table1}
    x="month"
    y="total_duration"
    xLabel="Month"
    yLabel="Total Duration (seconds)"
    title="Total Duration of Tests by Month"
    tooltip="Total Duration"
/>

<!-- -- Bar chart to visualize the average duration of tests by month -->
<BarChart
    data={table1}
    x="month"
    y="avg_duration"
    xLabel="Month"
    yLabel="Average Duration (seconds)"
    title="Average Duration of Tests by Month"
    tooltip="Avg Duration"
/>