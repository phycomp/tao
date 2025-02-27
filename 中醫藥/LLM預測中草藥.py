from transformers import BertTokenizer, BertModel
from stUtil import rndrCode
from torch import unique, cat as trchCAT
from torch.nn import Module, Embedding, LSTM, Linear, CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset
from herbalUtil import ChineseMedicineModel, rtrv準確率
from torch import randn as trchRndn, randint as trchRndint

MENU, 表單=[], ['訓練', '預測']	#, '錯綜複雜', '二十四節氣'
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  srch=text_input('搜尋', '')
if menu==len(表單):
  pass
elif menu==MENU[1]:
  tblName='sutra'
elif menu==MENU[0]: #訓練
  input_dim, num_classes, batch_size=20, 3, 32 # 准備數據 假設數據有1000條樣本，特徵維度為20，分類為3個類別
  tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
  model = BertModel.from_pretrained("bert-base-chinese")
  model = ChineseMedicineModel(vocab_size=5000, embed_size=300, hidden_size=512, num_classes=10)
  criterion = CrossEntropyLoss()
  optimizer = Adam(model.parameters(), lr=0.001)
  for epoch in range(10): # 假設您已經創建了 DataLoader 數據
      for data, labels in data_loader:
          optimizer.zero_grad()
          outputs = model(data)
          loss = criterion(outputs, labels)
          loss.backward()
          optimizer.step()


  x_data = trchRndn(1000, input_dim)
  y_data = trchRndint(0, num_classes, (1000,))

  dataset = TensorDataset(x_data, y_data)
  data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

  model = SimpleModel(input_dim, num_classes) # 初始化模型、損失函數和優化器
  criterion = CrossEntropyLoss()
  optimizer = Adam(model.parameters(), lr=0.001)
  #epochs = 5 #for epoch in range(epochs):
  LOSS, EPS=1, 1e-6
  while LOSS>EPS: # 訓練模型
      model.train()
      all_preds = []
      all_labels = []
      epoch_loss = 0

      for inputs, labels in data_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        loss.backward() # 反向傳播和優化
        optimizer.step()

        epoch_loss += loss.item()

        # 記錄預測和真實標簽
        _, preds = torch.max(outputs, 1)
        all_preds.append(preds)
        all_labels.append(labels)
        all_preds = trchCAT(all_preds) # 將所有批次的預測和標簽拼接起來
        all_labels = trchCAT(all_labels)
        accuracy, recall, f1_score = calculate_metrics(all_preds, all_labels) # 計算准確率、召回率和 F1 分數
        LOSS= epoch_loss/len(data_loader)
        #print(f"Epoch {epoch+1}/{epochs}")
        rndrCode(f"Loss: {epoch_loss/len(data_loader):.4f} | Accuracy: {accuracy:.4f} | Recall: {recall:.4f} | F1 Score: {f1_score:.4f}")
