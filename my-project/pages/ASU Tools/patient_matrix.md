```sql table1
SELECT
*
FROM
    test_database.asu_patient_prior;
```

```sql table2
WITH test_summary AS (
    SELECT
        "Status",
        COUNT(*) AS count
    FROM test_database.asu_patient_prior
    WHERE "Status" IN ('pass', 'fail')  -- Ensure to filter only pass and fail statuses
    GROUP BY "Status"
)

SELECT
    CASE WHEN "Status" = 'pass' THEN 'Pass' ELSE 'Fail' END AS name,
    count AS value
FROM test_summary;
```

<ECharts
    config={{
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
        series: [
            {
                name: 'Test Pass/Fail Distribution',
                type: 'pie',
                data: [
                    { name: 'Pass', value: 55 },  // Replace with actual counts from query
                    { name: 'Fail', value: 0 }   // Replace with actual counts from query
                ],
            },
        ],
    }}
/>

<LineChart 
    data={table1}  
    x="Test Case Name" 
    y="Duration (seconds)"
    seriesField="Status"  
    yAxisTitle="Duration (seconds)"  
    xAxisTitle="Test Case Name" 
/>
<ScatterPlot
    data={table1} 
    title="Test Case Performance"
    x="Start Date"
    y="Duration (seconds)"
    xLabel="Start Date"
    yLabel="Duration (seconds)"
    tooltip={["Test Case Name", "Start Date", "Start Time", "Duration (seconds)", "Status"]}
    color="#FF5722"
    grid={{ stroke: "#ccc" }}
    pointSize={10}
    legend={{ position: "top-right", text: "Test Cases" }}
    padding={{ top: 20, bottom: 50, left: 40, right: 20 }}
/>
