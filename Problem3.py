def check_network(mobile_number):
   key_digits = mobile_number[2:4]
  
networks = {
    'smart' : ['13', '14, '20', '21', '28', '29', '30']
    'TNT': ['09', '09', '10', '11', '12', '18', '19']
    'Sun': ["22", "23", "32", "33"]
    'Globe' : ["15", "16", "17", "25", "26", "27"]
    'TM': ["03", "04", "05", "06", "07"]
    'Red': ["01", "02", "24"]
    'Dito' :["91", "92", "93", "94", "95", "96", "97"]

   }

    for network, prefix in networks.items():
        if key_digits in prefixes:
            return network
        
        return "Unknown network"

def main():
    mobile_number = input("Enter a mobile number: ").strip()
 
 if len(mobile_number) == 11 and mobile_number[0:2] == "09":
        network = check_network(mobile_number)
       else:
            print(" Invalid!")

main()

    
