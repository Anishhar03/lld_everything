# Capacity Estimation

Capacity estimation shows whether your design can handle expected scale.

## Common Units

```text
1 KB = 10^3 bytes
1 MB = 10^6 bytes
1 GB = 10^9 bytes
1 TB = 10^12 bytes
```

## QPS

```text
Average QPS = requests per day / 86400
Peak QPS = average QPS * peak factor
```

Example:

```text
100M requests/day / 86400 = about 1157 QPS
Peak at 5x = about 5800 QPS
```

## Storage

```text
storage/day = records/day * record size
total storage = storage/day * retention days * replication factor
```

Example:

```text
10M events/day * 500 bytes = 5GB/day
1 year = 1.8TB
3 replicas = 5.4TB
```

## Bandwidth

```text
bandwidth/sec = QPS * response size
```

Example:

```text
5000 QPS * 20KB = 100MB/s
```

## Cache Size

If 20% hot data serves 80% traffic:

```text
cache size = hot objects * object size
```

## Interview Tip

Do not over-optimize exact math. Show order-of-magnitude thinking and explain assumptions.
