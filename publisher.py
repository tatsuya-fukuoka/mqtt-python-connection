import paho.mqtt.client as mqtt
from time import sleep

# ブローカーが接続に応答した際の呼び出し関数
def on_connect(client, obj, flags, rc):
    # rc: 接続結果
    # rc = 0: 接続成功、rc != 0: 接続拒否
    print('Connection Success' if rc == 0 else 'Connection refuse')

# ブローカーから切断された際の呼び出し関数
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

# ブローカーへの送信を完了した時の呼び出し関数
def on_publish(client, obj, mid):
    print("mid: " + str(mid)) # midはパブリッシュ要求のID

if __name__ == '__main__':
    client = mqtt.Client()                  # クライアント インスタンスを作成
    client.on_connect = on_connect
    client.on_publish = on_publish

    BROKER_IP_ADDR = "192.168.43.145"       # MQTTブローカーのIPアドレス
    PORT = 1883                             # ポート番号：1883
    MAX_SECOND_CONECT = 60                  # 通信可能な許容秒数
    TOPIC = 'test'                          # トピック名
    QOS = 0

    client.connect(BROKER_IP_ADDR, PORT, MAX_SECOND_CONECT) # クライアントをブローカーに接続

    client.loop_start() # ループの開始

    i = 0
    while True:
        client.publish(TOPIC, f"Hello!! {i} time", qos=QOS) # メッセージ送信
        i+=1
        sleep(3)
