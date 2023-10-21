class Link:
   """
   Class for network links.  As currently written, assumes costs are calculated as the
   sum of three factors:
      1. Travel time, computed via the BPR function
      2. Toll cost, the product of toll and network.tollFactor
      3. Distance-related costs, the product of length and network.distanceFactor
   """
   
   def __init__(self, network, tail, head, capacity = 99999, length = 99999, freeFlowTime = 99999, alpha = 0.15, beta = 4, speedLimit = 99999, toll = 0, linkType = 0):
      """
      Initializer for links; note default values for parameters if not specified.
      For the classic traffic assignment problem speedLimit and linkType do  not
      have any impact (and length and toll are only relevant if a distanceFactor
      or tollFactor are specified). 
      """
      self.network = network
      self.tail = tail
      self.head = head
      self.capacity = capacity
      self.length = length
      self.freeFlowTime = freeFlowTime
      self.alpha = alpha
      self.beta = beta
      self.speedLimit = speedLimit
      self.toll = toll
      self.linkType = linkType
      
   def calculateCost(self):
      """
      Calculates the cost of the link using the BPR relation, adding in toll and
      distance-related costs.
      This cost is returned by the method and NOT stored in the cost attribute.
      """   
      vcRatio = self.flow / self.capacity
      travelTime = self.freeFlowTime * (1 + self.alpha * pow(vcRatio, self.beta))
      #print(travelTime, self.toll, tollFactor)
      return travelTime + self.toll * self.network.tollFactor + self.length * self.network.distanceFactor 

   def updateCost(self):
      """
      Same as calculateCost, except that the link.cost attribute is updated as well.
      """   
      self.cost = self.calculateCost()
