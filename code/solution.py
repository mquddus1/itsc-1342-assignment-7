# Mohammed Abdul Quddus - Assignment 7

def dissect_packet(src_ip, dst_ip, protocol, payload_bytes, flags=None):
    """Build a normalized dictionary representing a captured packet."""
    return {
        "src": src_ip,
        "dst": dst_ip,
        "proto": protocol.upper(),
        "length": max(0, payload_bytes),
        "syn_flag": flags is not None and "SYN" in flags,
    }
