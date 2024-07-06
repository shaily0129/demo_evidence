```sql table6
SELECT
    "Test Case Name",
    "Start Date",
    "Start Time",
    "Duration (seconds)",
    "Status"
FROM new_booking.new_booking2
```


```sql table7
WITH test_summary AS (
    SELECT
        "Status",
        COUNT(*) AS count
    FROM new_booking.new_booking2
    WHERE "Status" IN ('pass', 'fail')  -- Ensure to filter only pass and fail statuses
    GROUP BY "Status"
)

SELECT
    CASE WHEN "Status" = 'pass' THEN 'Pass' ELSE 'Fail' END AS name,
    count AS value
FROM test_summary;
```


<ECharts config={{
    tooltip: {
        formatter: '{b}: {c} ({d}%)'
    },
    series: [
        {
            name: 'Test Pass/Fail Distribution',
            type: 'pie',
            data: [
                { name: 'Pass', value: 87 },
                { name: 'Fail', value: 21 }
            ],
        },
    ],
}} />


<LineChart 
    data={table7}
    x="name"
    y="value"
    seriesField="name"
    yAxisTitle="Number of Tests"
    xAxisTitle="Test Status"
/>

<ScatterPlot
    data={table6}
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