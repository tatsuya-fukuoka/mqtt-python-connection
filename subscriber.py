import paho.mqtt.client as mqtt

# ブローカーが接続に応答した際の呼び出し関数
def on_connect(client, obj, flags, rc):
    # rc: 接続結果
    # rc = 0: 接続成功、rc != 0: 接続拒否
    print('Connection Success' if rc == 0 else 'Connection refuse')

# サブスクライブしているトピックでメッセージが受信された時の呼び出し関数
def on_message(client, obj, msg):
    print(f'TOPIC: {msg.topic}, QOS: {msg.qos}, PAYLOAD: {msg.payload}')
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# ブローカがサブスクライブのリクエストに応答する時の呼び出す関数
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

if __name__ == '__main__':
    client = mqtt.Client()                  # クライアント インスタンスを作成
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe

    BROKER_IP_ADDR = "localhost"            # MQTTブローカーのIPアドレス
    PORT = 1883                             # ポート番号：1883
    MAX_SECOND_CONECT = 60                  # 通信可能な許容秒数
    TOPIC = 'test'                          # トピック名

    client.connect(BROKER_IP_ADDR, PORT, MAX_SECOND_CONECT) # クライアントをブローカーに接続
    client.subscribe(TOPIC) # クライアントを1つ以上のトピックにサブスクライブ

    client.loop_forever()