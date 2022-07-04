# fiftyone-playground-docker
fiftyone-playground-dockerは機械学習に用いるデータセットのフォーマットを変換するためのスクリプトです。

## 事前準備
Python 3.7 - 3.10 をインストールしておいてください。

### env.jsonの作成
sampleファイルからenv.json5を作成してください。

```
data_path・・・datasetが置いてあるパス情報を記載します。
export・・・labelの情報が書き出しされるパス情報を記載します。

```

#### envファイルの生成
下記のコマンドでenvファイルを生成します。

```
make create-env
```

## formatを変換する
データセットのformatを変換して、exportで指定してあるpathに書き出しされます。

```
make convert
```

## 変換したデータセットの確認
envファイルのlaunch_appで指定しているport番号にlocalhostでアクセスすると、確認できます。

```
make launch-app
```
