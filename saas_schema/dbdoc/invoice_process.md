# invoice_process

## Description

è«‹æ±‚æ›¸å‡¦ç†ã€‚è«‹æ±‚æ›¸ã®å‡¦ç†ã¨æ”¯æ‰•ã„ã¯ä¸€è²«ã—ã¦è¡Œã‚ã‚Œã‚‹ã‚‚ã®ã¨æƒ³å®šã—ã¦ã¾ã¨ã‚ã¦ã„ã‚‹ã€‚

<details>
<summary><strong>Table Definition</strong></summary>

```sql
CREATE TABLE `invoice_process` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'IDã€‚(tenant, process_id) ã§è¤‡åˆä¸»ã‚­ãƒ¼ã«ã™ã‚‹ã¨ä»–ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã¨JOINã™ã‚‹ã®ãŒé¢å€’ãªã®ã¨ã€å¾Œç¶šã®æ”¯æ‰•ã„å‡¦ç†ã§ä¸€æ„ãªè­˜åˆ¥å­ãŒãªã„ã¨ä¸ä¾¿ãã†ãªã®ã§ã‚µãƒ­ã‚²ãƒ¼ãƒˆã‚­ãƒ¼ã‚’ã¤ã‹ã†ã€‚',
  `tenant` int(11) unsigned NOT NULL COMMENT 'ãƒ†ãƒŠãƒ³ãƒˆ',
  `process_id` int(11) unsigned NOT NULL COMMENT 'ãƒ†ãƒŠãƒ³ãƒˆå†…ã§ä½¿ã‚ã‚Œã‚‹è«‹æ±‚æ›¸å‡¦ç†ã®é€šç•ªã€‚ç”»é¢ã® No. ã«ä½¿ã†ã€‚',
  `state` int(2) NOT NULL COMMENT 'çŠ¶æ…‹ã€‚æœªå‡¦ç†ã€å‰Šé™¤æ¸ˆã€å‡¦ç†ä¸­ï¼ˆç´°ã‹ã„çŠ¶æ…‹ãŒã‚ã‚‹ã‹ã‚‚ï¼‰ã€å‡¦ç†æ¸ˆã¿ã¯å¿…è¦ã€‚',
  `amount` int(11) unsigned NOT NULL COMMENT 'é‡‘é¡ã€‚æ”¯æ‰•ã„ãŒãƒžã‚¤ãƒŠã‚¹ã«ã¯ãªã‚‰ãªã„ã®ã§ã€unsigned ã¨ã™ã‚‹ã€‚',
  `payee` int(11) unsigned NOT NULL COMMENT 'æ”¯æ‰•å…ˆå–å¼•å…ˆ',
  `payment_method_type` enum('bank_transfer','direct_debit','credit card') COLLATE utf8mb4_bin NOT NULL COMMENT 'æ”¯æ‰•ã„æ–¹æ³•ç¨®åˆ¥',
  `payment_method_id` int(11) unsigned NOT NULL COMMENT 'æ”¯æ‰•ã„æ–¹æ³•ã€‚payment_method_type ãŒç¤ºã™ãƒ†ãƒ¼ãƒ–ãƒ«ã®IDã€‚å¤–éƒ¨ã‚­ãƒ¼åˆ¶ç´„ã¯ã¤ã‘ã‚‰ã‚Œãªã„ã€‚',
  `payee_bank_account` int(11) unsigned DEFAULT NULL COMMENT 'æŒ¯è¾¼å…ˆå£åº§. payment_method_type=bank_transfer ã®ã¨ãã®ã¿å€¤ãŒã‚ã‚‹',
  `due` date NOT NULL COMMENT 'æ”¯æ‰•æœŸæ—¥',
  `pic` int(11) unsigned NOT NULL COMMENT 'æ‹…å½“è€…',
  `classification` int(11) unsigned NOT NULL COMMENT 'ä»•è¨³',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tenant` (`tenant`,`process_id`),
  KEY `payee` (`payee`),
  KEY `payee_bank_account` (`payee_bank_account`),
  KEY `pic` (`pic`),
  KEY `classification` (`classification`),
  CONSTRAINT `invoice_process_ibfk_1` FOREIGN KEY (`tenant`) REFERENCES `tenant` (`id`),
  CONSTRAINT `invoice_process_ibfk_2` FOREIGN KEY (`payee`) REFERENCES `business_partner` (`id`),
  CONSTRAINT `invoice_process_ibfk_3` FOREIGN KEY (`payee_bank_account`) REFERENCES `bp_bank_account` (`id`),
  CONSTRAINT `invoice_process_ibfk_4` FOREIGN KEY (`pic`) REFERENCES `user` (`id`),
  CONSTRAINT `invoice_process_ibfk_5` FOREIGN KEY (`classification`) REFERENCES `classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='è«‹æ±‚æ›¸å‡¦ç†ã€‚è«‹æ±‚æ›¸ã®å‡¦ç†ã¨æ”¯æ‰•ã„ã¯ä¸€è²«ã—ã¦è¡Œã‚ã‚Œã‚‹ã‚‚ã®ã¨æƒ³å®šã—ã¦ã¾ã¨ã‚ã¦ã„ã‚‹ã€‚'
```

