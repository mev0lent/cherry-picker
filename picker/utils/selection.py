import ipaddress

def select_first_octet_bias(hosts):
    """
    Picks IP addresses with a bias towards common important addresses like .1, .10, .254.
    """
    important_suffixes = [1, 2, 10, 20, 50, 100, 200, 254]

    prioritized = []
    for ip in hosts:
        last_octet = int(str(ip).split('.')[-1])
        if last_octet in important_suffixes:
            prioritized.append(ip)

    return prioritized
