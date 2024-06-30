# invoice_process

## Description

è«‹æ±‚æ›¸å‡¦ç†ã®ãƒ¯ãƒ¼ã‚¯ãƒ•ãƒ­ãƒ¼ã€‚è«‹æ±‚æ›¸ã®å‡¦ç†ã¨æ”¯æ‰•ã„ã¯ä¸€è²«ã—ã¦è¡Œã‚ã‚Œã‚‹ã‚‚ã®ã¨æƒ³å®šã—ã¦ã¾ã¨ã‚ã¦ã„ã‚‹ã€‚

<details>
<summary><strong>Table Definition</strong></summary>

```sql
CREATE TABLE `invoice_process` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'IDã€‚(tenant, process_num) ã§è¤‡åˆä¸»ã‚­ãƒ¼ã«ã™ã‚‹ã¨ä»–ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã¨JOINã™ã‚‹ã®ãŒé¢å€’ãªã®ã¨ã€å¾Œç¶šã®æ”¯æ‰•ã„å‡¦ç†ã§ä¸€æ„ãªè­˜åˆ¥å­ãŒãªã„ã¨ä¸ä¾¿ãã†ãªã®ã§ã‚µãƒ­ã‚²ãƒ¼ãƒˆã‚­ãƒ¼ã‚’ã¤ã‹ã†ã€‚',
  `tenant` int(11) unsigned NOT NULL COMMENT 'ãƒ†ãƒŠãƒ³ãƒˆ',
  `process_num` int(11) unsigned NOT NULL COMMENT 'ãƒ†ãƒŠãƒ³ãƒˆå†…ã§ä½¿ã‚ã‚Œã‚‹è«‹æ±‚æ›¸å‡¦ç†ã®é€šç•ªã€‚ç”»é¢ã® No. ã«ä½¿ã†ã€‚',
  `state` int(2) NOT NULL COMMENT 'ãƒ¯ãƒ¼ã‚¯ãƒ•ãƒ­ãƒ¼ã®çŠ¶æ…‹ã‚’ç¤ºã™å€¤ã€‚çŠ¶æ…‹ã«å¯¾ã™ã‚‹è¦ä»¶ãŒä¸æ˜Žãªã®ã§å€¤ã§è¡¨ç¾ã—ã¦ãŠãã€‚å°‘ãªãã¨ã‚‚æœªå‡¦ç†ã€å‰Šé™¤æ¸ˆã€å‡¦ç†ä¸­ã€å‡¦ç†æ¸ˆã¿ã®çŠ¶æ…‹ã¯å¿…è¦ã ã‚ã†ã€‚',
  `amount` int(11) unsigned NOT NULL COMMENT 'é‡‘é¡ã€‚æ”¯æ‰•ã„ãŒãƒžã‚¤ãƒŠã‚¹ã«ã¯ãªã‚‰ãªã„ã®ã§ã€unsigned ã¨ã™ã‚‹ã€‚',
  `payee` int(11) unsigned NOT NULL COMMENT 'æ”¯æ‰•å…ˆå–å¼•å…ˆ',
  `payment_method` int(11) unsigned NOT NULL COMMENT 'æ”¯æ‰•ã„æ–¹æ³•',
  `payee_bank_account` int(11) unsigned DEFAULT NULL COMMENT 'æŒ¯è¾¼å…ˆå£åº§ã€‚payment_method_type=bank_transfer ã®ã¨ãã®ã¿å€¤ãŒã‚ã‚‹ã€‚',
  `due` date NOT NULL COMMENT 'æ”¯æ‰•æœŸæ—¥',
  `pic` int(11) unsigned NOT NULL COMMENT 'æ‹…å½“è€…',
  `classification` int(11) unsigned NOT NULL COMMENT 'ä»•è¨³',
  PRIMARY KEY (`id`),
  UNIQUE KEY `process_num` (`process_num`,`tenant`),
  UNIQUE KEY `classification` (`classification`),
  KEY `tenant` (`tenant`),
  KEY `payee` (`payee`),
  KEY `payment_method` (`payment_method`),
  KEY `payee_bank_account` (`payee_bank_account`),
  KEY `pic` (`pic`),
  CONSTRAINT `invoice_process_ibfk_1` FOREIGN KEY (`tenant`) REFERENCES `tenant` (`id`),
  CONSTRAINT `invoice_process_ibfk_2` FOREIGN KEY (`payee`) REFERENCES `business_partner` (`id`),
  CONSTRAINT `invoice_process_ibfk_3` FOREIGN KEY (`payment_method`) REFERENCES `payment_method` (`id`),
  CONSTRAINT `invoice_process_ibfk_4` FOREIGN KEY (`payee_bank_account`) REFERENCES `business_partner_bank_account` (`id`),
  CONSTRAINT `invoice_process_ibfk_5` FOREIGN KEY (`pic`) REFERENCES `user` (`id`),
  CONSTRAINT `invoice_process_ibfk_6` FOREIGN KEY (`classification`) REFERENCES `classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='è«‹æ±‚æ›¸å‡¦ç†ã®ãƒ¯ãƒ¼ã‚¯ãƒ•ãƒ­ãƒ¼ã€‚è«‹æ±‚æ›¸ã®å‡¦ç†ã¨æ”¯æ‰•ã„ã¯ä¸€è²«ã—ã¦è¡Œã‚ã‚Œã‚‹ã‚‚ã®ã¨æƒ³å®šã—ã¦ã¾ã¨ã‚ã¦ã„ã‚‹ã€‚'
