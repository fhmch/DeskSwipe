# 01_DeskSwipe — 自作PC & デスク環境選定スタジオ

用途や好みに合わせた自作PCとデスク周りの構成をシミュレーションできるWebアプリケーションです。

- **本番URL（日本語）**: [https://fhmch.github.io/DeskSwipe/](https://fhmch.github.io/DeskSwipe/)
- **本番URL（英語）**: [https://fhmch.github.io/DeskSwipe/en/](https://fhmch.github.io/DeskSwipe/en/)
- **姉妹ツール**: [ErgoSwipe（机・椅子の高さ計算カルテ）](https://fhmch.github.io/ErgoSwipe/)

---

## 🌟 主な機能と特徴

1. **構成シミュレーション**:
   - 用途（日常事務、インディーゲーム、競技FPS、重量級3D、AI開発など）や予算に応じたパーツ構成を自動選定。
   - リアルタイムでの合計金額・消費電力・詳細スペックの表示。
2. **直感的なキャンバス ＆ 詳細インスペクター**:
   - デスク（モニター、キーボード、PCケース）＋ケース内部（クーラー、GPU、RAM、電源）の連動表示。
   - パーツごとの複数有力候補（鉄板モデル、コスパモデル、デザインモデル）の差し替え機能。
3. **グローバル（英語）対応 (`/en/`)**:
   - 海外ユーザー向けに全UIを英訳。
   - Amazon Global / Newegg / B&H Photo Video への直接リンク対応。
4. **充実のナレッジ記事 ＆ 運営者情報**:
   - 初心者向けPC自作ガイド、GPU選び、モニター選定、エルゴノミクスに関する専門記事4本を内包。
   - 信頼性を担保する運営者情報・利用規約モーダルを完備。
5. **ErgoSwipe への相互送客**:
   - ヘッダーに「📐 机・椅子の高さ計算 (ErgoSwipe) ↗」ボタンを配置し、回遊率を最大化。

---

## 📁 ディレクトリ構成

```
01_DeskSwipe/
  ├── index.html              # 日本語版メインアプリ
  ├── en/
  │    └── index.html         # 英語版メインアプリ
  ├── assets/                 # 各種ハードウェア・デスク空間の実写画像
  ├── data/
  │    └── parts_catalog.json # パーツマスターデータ
  ├── scripts/                # データ更新・画像検証用Pythonスクリプト
  ├── robots.txt / sitemap.xml# SEO設定ファイル
  └── README.md
```

---

## 💰 収益化・アフィリエイト

- **もしもアフィリエイト サイトID**: `5840290`
- **提携先**: 楽天市場、Yahoo!ショッピング、Amazon.co.jp（再審査準備中）
