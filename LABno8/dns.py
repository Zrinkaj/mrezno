import dns.resolver
#import dns
#from dns import resolver


adresa = input("Unesi adresu: ")
zapis = input("Unesi tip DNS zapisa: ")

if(zapis == 'A') :
    result = dns.resolver.resolve(adresa, 'A')
    for ipval in result:
        print('IP: ', ipval.to_text())

elif(zapis == 'PTR') :
    result = dns.resolver.resolve(adresa, 'PTR')
    for ipval in result:
        print('PTR Record: ', ipval.to_text())

elif(zapis == 'MX') : 
    result = dns.resolver.resolve(adresa, 'MX')
    for ipval in result:
        print ('MX Record: ' , ipval.to_text())