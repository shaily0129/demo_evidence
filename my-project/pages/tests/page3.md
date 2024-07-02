```sql database1_tests
WITH pie_data AS (
    SELECT name, AVG(duration) AS value
    FROM test_database.test_data1
    WHERE module = 'test_classification'
    AND name IN (
        'test_classification_arabic_text',
        'test_classification_code_snippet',
        'test_classification_combination_characters',
        'test_classification_combined_unicode_text',
        'test_classification_cyrillic_text',
        'test_classification_default'
    )
    GROUP BY name
)
SELECT name, value
FROM pie_data;

```

<ECharts config={{
    tooltip: {
        formatter: '{b}: {c} ({d}%)'
    },
    series: [
        {
            type: 'pie',
            data: [
                { name: 'test_classification_arabic_text', value: 7.61 },
                { name: 'test_classification_code_snippet', value: 3.43 },
                { name: 'test_classification_combination_characters', value: 2.95 },
                { name: 'test_classification_combined_unicode_text', value: 2.76 },
                { name: 'test_classification_cyrillic_text', value: 3.70 },
                { name: 'test_classification_default', value: 6.31 },
            ],
        },
    ],
}} />
