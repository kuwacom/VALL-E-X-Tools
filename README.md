# What Is This
VALL-E-X 用のツール類

# How To Use
以下本家リポジトリを参考に進めていきます
https://github.com/Plachtaa/VALL-E-X


## リポジトリのクローン
先に本家リポジトリ内のソースコードの一部をコピーしてきます

必要なファイル・フォルダは

`customs` `data` `images` `models` `modules` `nltk_data` `prompts` `utils` `whisper`

の系 9フォルダです

## Python環境の作成
### 仮想環境の作成
次に `venv` を利用して環境を構築していきます

それぞれのOSにあったコマンドを実行してください
(コマンド等が違う場合はその都度修正してください)

> Windows
```shell
py -3.10 -m venv venv
```
> Linux
```bash
python3 -m venv venv
```

### モジュールのインストール
次にモジュールをインストールします

先ほど準備した仮想環境へアクティベートした状態で行ってください

```
./venv/Scripts/activate
```

プリセットでは二つの環境のみ用意してありますのでそれ以外の場合は各自変更してください

> CUDA 12.1
```bash
pip install -r req-cuda-12.1.txt
```
> CUDA 12.1
```bash
pip install -r req.txt
```

以上で環境の構築は終了です


## 動作テスト
以下のファイルを実行して動作のテストをしてください

```
test.py
```