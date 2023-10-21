import network

if __name__ == '__main__':
   newNetwork = network.Network("tests/SiouxFalls_net.txt", "tests/SiouxFalls_trips.txt")
   print(len(newNetwork.link))
   print(str(newNetwork))