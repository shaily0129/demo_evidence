```sql table4
SELECT
*
FROM
    booking2.booking2;
```

```sql table5
SELECT
    "Start Date" AS date,
    COUNT(*) AS num_tests,
    SUM("Duration (seconds)") AS total_duration,
    AVG("Duration (seconds)") AS avg_duration,
    MIN("Duration (seconds)") AS min_duration,
    MAX("Duration (seconds)") AS max_duration
FROM booking2.booking2
GROUP BY "Start Date"
ORDER BY "Start Date";
```

<BarChart
    data={table4}
    title="Test Durations"
    x="Test Name"
    y="Duration (seconds)"
    tooltip={["Start Date", "Start Time", "Duration (seconds)"]}
    xLabel="Test Name"
    yLabel="Duration (seconds)"
    color="#4CAF50"
    grid={{ stroke: "#ccc" }}
    barSize={20} 
    legend={{ position: "top-right", text: "Test Duration" }} 
    padding={{ top: 20, bottom: 50, left: 40, right: 20 }} 
/>

<ScatterPlot
    data={table4}
    title="Test Duration Analysis Over Time"
    x="Start Date"
    y="Duration (seconds)"
    xFmt="%Y-%m-%d"
    tooltip={["Test Name", "Start Time", "Duration (seconds)"]}
    xLabel="Start Date"
    yLabel="Duration (seconds)"
    color="#FF5722"
    grid={{ stroke: "#ccc" }}
    pointSize={10}
    legend={{ position: "top-right", text: "Test Duration" }} 
    padding={{ top: 20, bottom: 50, left: 40, right: 20 }} 
/>

<FunnelChart 
    data={[
        { stage: 'test_complete_info', duration: 0.170 },
        { stage: 'test_empty_params', duration: 0.136 },
        { stage: 'test_empty_request', duration: 0.133 },
        { stage: 'test_insurance_provided', duration: 0.152 },
        { stage: 'test_large_age_value', duration: 0.132 }
    ]}
    nameCol="stage"
    valueCol="duration"
    funnelAlign="left"
    title="Test Case Duration Funnel"
    valueLabel="Duration (seconds)"
    color="#4CAF50"
    tooltip={["Start Date", "Start Time", "Duration (seconds)"]}
    grid={{ stroke: "#ccc" }}
/>

<ECharts
    config={{
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        series: [
            {
                name: 'Coverage',
                type: 'pie',
                radius: ['40%', '70%'],
                data: [
                    { value: 0.170, name: 'test_complete_info' },
                    { value: 0.136, name: 'test_empty_params' },
                    { value: 0.133, name: 'test_empty_request' },
                    { value: 0.152, name: 'test_insurance_provided' },
                    { value: 0.132, name: 'test_large_age_value' }
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    }}
/>

<LineChart
    data={table4}
    x="Test Name"
    y="Duration (seconds)"
    title="Test Name vs Duration(sec)"
    xLabel="Month"
    yLabel="Total Duration (seconds)"
/>
