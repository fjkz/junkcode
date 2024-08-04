# tax_class

## Description

ç¨ŽåŒºåˆ†ã€‚ç¨ŽçŽ‡å¤‰æ›´ã‚„å±žæ€§å€¤ã®è¿½åŠ ã‚’è€ƒæ…®ã—ã¦ã€ENUM ã§è¡¨ç¾ã›ãšã«åˆ¥ãƒ†ãƒ¼ãƒ–ãƒ«ã«ã™ã‚‹ã€‚ç¨ŽåŒºåˆ†ã¯ãƒ†ãƒŠãƒ³ãƒˆã«ã‚ˆã‚‰ãªã„ã€‚

<details>
<summary><strong>Table Definition</strong></summary>

```sql
CREATE TABLE `tax_class` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL COMMENT 'è¡¨ç¤ºå',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='ç¨ŽåŒºåˆ†ã€‚ç¨ŽçŽ‡å¤‰æ›´ã‚„å±žæ€§å€¤ã®è¿½åŠ ã‚’è€ƒæ…®ã—ã¦ã€ENUM ã§è¡¨ç¾ã›ãšã«åˆ¥ãƒ†ãƒ¼ãƒ–ãƒ«ã«ã™ã‚‹ã€‚ç¨ŽåŒºåˆ†ã¯ãƒ†ãƒŠãƒ³ãƒˆã«ã‚ˆã‚‰ãªã„ã€‚'
```

</details>

## Columns

| Name | Type | Default | Nullable | Extra Definition | Children | Parents | Comment |
| ---- | ---- | ------- | -------- | ---------------- | -------- | ------- | ------- |
| id | int(11) unsigned |  | false | auto_increment | [classification_detail](classification_detail.md) |  | ID |
| name | varchar(255) |  | false |  |  |  | è¡¨ç¤ºå |

## Constraints

| Name | Type | Definition |
| ---- | ---- | ---------- |
| name | UNIQUE | UNIQUE KEY name (name) |
| PRIMARY | PRIMARY KEY | PRIMARY KEY (id) |

## Indexes

| Name | Definition |
| ---- | ---------- |
| PRIMARY | PRIMARY KEY (id) USING BTREE |
| name | UNIQUE KEY name (name) USING BTREE |

## Relations

![er](tax_class.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)