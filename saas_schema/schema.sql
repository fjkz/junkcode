-- 資料には言及がない機能の実現のためのテーブルやフィールドはキリがないので省いています。
-- レコード作成のタイムスタンプなど業務に関係しないフィールドは省略している。
-- スキーマで表現するために、なるべくユニーク制約と外部キー制約を貼っています。

CREATE TABLE tenant (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='テナント。主キー以外のフィールドは不明なので省略する。';

CREATE TABLE user (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント。ユーザーは１つのテナントに所属する。テナントの付けかえも考慮しない。',
  name varchar(255) NOT NULL COMMENT '名前。テナント内でユーザーを識別子する値として使う。',
  PRIMARY KEY (id),
  UNIQUE (name, tenant), -- カーディナリティの高い順
  FOREIGN KEY (tenant) REFERENCES tenant (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='この SaaS サービスを使う人間';

CREATE TABLE business_partner (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  name varchar(255) NOT NULL COMMENT '表示名',
  PRIMARY KEY (id),
  UNIQUE (name, tenant),
  FOREIGN KEY (tenant) REFERENCES tenant (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='取引先。請求元や支払い先の個人もしくは法人';

CREATE TABLE business_partner_bank_account (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  owner int(11) unsigned NOT NULL COMMENT '取引先',
  name varchar(255) NOT NULL COMMENT '表示名',
  bank_code char(4) NOT NULL COMMENT '銀行コード。銀行コードのマスタが要るが省略する。',
  account_type int(1) NOT NULL COMMENT '口座種別',
  branch char(5) NOT NULL COMMENT '支店番号',
  account_number char(8) COMMENT '口座番号',
  PRIMARY KEY (id),
  UNIQUE (name, owner),
  UNIQUE (account_number, branch, bank_code, owner), -- 同じ口座は登録できない。
  FOREIGN KEY (owner) REFERENCES business_partner (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='取引先の銀行口座。payment_method_bank_transfer とフィールドは重複するが、共通部分を切り出すと余計なテーブルが増えてクエリが複雑になるので、重複したフィールドをそれぞれに持たせている。また、仮にそれぞれのテーブルに重複した銀行口座があっても、一つに寄せてはならない。';

CREATE TABLE payment_method (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  payment_method_type enum("bank_transfer", "direct_debit", "credit card") NOT NULL COMMENT '支払い方法種別。この種別の支払い方法のテーブルのみこのレコードには参照をもつ。',
  name char(255) NOT NULL COMMENT '表示名',
  is_default boolean NOT NULL COMMENT '既定の支払い方法か否かを表すフラグ。テナントごとに１つデフォルトがある。',
  PRIMARY KEY (id),
  UNIQUE (name, tenant),
  FOREIGN KEY (tenant) REFERENCES tenant (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='支払い方法。具体的な支払い方法は支払いカテゴリごとに別テーブルにもち、このテーブルを参照する。is_default のような共通のフィールドはこのテーブルに置く。';

CREATE TABLE payment_method_bank_transfer (
  payment_method_id int(11) unsigned NOT NULL COMMENT '支払い方法ID。payment_method テーブルの主キーと同一の値である。',
  bank_code char(4) NOT NULL COMMENT '銀行コード。銀行コードのマスタが要るが省略する。',
  account_type int(1) NOT NULL COMMENT '口座種別',
  branch char(5) NOT NULL COMMENT '支店番号',
  account_number char(8) NOT NULL COMMENT '口座番号',
  PRIMARY KEY (payment_method_id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_method (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='銀行振り込みによる支払方法。支払先ではなく、支払い元の銀行口座を示している。支払い方法のカテゴリごとにテーブルを分ける。この結果外部キー制約はつけられない。一方で、すべての支払い種別を一つのテーブルで表現すると、フィールドがNULLばかりになり、また支払い種別の追加が難しくなる。';

CREATE TABLE payment_method_direct_debit (
  payment_method_id int(11) unsigned NOT NULL COMMENT '支払い方法ID。payment_method テーブルの主キーと同一の値である。',
  PRIMARY KEY (payment_method_id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_method (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='自動引落による支払い方法。フィールドは明らかでないので省略する。';

CREATE TABLE payment_method_credit_card (
  payment_method_id int(11) unsigned NOT NULL COMMENT '支払い方法ID。payment_method テーブルの主キーと同一の値である。',
  PRIMARY KEY (payment_method_id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_method (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='クレジットカードによる支払い方法。フィールドは明らかでないので省略する。';

CREATE TABLE account_category (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  name varchar(255) NOT NULL COMMENT '表示名',
  dr_or_cr enum('debit', 'credit') NOT NULL COMMENT '借方 or 貸方',
  PRIMARY KEY (id),
  UNIQUE (tenant, name, dr_or_cr), -- 科目名はどのテナントでも同じなので tenant を先にする。
  FOREIGN KEY (tenant) REFERENCES tenant (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='科目。科目は独自に追加できるとして、テナント毎に科目を用意する。標準の科目も量が少ないのでテナントごとにコピーするようにしている。';

CREATE TABLE account_subcategory (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  name varchar(255) NOT NULL COMMENT '表示名',
  category int(11) unsigned NOT NULL COMMENT '親の科目',
  PRIMARY KEY (id),
  UNIQUE (category, name),
  FOREIGN KEY (category) REFERENCES account_category (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='補助科目';

CREATE TABLE cost_center (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  name varchar(255) NOT NULL COMMENT '表示名',
  PRIMARY KEY (id),
  UNIQUE (name, tenant),
  FOREIGN KEY (tenant) REFERENCES tenant (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='会計上の部門';

CREATE TABLE tax_class (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  name varchar(255) NOT NULL COMMENT '表示名',
  PRIMARY KEY (id),
  UNIQUE (name)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='税区分。税率変更や属性値の追加を考慮して、ENUM で表現せずに別テーブルにする。税区分はテナントによらない。';

CREATE TABLE classification (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  remarks varchar(2000) COMMENT '請求メモ',
  PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='仕訳。invoice_process にまとめることも考えたが、invoice_process_detail が必要になったので対称性のために仕訳は切り出した。';

CREATE TABLE classification_detail (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  parent int(11) unsigned NOT NULL COMMENT '明細の親である仕訳',
  date date NOT NULL COMMENT '計上日',
  amount int(11) NOT NULL COMMENT '金額。請求を債権と相殺するなどマイナスはありうるので、帳簿上は signed とする。',
  category int(11) unsigned NOT NULL COMMENT '勘定科目。科目に借方貸方を設定しているので、科目からこの明細の借方貸方がわかる。',
  subcategory int(11) unsigned COMMENT '補助科目',
  cost_center int(11) unsigned COMMENT '部門',
  tax_class int(11) unsigned NOT NULL COMMENT '税区分',
  PRIMARY KEY (id),
  FOREIGN KEY (parent) REFERENCES classification (id),
  FOREIGN KEY (category) REFERENCES account_category (id),
  FOREIGN KEY (subcategory) REFERENCES account_subcategory (id),
  FOREIGN KEY (cost_center) REFERENCES cost_center (id),
  FOREIGN KEY (tax_class) REFERENCES tax_class (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='仕訳明細。同一の請求明細であっても貸方借方それぞれのレコードが入る。';

CREATE TABLE classification_detail_pair (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  debit_detail int(11) unsigned COMMENT '借方明細。credit_detail と同じ仕訳に属して、計上日も同じ。',
  credit_detail int(11) unsigned COMMENT '貸方明細。debit_detail と同じ仕訳に属して、計上日も同じ。',
  remarks varchar(2000) COMMENT '摘要',
  PRIMARY KEY (id),
  UNIQUE (debit_detail),
  FOREIGN KEY (debit_detail) REFERENCES classification_detail (id),
  UNIQUE (credit_detail),
  FOREIGN KEY (credit_detail) REFERENCES classification_detail (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='仕訳明細ペア。計上日が同じ借方と借方をペアにして摘要を加えるのは、画面特有の概念と思われるので別テーブルで表現する。';

CREATE TABLE invoice_process (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID。(tenant, process_num) で複合主キーにすると他のテーブルとJOINするのが面倒なのと、後続の支払い処理で一意な識別子がないと不便そうなのでサロゲートキーをつかう。',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  process_num int(11) unsigned NOT NULL COMMENT 'テナント内で使われる請求書処理の通番。画面の No. に使う。',
  state int(2) NOT NULL COMMENT 'ワークフローの状態を示す値。状態に対する要件が不明なので値で表現しておく。少なくとも未処理、削除済、処理中、処理済みの状態は必要だろう。',
  amount int(11) unsigned NOT NULL COMMENT '金額。支払いがマイナスにはならないので、unsigned とする。',
  payee int(11) unsigned NOT NULL COMMENT '支払先取引先',
  payment_method int(11) unsigned NOT NULL COMMENT '支払い方法',
  payee_bank_account int(11) unsigned COMMENT '振込先口座。payment_method_type=bank_transfer のときのみ値がある。',
  due date NOT NULL COMMENT '支払期日',
  pic int(11) unsigned NOT NULL COMMENT '担当者',
  classification int(11) unsigned NOT NULL COMMENT '仕訳',
  PRIMARY KEY (id),
  UNIQUE KEY (process_num, tenant),
  FOREIGN KEY (tenant) REFERENCES tenant (id),
  FOREIGN KEY (payee) REFERENCES business_partner (id),
  FOREIGN KEY (payment_method) REFERENCES payment_method (id),
  FOREIGN KEY (payee_bank_account) REFERENCES business_partner_bank_account (id),
  FOREIGN KEY (pic) REFERENCES user (id),
  UNIQUE KEY (classification),
  FOREIGN KEY (classification) REFERENCES classification (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='請求書処理のワークフロー。請求書の処理と支払いは一貫して行われるものと想定してまとめている。';

CREATE TABLE invoice_file (
  id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  tenant int(11) unsigned NOT NULL COMMENT 'テナント',
  filename varchar(2000) NOT NULL COMMENT 'ファイル名',
  object_url varchar(2000) NOT NULL COMMENT '請求書のファイルのURL',
  process int(11) unsigned COMMENT 'この請求書が処理されるプロセスのID。請求書をアップロードしてから、選択して処理すると推測して nullable にする。',
  PRIMARY KEY (id),
  -- UNIQUE (object_url), 長すぎてユニーク制約がつけられない。
  FOREIGN KEY (tenant) REFERENCES tenant (id),
  FOREIGN KEY (process) REFERENCES invoice_process (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='請求書ファイル。請求書の中のデータは、構造が取引先によって異なると思われるのでテーブルには入れない。';
