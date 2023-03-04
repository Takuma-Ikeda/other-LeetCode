# LeetCode やってみた

## NeetCode (Rust)

Rust 1.67

- https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/neetcode/README.md
- NeetCode (150 問)
  - https://neetcode.io/practice

### Docker

```sh
docker compose up -d

# rust コンテナに入る
docker compose run rust

# プロジェクト作成: プロジェクト内の .git は削除する
cargo new arrays_and_hashing
cd arrays_and_hashing

# 下記実行後、Makefile.toml 作成
cargo install cargo-make

# プログラム実行
cargo run

# コーディングが捗る
cargo make watch
```

### 参考リンク

- https://github.com/Takuma-Ikeda/study-Rust

## Difficulty (Python)

Python 3.9.6

- Easy
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/easy/README.md
- Medium
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/README.md

### pipenv インストール

```sh
# Mac の場合
brew install pipenv
pipenv install
pipenv --python 3.9.6
```

#### 起動・終了

```sh
# 起動
pipenv shell

# 終了: もしくは Ctrl + D
exit
```

#### test ファイルの実行

```sh
# python src/easy/test_two_sum.py など
python ファイル名
```

### 参考リンク

- [【基礎一覧】Pythonの基本文法を全て解説してみた！【初心者】](https://suwaru.tokyo/%e3%80%90%e5%9f%ba%e7%a4%8e%e3%81%ae%e4%b8%80%e8%a6%a7%e3%80%91python%e3%81%ae%e5%9f%ba%e6%9c%ac%e6%96%87%e6%b3%95%e3%82%92%e8%a7%a3%e8%aa%ac%e3%81%97%e3%81%a6%e3%81%bf%e3%81%9f%e3%80%90%e5%88%9d/)
