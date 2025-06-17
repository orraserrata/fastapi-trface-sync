from zklib import zklib

def fetch_attendance_records():
    zk = zklib.ZKLib(ip, port)
zk.connect()
attendances = zk.get_attendance()

