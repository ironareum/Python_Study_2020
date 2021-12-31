"""
socket: 연결된 네트워크 양 끝단의 추상개념. 네트워크로 통하는 컴퓨터의 외부와 컴퓨터 내부의 프로그램을 이어주는 인터페이스. (네트워크 반대편이 어디인지에 대한 정보를 가짐)
socket 모듈은 소켓프로그래밍에 필요한 시스템 콜을 래핑하는 API를 제공하는 모듈.


1. 소켓 객체 생성
# socket.socket(패밀리=, 타입=)=> (소켓이 사용할 주소 체계, 소켓 타입)
  socket.socket(socket.AF_INET, socket.SOCK_STREAM) => 기본값
    - 패밀리(주소체계): PF_INET / AF_INET (상수값 같음)
      AF_INET 주소체계: AF_INET(IPv4 인터넷 프로토콜), AF_INET6(IPv6 인터넷 프로토콜), AF_LOCAL(LOCAL 통신을 위한 UNIX프로토콜)
    - 소켓타입: SOCKET_STREAM(TCP소켓을 할당할때 사용되는 인자값) / SOCK_DGRAM(UDP소켓을 할당할때 사용되는 인자)
      SOCKET_STREAM: 소켓과 소켓이 계속 연결되어 있는 상태유지. 1 vs 1 연결.
      SOCK_DGRAM: 소켓이 특정주소로 메세지를 보내고 다른 한 소켓은 연결상태 관련없이 메세지가 오면 받기만 하면 됨. 주소로 보내기만 할 뿐이지 데이터의 파손이나 분실에 대해서는 체크할수 없음.

2. 소켓을 포트에 맵핑, 상대측 포트에 연결 (서버측/클라이언트측 구성방식 다름)
# 서버 (최초의 수신자가 되는 노드를 의미)
    # 바인드와 리스닝(같은 포트로 여러 클라이언트와 동시에 접속 될 수 있기때문.)
      바인드: 프로그램 인터페이스인 소켓과 네트워크 자원인 포트를 연결하는 행위.
      - 바인딩: 서버가 소켓을 포트에 맵핑하는 행위.
        이는 생성된 소켓 객체에 대해서 sock.bind()호출함 (호스트이름과 포트번호를 튜플로 전달)
        sock = socket.socket()
        host = 'localhost'
        port = 7777
        sock.bind((host, port))
      - 리스닝: 소켓에 대해 listen()메소드 호출.
        socket.listen()
        클라이언트가 바인드된 포트로 연결을 할때까지 기다리는 블럭킹 함수.
        클라이언트로부터 연결 요청이 들어오면 리턴.
        따라서 이코드의 다음 행에는 해당 연결을 받아들이기 위한 accept()메소드를 호출하는 부분이 옴.
        accept()는 (소켓, 주소정보)로 구성되는 튜플을 리턴. 여기서의 소켓은 처음 생성한 소켓과는 별개.
    # 정보 주고 받기
      - sock.recv(): 소켓으로부터 데이터를 읽을때
        *데이터를 읽어들일때 버퍼의 크기를 전달해야함.
        sock.recv(bufsize)는 최대 bufsize 바이트 만큼의 데이터를 읽어옴. 읽어올 데이터가 없을땐 대기.
        읽어들인 데이터는 바이트 타입의 byte squence이며, 문자열을 주고받고 싶다면 해당 문자열을 인코딩/디코딩 해서 전달해야함.
      - sock.sendall(): 정보를 보낼때
        send() 메소드: sendall()과는 달리 리턴값이 있음. 바로 실제 전송된 바이트 수를 리턴함.
    # 닫기
      - socket.close()
      - 연결 종료시 서버와 클라이언트 모두 소켓을 닫아야 함.
      - 참고로 소켓 객체는 컨텍스트 매니저 프로토콜을 지원하므로 with구문과 함께 사용하면 안전하게 닫히는것을 보장할 수 있음.

# 클라이언트가 서버에 연결하기 - connect (1:1통신. 바인드나 리스닝 필요x)
    # sock.connect() (인자는 bind()와 동일)
      리턴값 존재x.
"""

import socket

mysock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
