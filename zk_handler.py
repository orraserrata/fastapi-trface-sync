from pyzk.zkmodules.zkbase import ZK

def fetch_attendance_records():
    zk = ZK("0.0.0.0", port=4370, timeout=5, force_udp=False)
    conn = zk.connect()
    conn.disable_device()
    attendance = conn.get_attendance()
    conn.enable_device()
    conn.disconnect()
    return [{"user_id": r.user_id, "timestamp": r.timestamp} for r in attendance]
