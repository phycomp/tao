class SimpleModel(Module): # 假設我們有一個簡單的模型
    def __init__(self, input_dim, num_classes):
        super(SimpleModel, self).__init__()
        self.fc = Linear(input_dim, num_classes)

    def forward(self, x):
        return self.fc(x)
def rtrv準確率(preds, labels, average='macro'):
    """
    計算准確率、召回率和 F1 分數。

    參數:
    - preds: Tensor, 預測的類別
    - labels: Tensor, 真實的類別
    - average: str, 決定計算宏平均還是微平均。默認為宏平均（'macro'）

    返回:
    - accuracy: float, 准確率
    - recall: float, 召回率
    - f1_score: float, F1 分數
    """
    # 轉換為一維張量
    preds = preds.view(-1)
    labels = labels.view(-1)

    # 計算准確率
    correct = (preds == labels).sum().item()
    accuracy = correct / labels.size(0)

    # 獲取類別
    num_classes = len(unique(labels))

    # 初始化用於存儲召回率和 F1 分數的變量
    recall_list = []
    f1_score_list = []

    # 逐類別計算
    for class_id in range(num_classes):
        true_positive = ((preds == class_id) & (labels == class_id)).sum().item()
        false_positive = ((preds == class_id) & (labels != class_id)).sum().item()
        false_negative = ((preds != class_id) & (labels == class_id)).sum().item()

        # 計算召回率
        recall = true_positive / (true_positive + false_negative + 1e-10)
        recall_list.append(recall)

        # 計算精確率
        precision = true_positive / (true_positive + false_positive + 1e-10)

        # 計算 F1 分數
        f1_score = 2 * (precision * recall) / (precision + recall + 1e-10)
        f1_score_list.append(f1_score)

    # 計算平均召回率和 F1 分數
    if average == 'macro':
        recall = sum(recall_list) / num_classes
        f1_score = sum(f1_score_list) / num_classes
    elif average == 'micro':
        recall = sum(true_positive_list) / sum(true_positive_list + false_negative_list)
        precision = sum(true_positive_list) / sum(true_positive_list + false_positive_list)
        f1_score = 2 * (precision * recall) / (precision + recall + 1e-10)

    return accuracy, recall, f1_score


class ChineseMedicineModel(Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_classes):
        super(ChineseMedicineModel, self).__init__()
        self.embedding = Embedding(vocab_size, embed_size)
        self.lstm = LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x)
        x = self.fc(x[:,-1,:])
        return x
