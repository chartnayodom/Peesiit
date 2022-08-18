"""Ping"""
def time_s(ips):
    """find time"""
    ind1 = ips.index("time")
    ind2 = ips.index("ms")
    time = ips[ind1+4:ind2]
    #print(time)
    if time.count("<") > 0:
        return 0
    elif time.count("=") > 0:
        return int(time[1:])

def maxi(num1, num2):
    """max"""
    if num1 >= num2:
        return num1
    else:
        return num2

def mini(num1, num2):
    """min"""
    if num1 <= num2:
        return num1
    else:
        return num2

def pinga(re_1, re_2, re_3, re_4, ip_):
    """TESARACT"""
    rec = 0
    lost = 0
    time_a = 0
    m_x = 0
    m_n = 9999999
    if re_1.count(ip_) > 0:
        time_s(re_1)
        m_x = maxi(m_x, time_s(re_1))
        m_n = mini(m_n, time_s(re_1))
        time_a += time_s(re_1)
        rec += 1
    else:
        lost += 1
    if re_2.count(ip_) > 0:
        time_s(re_2)
        m_x = maxi(m_x, time_s(re_2))
        m_n = mini(m_n, time_s(re_2))
        time_a += time_s(re_2)
        rec += 1
    else:
        lost += 1
    if re_3.count(ip_) > 0:
        time_s(re_3)
        m_x = maxi(m_x, time_s(re_3))
        m_n = mini(m_n, time_s(re_3))
        time_a += time_s(re_3)
        rec += 1
    else:
        lost += 1
    if re_4.count(ip_) > 0:
        time_s(re_4)
        m_x = maxi(m_x, time_s(re_4))
        m_n = mini(m_n, time_s(re_4))
        time_a += time_s(re_4)
        rec += 1
    else:
        lost += 1
    avg = (lost/4)*100
    if lost == 4:
        print("""Ping statistics for %s:
    Packets: Sent = 4, Received = %d, Lost = %d (%d%s loss),""" %(ip_, rec, lost, int(avg), "%"))
        print()
        print()
    else:
        print("Ping statistics for %s:" %ip_)
        print("    Packets: Sent = 4, Received = %d, Lost = %d (%d%s loss)," \
            %(rec, lost, int(avg), "%"))
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(m_n, m_x, int(time_a/rec)))

def main():
    """Main function"""
    input()
    input()
    ping = input()
    re_1 = input()
    re_2 = input()
    re_3 = input()
    re_4 = input()
    #หาเลขip
    if ping.count("[") > 0:
        ipbr = ping.index("[")
        ipbr2 = ping.index("]")
        ip_ = ping[ipbr+1:ipbr2]
        #print(ip_)
    else:
        end = ping.index(" with")
        ip_ = ping[8:end]
        #print(ip_)
    #check packageที่pingไป
    pinga(re_1, re_2, re_3, re_4, ip_)


main()
