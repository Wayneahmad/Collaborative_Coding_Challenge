"""
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example,  "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses 
        while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses."""

def validate_ipv4(string: str):
    # "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros
    false_list = []
    ipv4_parts = string.split('.')
    if len(ipv4_parts) != 4:
        return False
    
    for ipv4_part in ipv4_parts:
        print(ipv4_part, 'part 1')
        if ipv4_part == '':
            return False
        
        if ipv4_part[0] ==  '0' and ipv4_part != '0':
            return False
        try:
            num = int(ipv4_part)
            if num <0 or num>255:
                return False
        except:
            return False
        
    for ipv4_part in ipv4_parts:
        # print(ipv4_part, ' part 1')
        false_list.append(ipv4_part.isnumeric())
        if False in false_list:
            return False
    

   
    return True

list_string =  [
        "192.168.1.0",
        "192.168@1.1",
        "192.168.1.00",
        "192.168.1.-0",
        "192.168.1."
    ]

for i in list_string:
    validate_ipv4(i)