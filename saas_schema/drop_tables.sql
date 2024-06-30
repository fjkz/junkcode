SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE
  account_category,
  account_subcategory,
  business_partner_bank_account,
  business_partner,
  classification,
  classification_detail,
  classification_detail_pair,
  cost_center,
  invoice_file,
  invoice_process,
  payment_method,
  payment_method_bank_transfer,
  payment_method_credit_card,
  payment_method_direct_debit,
  tax_class,
  tenant,
  user;

SET FOREIGN_KEY_CHECKS = 1;
