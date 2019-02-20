# 自行維護的詞庫資源  
欲編輯者請先將GITHUB的帳號告知管理者，以添加編輯權限。  
(僅下載無須權限，根據步驟1.即可clone)  
目前管理者: 游璿達  
聯絡方式:iima.yu@fubon.com  
  
  
## 使用說明:  
### 0.設定本地git帳號(從任何地方打開git bash)  
(雖然以下設定的帳號與github帳號無關，但每個人都必須要有github帳號才能push。)  
```git
git config --global user.name 'your_name'
git config --global user.email 'your_email'
```
  
### 1.從github把此專案拉到本地  
到你想要的路徑下，點滑鼠右鍵，打開git bash。(會clone一個資料夾到local)  
```git
git -c http.sslVerify=false clone https://github.com/tfbigdata/dict.git
```
  
### 2.同步雲端版本  
(pull前記得先add、commit變更，add、commit詳見步驟3.)  
在指定路徑下執行code  
(指定路徑=clone下來的資料夾。所以你可以對這個資料夾點右鍵開git bash，打開就會是在指定路徑下)  
```git
git -c http.sslVerify=false pull
```
  
### 3.上傳變更  
(先pull再push。)  
在指定路徑下開啟git bash。  
```git
git add .
git commit -m '此次提交說明文字'
git -c http.sslVerify=false push
```
  
## 檔案說明:
fbdict.txt = 自訂的詞庫  
dict_kw.csv = 自訂的主題詞庫  
  
dict.txt.big = jieba繁體詞庫  
  
ch_stopword.txt = 中文停用詞(簡)  
baidu_stopword.txt = 百度停用詞(簡)  
4u_stopword.txt = 四川大學停用詞(簡)  
h_stopword.txt = 哈爾濱工業大學停用詞(簡)  
