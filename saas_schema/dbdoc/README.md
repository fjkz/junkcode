# mysaas

## Tables

| Name | Columns | Comment | Type |
| ---- | ------- | ------- | ---- |
| [account_category](account_category.md) | 4 | ç§‘ç›®ã€‚ç§‘ç›®ã¯ç‹¬è‡ªã«è¿½åŠ ã§ãã‚‹ã¨ã—ã¦ã€ãƒ†ãƒŠãƒ³ãƒˆæ¯Žã«ç§‘ç›®ã‚’ç”¨æ„ã™ã‚‹ã€‚æ¨™æº–ã®ç§‘ç›®ã‚‚é‡ãŒå°‘ãªã„ã®ã§ãƒ†ãƒŠãƒ³ãƒˆã”ã¨ã«ã‚³ãƒ”ãƒ¼ã™ã‚‹ã‚ˆã†ã«ã—ã¦ã„ã‚‹ã€‚ | BASE TABLE |
| [account_subcategory](account_subcategory.md) | 3 | è£œåŠ©ç§‘ç›® | BASE TABLE |
| [business_partner](business_partner.md) | 3 | å–å¼•å…ˆã€‚è«‹æ±‚å…ƒã‚„æ”¯æ‰•ã„å…ˆã®å€‹äººã‚‚ã—ãã¯æ³•äºº | BASE TABLE |
| [business_partner_bank_account](business_partner_bank_account.md) | 7 | å–å¼•å…ˆã®éŠ€è¡Œå£åº§ã€‚payment_method_bank_transfer ã¨ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã¯é‡è¤‡ã™ã‚‹ãŒã€å…±é€šéƒ¨åˆ†ã‚’åˆ‡ã‚Šå‡ºã™ã¨ä½™è¨ˆãªãƒ†ãƒ¼ãƒ–ãƒ«ãŒå¢—ãˆã¦ã‚¯ã‚¨ãƒªãŒè¤‡é›‘ã«ãªã‚‹ã®ã§ã€é‡è¤‡ã—ãŸãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã‚’ãã‚Œãžã‚Œã«æŒãŸã›ã¦ã„ã‚‹ã€‚ã¾ãŸã€ä»®ã«ãã‚Œãžã‚Œã®ãƒ†ãƒ¼ãƒ–ãƒ«ã«é‡è¤‡ã—ãŸéŠ€è¡Œå£åº§ãŒã‚ã£ã¦ã‚‚ã€ä¸€ã¤ã«å¯„ã›ã¦ã¯ãªã‚‰ãªã„ã€‚ | BASE TABLE |
| [classification](classification.md) | 2 | ä»•è¨³ã€‚invoice_process ã«ã¾ã¨ã‚ã‚‹ã“ã¨ã‚‚è€ƒãˆãŸãŒã€invoice_process_detail ãŒå¿…è¦ã«ãªã£ãŸã®ã§å¯¾ç§°æ€§ã®ãŸã‚ã«ä»•è¨³ã¯åˆ‡ã‚Šå‡ºã—ãŸã€‚ | BASE TABLE |
| [classification_detail](classification_detail.md) | 8 | ä»•è¨³æ˜Žç´°ã€‚åŒä¸€ã®è«‹æ±‚æ˜Žç´°ã§ã‚ã£ã¦ã‚‚è²¸æ–¹å€Ÿæ–¹ãã‚Œãžã‚Œã®ãƒ¬ã‚³ãƒ¼ãƒ‰ãŒå…¥ã‚‹ã€‚ | BASE TABLE |
| [classification_detail_pair](classification_detail_pair.md) | 4 | ä»•è¨³æ˜Žç´°ãƒšã‚¢ã€‚è¨ˆä¸Šæ—¥ãŒåŒã˜å€Ÿæ–¹ã¨å€Ÿæ–¹ã‚’ãƒšã‚¢ã«ã—ã¦æ‘˜è¦ã‚’åŠ ãˆã‚‹ã®ã¯ã€ç”»é¢ç‰¹æœ‰ã®æ¦‚å¿µã¨æ€ã‚ã‚Œã‚‹ã®ã§åˆ¥ãƒ†ãƒ¼ãƒ–ãƒ«ã§è¡¨ç¾ã™ã‚‹ã€‚ | BASE TABLE |
| [cost_center](cost_center.md) | 3 | ä¼šè¨ˆä¸Šã®éƒ¨é–€ | BASE TABLE |
| [invoice_file](invoice_file.md) | 5 | è«‹æ±‚æ›¸ãƒ•ã‚¡ã‚¤ãƒ«ã€‚è«‹æ±‚æ›¸ã®ä¸­ã®ãƒ‡ãƒ¼ã‚¿ã¯ã€æ§‹é€ ãŒå–å¼•å…ˆã«ã‚ˆã£ã¦ç•°ãªã‚‹ã¨æ€ã‚ã‚Œã‚‹ã®ã§ãƒ†ãƒ¼ãƒ–ãƒ«ã«ã¯å…¥ã‚Œãªã„ã€‚ | BASE TABLE |
| [invoice_process](invoice_process.md) | 11 | è«‹æ±‚æ›¸å‡¦ç†ã®ãƒ¯ãƒ¼ã‚¯ãƒ•ãƒ­ãƒ¼ã€‚è«‹æ±‚æ›¸ã®å‡¦ç†ã¨æ”¯æ‰•ã„ã¯ä¸€è²«ã—ã¦è¡Œã‚ã‚Œã‚‹ã‚‚ã®ã¨æƒ³å®šã—ã¦ã¾ã¨ã‚ã¦ã„ã‚‹ã€‚ | BASE TABLE |
| [payment_method](payment_method.md) | 5 | æ”¯æ‰•ã„æ–¹æ³•ã€‚å…·ä½“çš„ãªæ”¯æ‰•ã„æ–¹æ³•ã¯æ”¯æ‰•ã„ã‚«ãƒ†ã‚´ãƒªã”ã¨ã«åˆ¥ãƒ†ãƒ¼ãƒ–ãƒ«ã«ã‚‚ã¡ã€ã“ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã‚’å‚ç…§ã™ã‚‹ã€‚is_default ã®ã‚ˆã†ãªå…±é€šã®ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã¯ã“ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã«ç½®ãã€‚ | BASE TABLE |
| [payment_method_bank_transfer](payment_method_bank_transfer.md) | 5 | éŠ€è¡ŒæŒ¯ã‚Šè¾¼ã¿ã«ã‚ˆã‚‹æ”¯æ‰•æ–¹æ³•ã€‚æ”¯æ‰•å…ˆã§ã¯ãªãã€æ”¯æ‰•ã„å…ƒã®éŠ€è¡Œå£åº§ã‚’ç¤ºã—ã¦ã„ã‚‹ã€‚æ”¯æ‰•ã„æ–¹æ³•ã®ã‚«ãƒ†ã‚´ãƒªã”ã¨ã«ãƒ†ãƒ¼ãƒ–ãƒ«ã‚’åˆ†ã‘ã‚‹ã€‚ã“ã®çµæžœå¤–éƒ¨ã‚­ãƒ¼åˆ¶ç´„ã¯ã¤ã‘ã‚‰ã‚Œãªã„ã€‚ä¸€æ–¹ã§ã€ã™ã¹ã¦ã®æ”¯æ‰•ã„ç¨®åˆ¥ã‚’ä¸€ã¤ã®ãƒ†ãƒ¼ãƒ–ãƒ«ã§è¡¨ç¾ã™ã‚‹ã¨ã€ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ãŒNULLã°ã‹ã‚Šã«ãªã‚Šã€ã¾ãŸæ”¯æ‰•ã„ç¨®åˆ¥ã®è¿½åŠ ãŒé›£ã—ããªã‚‹ã€‚ | BASE TABLE |
| [payment_method_credit_card](payment_method_credit_card.md) | 1 | ã‚¯ãƒ¬ã‚¸ãƒƒãƒˆã‚«ãƒ¼ãƒ‰ã«ã‚ˆã‚‹æ”¯æ‰•ã„æ–¹æ³•ã€‚ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã¯æ˜Žã‚‰ã‹ã§ãªã„ã®ã§çœç•¥ã™ã‚‹ã€‚ | BASE TABLE |
| [payment_method_direct_debit](payment_method_direct_debit.md) | 1 | è‡ªå‹•å¼•è½ã«ã‚ˆã‚‹æ”¯æ‰•ã„æ–¹æ³•ã€‚ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã¯æ˜Žã‚‰ã‹ã§ãªã„ã®ã§çœç•¥ã™ã‚‹ã€‚ | BASE TABLE |
| [tax_class](tax_class.md) | 2 | ç¨ŽåŒºåˆ†ã€‚ç¨ŽçŽ‡å¤‰æ›´ã‚„å±žæ€§å€¤ã®è¿½åŠ ã‚’è€ƒæ…®ã—ã¦ã€ENUM ã§è¡¨ç¾ã›ãšã«åˆ¥ãƒ†ãƒ¼ãƒ–ãƒ«ã«ã™ã‚‹ã€‚ç¨ŽåŒºåˆ†ã¯ãƒ†ãƒŠãƒ³ãƒˆã«ã‚ˆã‚‰ãªã„ã€‚ | BASE TABLE |
| [tenant](tenant.md) | 1 | ãƒ†ãƒŠãƒ³ãƒˆã€‚ä¸»ã‚­ãƒ¼ä»¥å¤–ã®ãƒ•ã‚£ãƒ¼ãƒ«ãƒ‰ã¯ä¸æ˜Žãªã®ã§çœç•¥ã™ã‚‹ã€‚ | BASE TABLE |
| [user](user.md) | 3 | ã“ã® SaaS ã‚µãƒ¼ãƒ“ã‚¹ã‚’ä½¿ã†äººé–“ | BASE TABLE |

## Relations

![er](schema.svg)

---

> Generated by [tbls](https://github.com/k1LoW/tbls)
