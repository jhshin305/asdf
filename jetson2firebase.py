#-*-coding: utf-8-*-

import firebase_admin
from firebase_admin import credentials, firestore, messaging, db

# 서비스 계정 키 파일을 사용하여 Admin SDK 초기화
# 'recycling-3b4ba-firebase-adminsdk-fbsvc-...' 파일 경로를 정확히 지정해야 합니다.
# 이 파일은 다운로드하여 안전하게 관리해야 합니다.
cred = credentials.Certificate('recycling-3b4ba-firebase-adminsdk-fbsvc-2194838d4b.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# rdb = firestore.reference('https://recycling-3b4ba-default-rtdb.firebaseio.com/')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://recycling-3b4ba-default-rtdb.firebaseio.com/'
})
dir = db.reference()
database = firestore.client()

def send_log(binType):
    database.collection(binType).add({
        'time': firestore.SERVER_TIMESTAMP
    })

def update_count(binType):
    dir = db.reference('currData/' + binType)
    value = dir.get()
    if value is None:
        value = 0
    else:
        value = int(value) + 1
    dir.set(value)

def update_full(binType):
    dir = db.reference('isFull/' + binType)
    dir.set(True)

def new_send_alert(binType):
    print(f"Sending alert for {binType} bin...")
    database.collection("alert").add({
        'type': binType,
        'time': firestore.SERVER_TIMESTAMP
    })

    # doc_ref1 = db.collection("fcmTokens")
    # tokens = doc_ref1.get()
    # registration_token = None
    doc_ref1 = database.collection("admin").document("fcmToken")
    # print(doc_ref1.get().to_dict())
    registration_token = doc_ref1.get().to_dict()['value']
    print(f"Registration token: {registration_token}")
    alertMessage = {
        'plastic': '플라스틱이 가득 찼습니다',
        'glass': '유리이 가득 찼습니다',
        'paper': '종이이 가득 찼습니다',
        'can': '캔이 가득 찼습니다',
    }


    # 푸시 알림을 받을 기기의 등록 토큰
    # for token_doc in tokens:
        # token_data = token_doc.to_dict()
        # registration_token = token_data.get('token')
        

    if registration_token:
        # 보낼 메시지 구성
        message = messaging.Message(
            notification=messaging.Notification(
                title='RecyclingBin',  # 알림 제목
                body=alertMessage.get(binType, '알 수 없는 알림'),  # 알림 내용
            ),
            token=registration_token,  # 특정 토큰으로 보내기
        )

        # 메시지 전송
        try:
            response = messaging.send(message)
            # 성공 시 메시지 ID가 반환됩니다.
            print('Successfully sent message:', response)
        except Exception as e:
            print('Error sending message:', e)
    else:
        print(f"Token not found in document {token_doc.id}")

def send_alert(binType):
    doc_ref = database.collection("recycling").document("recycling")
    data = doc_ref.get().to_dict()
    fullBin = []
    for key, value in data.items():
        print(value)
        if value >= 100:  # 100 이상인 경우
            fullBin.append(key)

    # 푸시 알림을 받을 기기의 등록 토큰
    # 클라이언트 앱에서 FCM SDK를 통해 얻어온 토큰입니다.
    doc_ref1 = db.collection("admin").document("fcmToken")
    # doc_ref1 = database.collection("admin").document("123456789")
    # print(doc_ref1.get().to_dict())
    registration_token = doc_ref1.get().to_dict()['test']

    # 보낼 메시지 구성
    # notification 필드는 기기 배경 상태일 때 알림을 표시합니다.
    # data 필드는 앱으로 전달되는 임의의 키-값 데이터입니다.
    message = messaging.Message(
        notification=messaging.Notification(
            title='full',  # 알림 제목
            body=', '.join(fullBin), # 알림 내용
        ),
        token=registration_token, # 특정 토큰으로 보내기
    )

    # 메시지 전송
    try:
        response = messaging.send(message)
        # 성공 시 메시지 ID가 반환됩니다.
        print('Successfully sent message:', response)
    except Exception as e:
        print('Error sending message:', e)