</details>

## Columns

| Name | Type | Default | Nullable | Extra Definition | Children | Parents | Comment |
| ---- | ---- | ------- | -------- | ---------------- | -------- | ------- | ------- |
| id | int(11) unsigned |  | false | auto_increment | [invoice_file](invoice_file.md) |  | IDã€‚(tenant, process_id) ã§è¤‡åˆä¸»ã‚­ãƒ¼ã«ã™ã‚‹ã¨ä»–ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã¨JOINã™ã‚‹ã®ãŒé¢å€’ãªã®ã¨ã€å¾Œç¶šã®æ”¯æ‰•ã„å‡¦ç†ã§ä¸€æ„ãªè­˜åˆ¥å­ãŒãªã„ã¨ä¸ä¾¿ãã†ãªã®ã§ã‚µãƒ­ã‚²ãƒ¼ãƒˆã‚­ãƒ¼ã‚’ã¤ã‹ã†ã€‚ |
| tenant | int(11) unsigned |  | false |  |  | [tenant](tenant.md) | ãƒ†ãƒŠãƒ³ãƒˆ |
| process_id | int(11) unsigned |  | false |  |  |  | ãƒ†ãƒŠãƒ³ãƒˆå†…ã§ä½¿ã‚ã‚Œã‚‹è«‹æ±‚æ›¸å‡¦ç†ã®é€šç•ªã€‚ç”»é¢ã® No. ã«ä½¿ã†ã€‚ |
| state | int(2) |  | false |  |  |  | çŠ¶æ…‹ã€‚æœªå‡¦ç†ã€å‰Šé™¤æ¸ˆã€å‡¦ç†ä¸­ï¼ˆç´°ã‹ã„çŠ¶æ…‹ãŒã‚ã‚‹ã‹ã‚‚ï¼‰ã€å‡¦ç†æ¸ˆã¿ã¯å¿…è¦ã€‚ |
| amount | int(11) unsigned |  | false |  |  |  | é‡‘é¡ã€‚æ”¯æ‰•ã„ãŒãƒžã‚¤ãƒŠã‚¹ã«ã¯ãªã‚‰ãªã„ã®ã§ã€unsigned ã¨ã™ã‚‹ã€‚ |
| payee | int(11) unsigned |  | false |  |  | [business_partner](business_partner.md) | æ”¯æ‰•å…ˆå–å¼•å…ˆ |
| payment_method_type | enum('bank_transfer','direct_debit','credit card') |  | false |  |  |  | æ”¯æ‰•ã„æ–¹æ³•ç¨®åˆ¥ |
| payment_method_id | int(11) unsigned |  | false |  |  |  | æ”¯æ‰•ã„æ–¹æ³•ã€‚payment_method_type ãŒç¤ºã™ãƒ†ãƒ¼ãƒ–ãƒ«ã®IDã€‚å¤–éƒ¨ã‚­ãƒ¼åˆ¶ç´„ã¯ã¤ã‘ã‚‰ã‚Œãªã„ã€‚ |
| payee_bank_account | int(11) unsigned |  | true |  |  | [bp_bank_account](bp_bank_account.md) | æŒ¯è¾¼å…ˆå£åº§. payment_method_type=bank_transfer ã®ã¨ãã®ã¿å€¤ãŒã‚ã‚‹ |
| due | date |  | false |  |  |  | æ”¯æ‰•æœŸæ—¥ |
| pic | int(11) unsigned |  | false |  |  | [user](user.md) | æ‹…å½“è€… |
| classification | int(11) unsigned |  | false |  |  | [classification](classification.md) | ä»•è¨³ |

## Constraints

| Name | Type | Definition |
| ---- | ---- | ---------- |
| invoice_process_ibfk_1 | FOREIGN KEY | FOREIGN KEY (tenant) REFERENCES tenant (id) |
| invoice_process_ibfk_2 | FOREIGN KEY | FOREIGN KEY (payee) REFERENCES business_partner (id) |
| invoice_process_ibfk_3 | FOREIGN KEY | FOREIGN KEY (payee_bank_account) REFERENCES bp_bank_account (id) |
| invoice_process_ibfk_4 | FOREIGN KEY | FOREIGN KEY (pic) REFERENCES user (id) |
| invoice_process_ibfk_5 | FOREIGN KEY | FOREIGN KEY (classification) REFERENCES classification (id) |
| PRIMARY | PRIMARY KEY | PRIMARY KEY (id) |
| tenant | UNIQUE | UNIQUE KEY tenant (tenant, process_id) |

## Indexes

| Name | Definition |
| ---- | ---------- |
| classification | KEY classification (classification) USING BTREE |
| payee | KEY payee (payee) USING BTREE |
| payee_bank_account | KEY payee_bank_account (payee_bank_account) USING BTREE |
| pic | KEY pic (pic) USING BTREE |
| PRIMARY | PRIMARY KEY (id) USING BTREE |
| tenant | UNIQUE KEY tenant (tenant, process_id) USING BTREE |

## Relations

![er](invoice_process.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)
