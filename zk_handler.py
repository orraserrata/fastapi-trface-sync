from zk import ZK

def fetch_attendance_records():
    zk = ZK("192.168.192.100", port=4370, timeout=5)  # VPN IP
    conn = zk.connect()
    conn.disable_device()
    records = conn.get_attendance()
    conn.enable_device()
    conn.disconnect()
    return [{"user_id": r.user_id, "timestamp": r.timestamp} for r in records]
