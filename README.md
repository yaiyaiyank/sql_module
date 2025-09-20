<div style="text-align:center; font-size:60px;"><b>SQLをオブシコで。</b></div>

## 目的

みなさんこんばんは、にじきんじ所属のヤイヤイさんです。このリポジトレィは肥大化した自作ライブラリをポリレポ化する試みです。

### !

トップモジュール: yaiで管理された[Logモジュール](https://github.com/yaiyaiyank/logging_module)に依存あり

### tips

AUTO_INCREMENTのidがオーバーフローするには1日100万回レコード追加したとしても20万年かかるのでその心配はない by ChatGPT
(追記: ChatGPTいわく「PRIMARY KEY AUTOINCREMENT は「一度使った値を二度と再利用しない」「常に過去最大値より大きい値」という追加ルールがつき、内部の sqlite_sequence を使います。速度や断片化の面で不利なことが多いので、厳密な単調増加が必要な場合以外は付けないのが定石です。」とのことなので、AUTO_INCREMENTは廃止しました。)
