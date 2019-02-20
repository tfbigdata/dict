# 自行維護的詞庫資源  
欲編輯者請先將GITHUB的帳號告知管理者，以添加編輯權限。  
(僅下載則無需告知，根據步驟1.即可clone)  
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
  
### 2.上傳變更  
(如果你有進行任何修改，請記得上傳並再提交時稍微描述變更內容。
未進行上傳的變更，在你下次與雲端同步的時候，都會被覆蓋掉。)  
到clone下來的資料夾(應該都是tfb_bigdata_dict)點右鍵打開git bash  
```git
git add .
git commit -m '此次提交說明文字'
git -c http.sslVerify=false push
```

### 3.同步雲端版本  
(如果你有進行任何修改，請記得上傳並再提交時稍微描述變更內容。
未進行上傳的變更，在你下次與雲端同步的時候，都會被覆蓋掉。)  
到clone下來的資料夾點右鍵打開git bash  
```git
git -c http.sslVerify=false pull
```

## 檔案說明:
fbdict.txt = 自訂的詞庫  
dict_kw.csv = 自訂的主題詞庫  
  
dict.txt.big = jieba繁體詞庫  
  
ch_stopword.txt = 中文停用詞(簡)  
baidu_stopword.txt = 百度停用詞(簡)  
4u_stopword.txt = 四川大學停用詞(簡)  
h_stopword.txt = 哈爾濱工業大學停用詞(簡)  
