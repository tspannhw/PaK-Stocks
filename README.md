# PaK-Stocks
Stocks



#### See also 

* https://github.com/tspannhw/FLaNK-Py-Stocks



#### References

* pip3.11  install kafka-python -U



#### Stonks table

````

CREATE TABLE `ssb`.`Meetups`.`stock2` (
  `symbol` VARCHAR(2147483647),
  `uuid` VARCHAR(2147483647),
  `ts` BIGINT,
  `dt` BIGINT,
  `datetime` VARCHAR(2147483647),
  `open` VARCHAR(2147483647),
  `close` VARCHAR(2147483647),
  `high` VARCHAR(2147483647),
  `volume` VARCHAR(2147483647),
  `low` VARCHAR(2147483647),
  `eventTimestamp` TIMESTAMP(3) WITH LOCAL TIME ZONE METADATA FROM 'timestamp',
  WATERMARK FOR `eventTimestamp` AS `eventTimestamp` - INTERVAL '3' SECOND
) WITH (
  'scan.startup.mode' = 'group-offsets',
  'deserialization.failure.policy' = 'ignore_and_log',
  'properties.request.timeout.ms' = '120000',
  'properties.auto.offset.reset' = 'earliest',
  'format' = 'json',
  'properties.bootstrap.servers' = 'kafka:9092',
  'connector' = 'kafka',
  'properties.transaction.timeout.ms' = '900000',
  'topic' = 'stocks2',
  'properties.group.id' = 'stock2flink'
)



````
