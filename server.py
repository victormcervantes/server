import socket, sys
import _thread as thread


host = ''
port = int(sys.argv[1])



def on_new_client(clientsocket, addr, name):
	while True:
		msg = clientsocket.recv(1024)
		if not msg: break
		f = open('log.txt', 'w')
		f.write(msg + '\n')
		f.close()
		print (addr, '[',name,'] >> ', msg.decode("utf-8"))
		# msg = raw_input('SERVER >>')
		clientsocket.send(b'got your msg!\r\n')
	print('closing ',addr)
	clientsocket.close()




names = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host,port))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		names.append(conn)
		thread.start_new_thread(on_new_client, (conn,addr,len(names)))
	s.close()