```

</details>

## Columns

| Name | Type | Default | Nullable | Extra Definition | Children | Parents | Comment |
| ---- | ---- | ------- | -------- | ---------------- | -------- | ------- | ------- |
| id | int(11) unsigned |  | false | auto_increment | [invoice_file](invoice_file.md) |  | IDã€‚(tenant, process_num) ã§è¤‡åˆä¸»ã‚­ãƒ¼ã«ã™ã‚‹ã¨ä»–ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã¨JOINã™ã‚‹ã®ãŒé¢å€’ãªã®ã¨ã€å¾Œç¶šã®æ”¯æ‰•ã„å‡¦ç†ã§ä¸€æ„ãªè­˜åˆ¥å­ãŒãªã„ã¨ä¸ä¾¿ãã†ãªã®ã§ã‚µãƒ­ã‚²ãƒ¼ãƒˆã‚­ãƒ¼ã‚’ã¤ã‹ã†ã€‚ |
| tenant | int(11) unsigned |  | false |  |  | [tenant](tenant.md) | ãƒ†ãƒŠãƒ³ãƒˆ |
| process_num | int(11) unsigned |  | false |  |  |  | ãƒ†ãƒŠãƒ³ãƒˆå†…ã§ä½¿ã‚ã‚Œã‚‹è«‹æ±‚æ›¸å‡¦ç†ã®é€šç•ªã€‚ç”»é¢ã® No. ã«ä½¿ã†ã€‚ |
| state | int(2) |  | false |  |  |  | ãƒ¯ãƒ¼ã‚¯ãƒ•ãƒ­ãƒ¼ã®çŠ¶æ…‹ã‚’ç¤ºã™å€¤ã€‚çŠ¶æ…‹ã«å¯¾ã™ã‚‹è¦ä»¶ãŒä¸æ˜Žãªã®ã§å€¤ã§è¡¨ç¾ã—ã¦ãŠãã€‚å°‘ãªãã¨ã‚‚æœªå‡¦ç†ã€å‰Šé™¤æ¸ˆã€å‡¦ç†ä¸­ã€å‡¦ç†æ¸ˆã¿ã®çŠ¶æ…‹ã¯å¿…è¦ã ã‚ã†ã€‚ |
| amount | int(11) unsigned |  | false |  |  |  | é‡‘é¡ã€‚æ”¯æ‰•ã„ãŒãƒžã‚¤ãƒŠã‚¹ã«ã¯ãªã‚‰ãªã„ã®ã§ã€unsigned ã¨ã™ã‚‹ã€‚ |
| payee | int(11) unsigned |  | false |  |  | [business_partner](business_partner.md) | æ”¯æ‰•å…ˆå–å¼•å…ˆ |
| payment_method | int(11) unsigned |  | false |  |  | [payment_method](payment_method.md) | æ”¯æ‰•ã„æ–¹æ³• |
| payee_bank_account | int(11) unsigned |  | true |  |  | [business_partner_bank_account](business_partner_bank_account.md) | æŒ¯è¾¼å…ˆå£åº§ã€‚payment_method_type=bank_transfer ã®ã¨ãã®ã¿å€¤ãŒã‚ã‚‹ã€‚ |
| due | date |  | false |  |  |  | æ”¯æ‰•æœŸæ—¥ |
| pic | int(11) unsigned |  | false |  |  | [user](user.md) | æ‹…å½“è€… |
| classification | int(11) unsigned |  | false |  |  | [classification](classification.md) | ä»•è¨³ |

## Constraints

| Name | Type | Definition |
| ---- | ---- | ---------- |
| classification | UNIQUE | UNIQUE KEY classification (classification) |
| invoice_process_ibfk_1 | FOREIGN KEY | FOREIGN KEY (tenant) REFERENCES tenant (id) |
| invoice_process_ibfk_2 | FOREIGN KEY | FOREIGN KEY (payee) REFERENCES business_partner (id) |
| invoice_process_ibfk_3 | FOREIGN KEY | FOREIGN KEY (payment_method) REFERENCES payment_method (id) |
| invoice_process_ibfk_4 | FOREIGN KEY | FOREIGN KEY (payee_bank_account) REFERENCES business_partner_bank_account (id) |
| invoice_process_ibfk_5 | FOREIGN KEY | FOREIGN KEY (pic) REFERENCES user (id) |
| invoice_process_ibfk_6 | FOREIGN KEY | FOREIGN KEY (classification) REFERENCES classification (id) |
| PRIMARY | PRIMARY KEY | PRIMARY KEY (id) |
| process_num | UNIQUE | UNIQUE KEY process_num (process_num, tenant) |

## Indexes

| Name | Definition |
| ---- | ---------- |
| payee | KEY payee (payee) USING BTREE |
| payee_bank_account | KEY payee_bank_account (payee_bank_account) USING BTREE |
| payment_method | KEY payment_method (payment_method) USING BTREE |
| pic | KEY pic (pic) USING BTREE |
| tenant | KEY tenant (tenant) USING BTREE |
| PRIMARY | PRIMARY KEY (id) USING BTREE |
| classification | UNIQUE KEY classification (classification) USING BTREE |
| process_num | UNIQUE KEY process_num (process_num, tenant) USING BTREE |

## Relations

![er](invoice_process.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)
