```sql table4
SELECT
*
FROM
    new_booking.new_booking;
```

```sql table5
SELECT
    date,
    COUNT(DISTINCT booking_id) AS num_unique_bookings
FROM new_booking.new_booking
GROUP BY date
ORDER BY date;

```

<ScatterPlot
    data={table4}
    title="Age vs Booking ID"
    x="age"
    y="request_id"
    xLabel="Age"
    yLabel="Booking ID"
    tooltip={["request_id", "name", "country", "insurance"]}
    color="#FF5722"
    grid={{ stroke: "#ccc" }}
    pointSize={10}
    legend={{ position: "top-right", text: "Booking Details" }}
    padding={{ top: 20, bottom: 50, left: 40, right: 20 }}
/>

<LineChart
    data={table4}
    x="age"
    y="request_id"
    title="Request ID over Age"
    xLabel="age"
    yLabel="request_id"
    tooltip={["request_id", "name", "country", "age", "insurance"]}
    grid={{ stroke: "#ccc" }}
/>



<BarChart
    data={table4}
    title="Number of Bookings by Country"
    x="country"
    y="request_id"
    xLabel="Country"
    yLabel="Number of Bookings"
    tooltip={["request_id", "name", "country", "age", "insurance"]}
    color="#4CAF50"
    grid={{ stroke: "#ccc" }}
    barSize={20}
    legend={{ position: "top-right", text: "Bookings" }}
    padding={{ top: 20, bottom: 50, left: 40, right: 20 }}
    groupBy="request_id" 
/>

<FunnelChart 
    data={table4}
    nameCol="age"
    valueCol="name"
    funnelAlign="left"
    title="Insurance Status Funnel"
    valueLabel="Booking ID"
    color="#4CAF50"
    tooltip={["request_id", "name", "country", "age"]}
    grid={{ stroke: "#ccc" }}
/>
