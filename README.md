# wien
![ダウンロード](https://user-images.githubusercontent.com/72644339/117702110-0e548c00-b203-11eb-92b0-7de160929354.png)
上の画像のようなテーブルグラフを最速で作れるようにしたwebアプリケーションです。ミニマルなデザインでかつドラッグアンドドロップできる直感的な操作が魅力で、画像のトリミング機能などもついているためこのアプリ一つで完結するアプリケーションです



## 技術面の話
フロントエンド側は`githubpages`で構築し、バックエンド側は`heroku`と`cloudinore`で構築しました。リポジトリのソースには`heroku`と`cloudinore`の設定前のコードを挙げているので、自身でデプロイしたい場合は、お好きなsaasで構築してください。



## 環境構築
- node@14.16.1
- npm@6.14.12
- vue-cli@4.5.12
- python3.8.10
- django@3.2
- djangorestframework
- virtualenv

### 事前知識
- npm
- webpack
- axios
- vue
- virtualenv
- pip
- django
- djangorestframework

### リポジトリをクローン
```
git clone https://github.com/uncia002/wien.git
```
### フロントエンド
#### 1.Nodeの依存関係のインストール
```
cd frontend
npm install
```
#### 2.開発を始める
```
npm run dev
```
### バックエンド
#### 1.仮想環境を作成
```
virtualenv env
env\Scripts\activate
```
#### 2.pythonの依存関係のインストール
```
cd backend
pip3 install requirements.txt
```
#### 3.SECRET_KEYの作成
```
cd backend
python3 get_random_secret_key.py
SECRET_KEY='こちらにSECRET_KEYが生成されます'       #=の両端の空白をなくさないとエラーが出る
echo SECRET_KEY='こちらに新しく生成されたSECRET_KEYを記入' > local_settings.py
cd ..
echo local_settings.py > .gitgnore
```
詳しくは[こちら](https://qiita.com/frosty/items/bb5bc1553f452e5bb8ff)を参照してください。
#### 4.開発用サーバーの起動
```
cd..
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## アプリURL
[こちらからアプリケーション（wien）に移動できます。](https://uncia002.github.io/wien/#)

使用方法は使用例動画からご覧ください。SNSプリセットを用意しているので、`プリセットを呼び出す`に`SNS`と入力し、エンターを押してみてください。
アクセスできないようでしたら`melirandeu@gmail.com`にご連絡ください(cloudinoreを使っているのでアクセス数に限界が出たらリクエストが拒否されます。)




## 使用例動画
使用例https://www.youtube.com/watch?v=ZOvA-0TlpM4
UIが少し違います。


## メモ
https://wien-backend.herokuapp.com/
一応APIのURL及びadmin情報を記載しておきます。
admin
ユーザー名：user1
パスワード:herokudjango

